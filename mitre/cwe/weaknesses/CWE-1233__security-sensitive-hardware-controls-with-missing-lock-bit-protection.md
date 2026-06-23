---
cwe_id: CWE-1233
name: Security-Sensitive Hardware Controls with Missing Lock Bit Protection
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-176, CAPEC-680]
url: https://cwe.mitre.org/data/definitions/1233.html
tags: [mitre-cwe, weakness, CWE-1233]
---

# CWE-1233 - Security-Sensitive Hardware Controls with Missing Lock Bit Protection

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1233](https://cwe.mitre.org/data/definitions/1233.html)

## Description
The product uses a register lock bit protection mechanism, but it does not ensure that the lock bit prevents modification of system registers or controls that perform changes to important hardware system configuration.

## Extended description
Integrated circuits and hardware intellectual properties (IPs) might provide device configuration controls that need to be programmed after device power reset by a trusted firmware or software module, commonly set by BIOS/bootloader. After reset, there can be an expectation that the controls cannot be used to perform any further modification. This behavior is commonly implemented using a trusted lock bit, which can be set to disable writes to a protected set of registers or address regions. The lock protection is intended to prevent modification of certain system configuration (e.g., memory/memory protection unit configuration). However, if the lock bit does not effectively write-protect all system registers or controls that could modify the protected system configuration, then an adversary may be able to use software to access the registers/controls and modify the protected hardware configuration.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Modify Memory

## Potential mitigations
- **Architecture and Design, Implementation, Testing**: Security lock bit protections must be reviewed for design inconsistency and common weaknesses. Security lock programming flow and lock properties must be tested in pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-176](https://capec.mitre.org/data/definitions/176.html)
- [CAPEC-680](https://capec.mitre.org/data/definitions/680.html)

## Related weaknesses
- CWE-284 (ChildOf)
- CWE-667 (ChildOf)

## Observed examples (CVE)
- **CVE-2018-9085**: Certain servers leave a write protection lock bit unset after boot, potentially allowing modification of parts of flash memory.
- **CVE-2014-8273**: Chain: chipset has a race condition (CWE-362) between when an interrupt handler detects an attempt to write-enable the BIOS (in violation of the lock bit), and when the handler resets the write-enable bit back to 0, allowing attackers to issue BIOS writes during the timing window [REF-1237].

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1233.html
