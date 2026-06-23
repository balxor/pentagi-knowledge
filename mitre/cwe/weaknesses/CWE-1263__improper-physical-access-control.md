---
cwe_id: CWE-1263
name: Improper Physical Access Control
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-401]
url: https://cwe.mitre.org/data/definitions/1263.html
tags: [mitre-cwe, weakness, CWE-1263]
---

# CWE-1263 - Improper Physical Access Control

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1263](https://cwe.mitre.org/data/definitions/1263.html)

## Description
The product is designed with access restricted to certain information, but it does not sufficiently protect against an unauthorized actor with physical access to these areas.

## Extended description
Sections of a product intended to have restricted access may be inadvertently or intentionally rendered accessible when the implemented physical protections are insufficient. The specific requirements around how robust the design of the physical protection mechanism needs to be depends on the type of product being protected. Selecting the correct physical protection mechanism and properly enforcing it through implementation and manufacturing are critical to the overall physical security of the product.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control**: Varies by Context

## Potential mitigations
- **Architecture and Design**: Specific protection requirements depend strongly on contextual factors including the level of acceptable risk associated with compromise to the product's protection mechanism. Designers could incorporate anti-tampering measures that protect against or detect when the product has been tampered with.
- **Testing**: The testing phase of the lifecycle should establish a method for determining whether the protection mechanism is sufficient to prevent unauthorized access.
- **Manufacturing**: Ensure that all protection mechanisms are fully activated at the time of manufacturing and distribution.

## Related attack patterns (CAPEC)
- [CAPEC-401](https://capec.mitre.org/data/definitions/401.html)

## Related weaknesses
- CWE-284 (ChildOf)
- CWE-1191 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1263.html
