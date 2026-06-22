# Importing into PentAGI Knowledges

## 1. Configure an embedding provider

PentAGI embeds every knowledge document into pgvector on creation, so an embedding
provider must be available. In your PentAGI `.env`:

**Local / free (Ollama):**
```env
EMBEDDING_PROVIDER=ollama
EMBEDDING_URL=http://host.docker.internal:11434
EMBEDDING_MODEL=nomic-embed-text
```
```bash
ollama pull nomic-embed-text
# allow Docker to reach Ollama: set OLLAMA_HOST=0.0.0.0 on the host, then restart Ollama
```

**OpenAI:**
```env
EMBEDDING_PROVIDER=openai
EMBEDDING_KEY=sk-...
EMBEDDING_MODEL=text-embedding-3-small
```

Restart PentAGI so `.env` is reloaded:
```bash
docker compose up -d
```

## 2. Create an API token

PentAGI UI -> **Settings -> PentAGI API** -> create a Bearer token (copy it once).

## 3. Push the pack

```bash
python tools/build_attack_knowledge.py --out ./mitre/attack/enterprise \
  --push --pentagi-url https://localhost:8443 --token "$PENTAGI_API_TOKEN"
```

The push uses the real PentAGI schema:

```graphql
createKnowledgeDocument(input: CreateKnowledgeDocumentInput!): KnowledgeDocument!
```
with `docType: guide`, `guideType: pentest`, and `question` set to the document title
(the field embedded for semantic search). The GraphQL endpoint is
`<pentagi-url>/api/v1/graphql`; for local self-signed TLS the script skips certificate
verification.

## 4. Verify

PentAGI UI -> **Knowledges** -> semantic search e.g. *"dump credentials from LSASS"* should
return T1003 and related techniques.
