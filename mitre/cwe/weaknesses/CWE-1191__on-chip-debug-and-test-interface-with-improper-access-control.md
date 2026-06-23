---
cwe_id: CWE-1191
name: On-Chip Debug and Test Interface With Improper Access Control
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-1, CAPEC-180]
url: https://cwe.mitre.org/data/definitions/1191.html
tags: [mitre-cwe, weakness, CWE-1191]
---

# CWE-1191 - On-Chip Debug and Test Interface With Improper Access Control

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1191](https://cwe.mitre.org/data/definitions/1191.html)

## Description
The chip does not implement or does not correctly perform access control to check whether users are authorized to access internal registers and test modes through the physical debug/test interface.

## Extended description
A device's internal information may be accessed through a scan chain of interconnected internal registers, usually through a JTAG interface. The JTAG interface provides access to these registers in a serial fashion in the form of a scan chain for the purposes of debugging programs running on a device. Since almost all information contained within a device may be accessed over this interface, device manufacturers typically insert some form of authentication and authorization to prevent unintended use of this sensitive information. This mechanism is implemented in addition to on-chip protections that are already present. If authorization, authentication, or some other form of access control is not implemented or not implemented correctly, a user may be able to bypass on-chip protection mechanisms through the debug interface. Sometimes, designers choose not to expose the debug pins on the motherboard. Instead, they choose to hide these pins in the intermediate layers of the board. This is primarily done to work around the lack of debug authorization inside the chip. In such a scenario (without debug authorization), when the debug interface is exposed, chip internals are accessible to an attacker.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data
- **Confidentiality**: Read Memory
- **Authorization**: Execute Unauthorized Code or Commands
- **Integrity**: Modify Memory
- **Integrity**: Modify Application Data
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: If feasible, the manufacturer should disable the JTAG interface or implement authentication and authorization for the JTAG interface. If authentication logic is added, it should be resistant to timing attacks. Security-sensitive data stored in registers, such as keys, etc. should be cleared when entering debug mode.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-18827**: chain: JTAG interface is not disabled (CWE-1191) during ROM code execution, introducing a race condition (CWE-362) to extract encryption keys

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1191.html
