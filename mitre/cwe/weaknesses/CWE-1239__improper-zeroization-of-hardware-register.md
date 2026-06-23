---
cwe_id: CWE-1239
name: Improper Zeroization of Hardware Register
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip]
related_capec: [CAPEC-150, CAPEC-204, CAPEC-37, CAPEC-545]
url: https://cwe.mitre.org/data/definitions/1239.html
tags: [mitre-cwe, weakness, CWE-1239]
---

# CWE-1239 - Improper Zeroization of Hardware Register

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-1239](https://cwe.mitre.org/data/definitions/1239.html)

## Description
The hardware product does not properly clear sensitive information from built-in registers when the user of the hardware block changes.

## Extended description
Hardware logic operates on data stored in registers local to the hardware block. Most hardware IPs, including cryptographic accelerators, rely on registers to buffer I/O, store intermediate values, and interface with software. The result of this is that sensitive information, such as passwords or encryption keys, can exist in locations not transparent to the user of the hardware logic. When a different entity obtains access to the IP due to a change in operating mode or conditions, the new entity can extract information belonging to the previous user if no mechanisms are in place to clear register contents. It is important to clear information stored in the hardware if a physical attack on the product is detected, or if the user of the hardware block changes. The process of clearing register contents in a hardware IP is referred to as zeroization in standards for cryptographic hardware modules such as FIPS-140-2 [REF-267].

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Confidentiality**: Varies by Context

## Potential mitigations
- **Architecture and Design**: Every register potentially containing sensitive information must have a policy specifying how and when information is cleared, in addition to clarifying if it is the responsibility of the hardware logic or IP user to initiate the zeroization procedure at the appropriate time.

## Related attack patterns (CAPEC)
- [CAPEC-150](https://capec.mitre.org/data/definitions/150.html)
- [CAPEC-204](https://capec.mitre.org/data/definitions/204.html)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)

## Related weaknesses
- CWE-226 (ChildOf)
- CWE-226 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1239.html
