---
cwe_id: CWE-1222
name: Insufficient Granularity of Address Regions Protected by Register Locks
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip]
related_capec: [CAPEC-679]
url: https://cwe.mitre.org/data/definitions/1222.html
tags: [mitre-cwe, weakness, CWE-1222]
---

# CWE-1222 - Insufficient Granularity of Address Regions Protected by Register Locks

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1222](https://cwe.mitre.org/data/definitions/1222.html)

## Description
The product defines a large address region protected from modification by the same register lock control bit. This results in a conflict between the functional requirement that some addresses need to be writable by software during operation and the security requirement that the system configuration lock bit must be set during the boot process.

## Extended description
Integrated circuits and hardware IPs can expose the device configuration controls that need to be programmed after device power reset by a trusted firmware or software module (commonly set by BIOS/bootloader) and then locked from any further modification. In hardware design, this is commonly implemented using a programmable lock bit which enables/disables writing to a protected set of registers or address regions. When the programmable lock bit is set, the relevant address region can be implemented as a hardcoded value in hardware logic that cannot be changed later. A problem can arise wherein the protected region definition is not granular enough. After the programmable lock bit has been set, then this new functionality cannot be implemented without change to the hardware design.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Access Control**: Other

## Potential mitigations
- **Architecture and Design**: The defining of protected locked registers should be reviewed or tested early in the design phase with software teams to ensure software flows are not blocked by the security locks. As an alternative to using register lock control bits and fixed access control regions, the hardware design could use programmable security access control configuration so that device trusted firmware can configure and change the protected regions based on software usage and security models.

## Related attack patterns (CAPEC)
- [CAPEC-679](https://capec.mitre.org/data/definitions/679.html)

## Related weaknesses
- CWE-1220 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1222.html
