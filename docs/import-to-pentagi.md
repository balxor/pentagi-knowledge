# Importing into PentAGI Knowledges

Run these commands from the repository root:

```bash
cd pentagi-knowledge
pip install -r requirements.txt
```

The ATT&CK, CWE, and CAPEC build scripts regenerate files before pushing them.
If you only want to import the committed snapshot, check your working tree after
running the commands and review any generated changes before committing.

## 1. Configure an embedding provider

PentAGI embeds knowledge documents into pgvector when they are created, so an
embedding provider must be configured in the PentAGI `.env`.

**Local Ollama:**

```env
EMBEDDING_PROVIDER=ollama
EMBEDDING_URL=http://host.docker.internal:11434
EMBEDDING_MODEL=nomic-embed-text
```

```bash
ollama pull nomic-embed-text
```

If PentAGI runs in Docker and Ollama runs on the host, allow Docker to reach
Ollama by setting `OLLAMA_HOST=0.0.0.0` on the host, then restart Ollama.

**OpenAI:**

```env
EMBEDDING_PROVIDER=openai
EMBEDDING_KEY=sk-...
EMBEDDING_MODEL=text-embedding-3-small
```

Restart PentAGI after editing `.env`:

```bash
docker compose up -d
```

## 2. Create an API token

In the PentAGI UI, go to **Settings -> PentAGI API**, create a bearer token,
and store it in an environment variable.

PowerShell:

```powershell
$env:PENTAGI_API_TOKEN = "<token>"
```

cmd.exe:

```cmd
set PENTAGI_API_TOKEN=<token>
```

Linux/macOS:

```bash
export PENTAGI_API_TOKEN="<token>"
```

## 3. Push MITRE ATT&CK

For local PentAGI with self-signed TLS, keep `--insecure`. Remove it when using
a host with a trusted certificate.

PowerShell:

```powershell
python tools/build_attack_knowledge.py --domain enterprise --out ./mitre/attack/enterprise --push --pentagi-url https://localhost:8443 --token $env:PENTAGI_API_TOKEN --insecure
python tools/build_attack_knowledge.py --domain mobile --out ./mitre/attack/mobile --push --pentagi-url https://localhost:8443 --token $env:PENTAGI_API_TOKEN --insecure
python tools/build_attack_knowledge.py --domain ics --out ./mitre/attack/ics --push --pentagi-url https://localhost:8443 --token $env:PENTAGI_API_TOKEN --insecure
```

cmd.exe:

```cmd
python tools\build_attack_knowledge.py --domain enterprise --out .\mitre\attack\enterprise --push --pentagi-url https://localhost:8443 --token "%PENTAGI_API_TOKEN%" --insecure
python tools\build_attack_knowledge.py --domain mobile --out .\mitre\attack\mobile --push --pentagi-url https://localhost:8443 --token "%PENTAGI_API_TOKEN%" --insecure
python tools\build_attack_knowledge.py --domain ics --out .\mitre\attack\ics --push --pentagi-url https://localhost:8443 --token "%PENTAGI_API_TOKEN%" --insecure
```

Linux/macOS:

```bash
python tools/build_attack_knowledge.py --domain enterprise --out ./mitre/attack/enterprise --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN" --insecure
python tools/build_attack_knowledge.py --domain mobile --out ./mitre/attack/mobile --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN" --insecure
python tools/build_attack_knowledge.py --domain ics --out ./mitre/attack/ics --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN" --insecure
```

ATT&CK documents are created with `docType: guide`, `guideType: pentest`,
`question` as the searchable title, and `content` as the full Markdown document.

## 4. Push CWE and CAPEC

PowerShell:

```powershell
python tools/build_cwe_knowledge.py --out ./mitre/cwe --push --pentagi-url https://localhost:8443 --token $env:PENTAGI_API_TOKEN --insecure
python tools/build_capec_knowledge.py --out ./mitre/capec --push --pentagi-url https://localhost:8443 --token $env:PENTAGI_API_TOKEN --insecure
```

cmd.exe:

```cmd
python tools\build_cwe_knowledge.py --out .\mitre\cwe --push --pentagi-url https://localhost:8443 --token "%PENTAGI_API_TOKEN%" --insecure
python tools\build_capec_knowledge.py --out .\mitre\capec --push --pentagi-url https://localhost:8443 --token "%PENTAGI_API_TOKEN%" --insecure
```

Linux/macOS:

```bash
python tools/build_cwe_knowledge.py --out ./mitre/cwe --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN" --insecure
python tools/build_capec_knowledge.py --out ./mitre/capec --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN" --insecure
```

CWE documents are created as `docType: answer`, `answerType: vulnerability`.
CAPEC documents are created as `docType: guide`, `guideType: pentest`.

## 5. Push tooling overlays

Tooling files under `tooling/` are curated Markdown files and are not generated.
Only directories that exist can be pushed; currently the committed overlay is
`tooling/enterprise`.

PowerShell:

```powershell
python tools/push_tooling.py --dir tooling/enterprise --pentagi-url https://localhost:8443 --token $env:PENTAGI_API_TOKEN --insecure
```

cmd.exe:

```cmd
python tools\push_tooling.py --dir tooling\enterprise --pentagi-url https://localhost:8443 --token "%PENTAGI_API_TOKEN%" --insecure
```

Linux/macOS:

```bash
python tools/push_tooling.py --dir tooling/enterprise --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN" --insecure
```

Tooling overlays are created with `docType: code`, `codeLang: markdown`,
`question` as the file stem, and `content` as the full Markdown document.

## 6. Verify

In the PentAGI UI, open **Knowledges** and run semantic searches:

| Query | Expected result |
|-------|-----------------|
| "dump credentials from LSASS" | T1003 (OS Credential Dumping) |
| "format string vulnerability" | CWE-134 |
| "sql injection attack pattern" | CAPEC-66 |
| "powershell download cradle" | T1059.001 tooling entry |
