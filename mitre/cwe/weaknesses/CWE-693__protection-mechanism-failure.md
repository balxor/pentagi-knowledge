---
cwe_id: CWE-693
name: Protection Mechanism Failure
type: weakness
abstraction: Pillar
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, ICS/OT]
related_capec: [CAPEC-1, CAPEC-107, CAPEC-127, CAPEC-17, CAPEC-20, CAPEC-22, CAPEC-237, CAPEC-36, CAPEC-477, CAPEC-480, CAPEC-51, CAPEC-57, CAPEC-59, CAPEC-65, CAPEC-668, CAPEC-74, CAPEC-87]
url: https://cwe.mitre.org/data/definitions/693.html
tags: [mitre-cwe, weakness, CWE-693]
---

# CWE-693 - Protection Mechanism Failure

**Abstraction:** Pillar  -  **Status:** Draft  -  **CWE:** [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

## Description
The product does not use or incorrectly uses a protection mechanism that provides sufficient defense against directed attacks against the product.

## Extended description
This weakness covers three distinct situations. A "missing" protection mechanism occurs when the application does not define any mechanism against a certain class of attack. An "insufficient" protection mechanism might provide some defenses - for example, against the most common attacks - but it does not protect against everything that is intended. Finally, an "ignored" mechanism occurs when a mechanism is available and in active use within the product, but the developer has not applied it in some code path.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-107](https://capec.mitre.org/data/definitions/107.html)
- [CAPEC-127](https://capec.mitre.org/data/definitions/127.html)
- [CAPEC-17](https://capec.mitre.org/data/definitions/17.html)
- [CAPEC-20](https://capec.mitre.org/data/definitions/20.html)
- [CAPEC-22](https://capec.mitre.org/data/definitions/22.html)
- [CAPEC-237](https://capec.mitre.org/data/definitions/237.html)
- [CAPEC-36](https://capec.mitre.org/data/definitions/36.html)
- [CAPEC-477](https://capec.mitre.org/data/definitions/477.html)
- [CAPEC-480](https://capec.mitre.org/data/definitions/480.html)
- [CAPEC-51](https://capec.mitre.org/data/definitions/51.html)
- [CAPEC-57](https://capec.mitre.org/data/definitions/57.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
- [CAPEC-65](https://capec.mitre.org/data/definitions/65.html)
- [CAPEC-668](https://capec.mitre.org/data/definitions/668.html)
- [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)
- [CAPEC-87](https://capec.mitre.org/data/definitions/87.html)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/693.html
