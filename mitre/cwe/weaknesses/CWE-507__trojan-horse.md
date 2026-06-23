---
cwe_id: CWE-507
name: Trojan Horse
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-698]
url: https://cwe.mitre.org/data/definitions/507.html
tags: [mitre-cwe, weakness, CWE-507]
---

# CWE-507 - Trojan Horse

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-507](https://cwe.mitre.org/data/definitions/507.html)

## Description
The product appears to contain benign or useful functionality, but it also contains code that is hidden from normal operation that violates the intended security policy of the user or the system administrator.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Operation**: Most antivirus software scans for Trojan Horses.
- **Installation**: Verify the integrity of the product that is being installed.

## Related attack patterns (CAPEC)
- [CAPEC-698](https://capec.mitre.org/data/definitions/698.html)

## Related weaknesses
- CWE-506 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/507.html
