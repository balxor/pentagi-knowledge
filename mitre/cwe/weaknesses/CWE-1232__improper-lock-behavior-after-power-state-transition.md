---
cwe_id: CWE-1232
name: Improper Lock Behavior After Power State Transition
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-166]
url: https://cwe.mitre.org/data/definitions/1232.html
tags: [mitre-cwe, weakness, CWE-1232]
---

# CWE-1232 - Improper Lock Behavior After Power State Transition

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1232](https://cwe.mitre.org/data/definitions/1232.html)

## Description
Register lock bit protection disables changes to system configuration once the bit is set. Some of the protected registers or lock bits become programmable after power state transitions (e.g., Entry and wake from low power sleep modes) causing the system configuration to be changeable.

## Extended description
Devices may allow device configuration controls which need to be programmed after device power reset via a trusted firmware or software module (commonly set by BIOS/bootloader) and then locked from any further modification. This action is commonly implemented using a programmable lock bit, which, when set, disables writes to a protected set of registers or address regions. After a power state transition, the lock bit is set to unlocked. Some common weaknesses that can exist in such a protection scheme are that the lock gets cleared, the values of the protected registers get reset, or the lock become programmable.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Modify Memory

## Potential mitigations
- **Architecture and Design, Implementation, Testing**: Security Lock bit protections should be reviewed for behavior across supported power state transitions. Security lock programming flow and lock properties should be tested in pre-silicon and post-silicon testing including testing across power transitions.

## Related attack patterns (CAPEC)
- [CAPEC-166](https://capec.mitre.org/data/definitions/166.html)

## Related weaknesses
- CWE-667 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1232.html
