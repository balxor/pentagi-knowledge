---
cwe_id: CWE-553
name: Command Shell in Externally Accessible Directory
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-650]
url: https://cwe.mitre.org/data/definitions/553.html
tags: [mitre-cwe, weakness, CWE-553]
---

# CWE-553 - Command Shell in Externally Accessible Directory

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-553](https://cwe.mitre.org/data/definitions/553.html)

## Description
A possible shell file exists in /cgi-bin/ or other accessible directories. This is extremely dangerous and can be used by an attacker to execute commands on the web server.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Installation, System Configuration**: Remove any Shells accessible under the web root folder and children directories.

## Related attack patterns (CAPEC)
- [CAPEC-650](https://capec.mitre.org/data/definitions/650.html)

## Related weaknesses
- CWE-552 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/553.html
