---
cwe_id: CWE-1231
name: Improper Prevention of Lock Bit Modification
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-680]
url: https://cwe.mitre.org/data/definitions/1231.html
tags: [mitre-cwe, weakness, CWE-1231]
---

# CWE-1231 - Improper Prevention of Lock Bit Modification

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1231](https://cwe.mitre.org/data/definitions/1231.html)

## Description
The product uses a trusted lock bit for restricting access to registers, address regions, or other resources, but the product does not prevent the value of the lock bit from being modified after it has been set.

## Extended description
In integrated circuits and hardware intellectual property (IP) cores, device configuration controls are commonly programmed after a device power reset by a trusted firmware or software module (e.g., BIOS/bootloader) and then locked from any further modification. This behavior is commonly implemented using a trusted lock bit. When set, the lock bit disables writes to a protected set of registers or address regions. Design or coding errors in the implementation of the lock bit protection feature may allow the lock bit to be modified or cleared by software after it has been set. Attackers might be able to unlock the system and features that the bit is intended to protect.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Modify Memory

## Potential mitigations
- **Architecture and Design, Implementation, Testing**: Security lock bit protections must be reviewed for design inconsistency and common weaknesses. Security lock programming flow and lock properties must be tested in pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-680](https://capec.mitre.org/data/definitions/680.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2017-6283**: chip reset clears critical read/write lock permissions for RSA function

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1231.html
