---
cwe_id: CWE-508
name: Non-Replicating Malicious Code
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/508.html
tags: [mitre-cwe, weakness, CWE-508]
---

# CWE-508 - Non-Replicating Malicious Code

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-508](https://cwe.mitre.org/data/definitions/508.html)

## Description
Non-replicating malicious code only resides on the target system or product that is attacked; it does not attempt to spread to other systems.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Operation**: Antivirus software can help mitigate known malicious code.
- **Installation**: Verify the integrity of the software that is being installed.

## Related weaknesses
- CWE-507 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/508.html
