---
cwe_id: CWE-664
name: Improper Control of a Resource Through its Lifetime
type: weakness
abstraction: Pillar
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-196, CAPEC-21, CAPEC-60, CAPEC-61, CAPEC-62]
url: https://cwe.mitre.org/data/definitions/664.html
tags: [mitre-cwe, weakness, CWE-664]
---

# CWE-664 - Improper Control of a Resource Through its Lifetime

**Abstraction:** Pillar  -  **Status:** Draft  -  **CWE:** [CWE-664](https://cwe.mitre.org/data/definitions/664.html)

## Description
The product does not maintain or incorrectly maintains control over a resource throughout its lifetime of creation, use, and release.

## Extended description
Resources often have explicit instructions on how to be created, used and destroyed. When code does not follow these instructions, it can lead to unexpected behaviors and potentially exploitable states. Even without explicit instructions, various principles are expected to be adhered to, such as "Do not use an object until after its creation is complete," or "do not use an object after it has been slated for destruction."

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Other**: Other

## Related attack patterns (CAPEC)
- [CAPEC-196](https://capec.mitre.org/data/definitions/196.html)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
- [CAPEC-61](https://capec.mitre.org/data/definitions/61.html)
- [CAPEC-62](https://capec.mitre.org/data/definitions/62.html)

## Observed examples (CVE)
- **CVE-2018-1000613**: Cryptography API uses unsafe reflection when deserializing a private key
- **CVE-2019-19911**: Chain: Python library does not limit the resources used to process images that specify a very large number of bands (CWE-1284), leading to excessive memory consumption (CWE-789) or an integer overflow (CWE-190).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/664.html
