---
cwe_id: CWE-1234
name: Hardware Internal or Debug Modes Allow Override of Locks
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-176]
url: https://cwe.mitre.org/data/definitions/1234.html
tags: [mitre-cwe, weakness, CWE-1234]
---

# CWE-1234 - Hardware Internal or Debug Modes Allow Override of Locks

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1234](https://cwe.mitre.org/data/definitions/1234.html)

## Description
System configuration protection may be bypassed during debug mode.

## Extended description
Device configuration controls are commonly programmed after a device power reset by a trusted firmware or software module (e.g., BIOS/bootloader) and then locked from any further modification. This is commonly implemented using a trusted lock bit, which when set, disables writes to a protected set of registers or address regions. The lock protection is intended to prevent modification of certain system configuration (e.g., memory/memory protection unit configuration). If debug features supported by hardware or internal modes/system states are supported in the hardware design, modification of the lock protection may be allowed allowing access and modification of configuration information.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design, Implementation, Testing**: Security Lock bit protections should be reviewed for any bypass/override modes supported. Any supported override modes either should be removed or protected using authenticated debug modes. Security lock programming flow and lock properties should be tested in pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-176](https://capec.mitre.org/data/definitions/176.html)

## Related weaknesses
- CWE-667 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1234.html
