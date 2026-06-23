---
cwe_id: CWE-314
name: Cleartext Storage in the Registry
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-37]
url: https://cwe.mitre.org/data/definitions/314.html
tags: [mitre-cwe, weakness, CWE-314]
---

# CWE-314 - Cleartext Storage in the Registry

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-314](https://cwe.mitre.org/data/definitions/314.html)

## Description
The product stores sensitive information in cleartext in the registry.

## Extended description
Attackers can read the information by accessing the registry key. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related attack patterns (CAPEC)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)

## Related weaknesses
- CWE-312 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-2227**: Cleartext passwords in registry key.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/314.html
