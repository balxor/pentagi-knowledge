---
cwe_id: CWE-514
name: Covert Channel
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-463]
url: https://cwe.mitre.org/data/definitions/514.html
tags: [mitre-cwe, weakness, CWE-514]
---

# CWE-514 - Covert Channel

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-514](https://cwe.mitre.org/data/definitions/514.html)

## Description
A covert channel is a path that can be used to transfer information in a way not intended by the system's designers.

## Extended description
Typically the system has not given authorization for the transmission and has no knowledge of its occurrence.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Access Control**: Read Application Data, Bypass Protection Mechanism

## Related attack patterns (CAPEC)
- [CAPEC-463](https://capec.mitre.org/data/definitions/463.html)

## Related weaknesses
- CWE-1229 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/514.html
