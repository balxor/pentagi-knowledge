---
cwe_id: CWE-325
name: Missing Cryptographic Step
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-68]
url: https://cwe.mitre.org/data/definitions/325.html
tags: [mitre-cwe, weakness, CWE-325]
---

# CWE-325 - Missing Cryptographic Step

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-325](https://cwe.mitre.org/data/definitions/325.html)

## Description
The product does not implement a required step in a cryptographic algorithm, resulting in weaker encryption than advertised by the algorithm.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data
- **Accountability, Non-Repudiation**: Hide Activities

## Related attack patterns (CAPEC)
- [CAPEC-68](https://capec.mitre.org/data/definitions/68.html)

## Related weaknesses
- CWE-1240 (ChildOf)
- CWE-573 (ChildOf)
- CWE-358 (PeerOf)

## Observed examples (CVE)
- **CVE-2001-1585**: Missing challenge-response step allows authentication bypass using public key.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/325.html
