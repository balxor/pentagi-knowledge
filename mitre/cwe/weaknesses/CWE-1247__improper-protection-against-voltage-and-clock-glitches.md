---
cwe_id: CWE-1247
name: Improper Protection Against Voltage and Clock Glitches
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, ICS/OT, System on Chip, Power Management Hardware, Clock/Counter Hardware, Sensor Hardware]
related_capec: [CAPEC-624, CAPEC-625]
url: https://cwe.mitre.org/data/definitions/1247.html
tags: [mitre-cwe, weakness, CWE-1247]
---

# CWE-1247 - Improper Protection Against Voltage and Clock Glitches

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1247](https://cwe.mitre.org/data/definitions/1247.html)

## Description
The device does not contain or contains incorrectly implemented circuitry or sensors to detect and mitigate voltage and clock glitches and protect sensitive information or software contained on the device.

## Extended description
A device might support features such as secure boot which are supplemented with hardware and firmware support. This involves establishing a chain of trust, starting with an immutable root of trust by checking the signature of the next stage (culminating with the OS and runtime software) against a golden value before transferring control. The intermediate stages typically set up the system in a secure state by configuring several access control settings. Similarly, security logic for exercising a debug or testing interface may be implemented in hardware, firmware, or both. A device needs to guard against fault attacks such as voltage glitches and clock glitches that an attacker may employ in an attempt to compromise the system.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, ICS/OT, System on Chip, Power Management Hardware, Clock/Counter Hardware, Sensor Hardware

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Memory, Modify Memory, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design, Implementation**: At the circuit-level, using Tunable Replica Circuits (TRCs) or special flip-flops such as Razor flip-flops helps mitigate glitch attacks. Working at the SoC or platform base, level sensors may be implemented to detect glitches. Implementing redundancy in security-sensitive code (e.g., where checks are performed)also can help with mitigation of glitch attacks.

## Related attack patterns (CAPEC)
- [CAPEC-624](https://capec.mitre.org/data/definitions/624.html)
- [CAPEC-625](https://capec.mitre.org/data/definitions/625.html)

## Related weaknesses
- CWE-1384 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-17391**: Lack of anti-glitch protections allows an attacker to launch a physical attack to bypass the secure boot and read protected eFuses.
- **CVE-2021-33478**: IP communication firmware allows access to a boot shell via certain impulses

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1247.html
