---
cwe_id: CWE-1242
name: Inclusion of Undocumented Features or Chicken Bits
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, ICS/OT]
related_capec: [CAPEC-212, CAPEC-36]
url: https://cwe.mitre.org/data/definitions/1242.html
tags: [mitre-cwe, weakness, CWE-1242]
---

# CWE-1242 - Inclusion of Undocumented Features or Chicken Bits

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1242](https://cwe.mitre.org/data/definitions/1242.html)

## Description
The device includes chicken bits or undocumented features that can create entry points for unauthorized actors.

## Extended description
A common design practice is to use undocumented bits on a device that can be used to disable certain functional security features. These bits are commonly referred to as "chicken bits". They can facilitate quick identification and isolation of faulty components, features that negatively affect performance, or features that do not provide the required controllability for debug and test. Another way to achieve this is through implementation of undocumented features.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Modify Memory, Read Memory, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design, Implementation**: The implementation of chicken bits in a released product is highly discouraged. If implemented at all, ensure that they are disabled in production devices. All interfaces to a device should be documented.

## Related attack patterns (CAPEC)
- [CAPEC-212](https://capec.mitre.org/data/definitions/212.html)
- [CAPEC-36](https://capec.mitre.org/data/definitions/36.html)

## Related weaknesses
- CWE-912 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1242.html
