---
cwe_id: CWE-1224
name: Improper Restriction of Write-Once Bit Fields
type: weakness
abstraction: Base
status: Incomplete
languages: [Verilog, VHDL, System on Chip]
related_capec: [CAPEC-680]
url: https://cwe.mitre.org/data/definitions/1224.html
tags: [mitre-cwe, weakness, CWE-1224]
---

# CWE-1224 - Improper Restriction of Write-Once Bit Fields

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1224](https://cwe.mitre.org/data/definitions/1224.html)

## Description
The hardware design control register "sticky bits" or write-once bit fields are improperly implemented, such that they can be reprogrammed by software.

## Extended description
Integrated circuits and hardware IP software programmable controls and settings are commonly stored in register circuits. These register contents have to be initialized at hardware reset to define default values that are hard coded in the hardware description language (HDL) code of the hardware unit. A common security protection method used to protect register settings from modification by software is to make the settings write-once or "sticky." This allows writing to such registers only once, whereupon they become read-only. This is useful to allow initial boot software to configure systems settings to secure values while blocking runtime software from modifying such hardware settings. Failure to implement write-once restrictions in hardware design can expose such registers to being re-programmed by software and written multiple times. For example, write-once fields could be implemented to only be write-protected if they have been set to value "1", wherein they would work as "write-1-once" and not "write-once".

## Applicable platforms / languages
Verilog, VHDL, System on Chip

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Varies by Context

## Potential mitigations
- **Architecture and Design**: During hardware design, all register write-once or sticky fields must be evaluated for proper configuration.

## Related attack patterns (CAPEC)
- [CAPEC-680](https://capec.mitre.org/data/definitions/680.html)

## Related weaknesses
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1224.html
