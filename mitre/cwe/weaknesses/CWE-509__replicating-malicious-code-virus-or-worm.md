---
cwe_id: CWE-509
name: Replicating Malicious Code (Virus or Worm)
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/509.html
tags: [mitre-cwe, weakness, CWE-509]
---

# CWE-509 - Replicating Malicious Code (Virus or Worm)

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-509](https://cwe.mitre.org/data/definitions/509.html)

## Description
Replicating malicious code, including viruses and worms, will attempt to attack other systems once it has successfully compromised the target system or the product.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Operation**: Antivirus software scans for viruses or worms.
- **Installation**: Always verify the integrity of the software that is being installed.

## Related weaknesses
- CWE-507 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/509.html
