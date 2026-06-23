---
cwe_id: CWE-1223
name: Race Condition for Write-Once Attributes
type: weakness
abstraction: Base
status: Incomplete
languages: [Verilog, VHDL, System on Chip]
related_capec: [CAPEC-26]
url: https://cwe.mitre.org/data/definitions/1223.html
tags: [mitre-cwe, weakness, CWE-1223]
---

# CWE-1223 - Race Condition for Write-Once Attributes

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1223](https://cwe.mitre.org/data/definitions/1223.html)

## Description
A write-once register in hardware design is programmable by an untrusted software component earlier than the trusted software component, resulting in a race condition issue.

## Extended description
Integrated circuits and hardware IP software programmable controls and settings are commonly stored in register circuits. These register contents have to be initialized at hardware reset to defined default values that are hard coded in the hardware description language (HDL) code of the hardware unit. A common security protection method used to protect register settings from modification by software is to make them write-once. This means the hardware implementation only allows writing to such registers once, and they become read-only after having been written once by software. This is useful to allow initial boot software to configure systems settings to secure values while blocking runtime software from modifying such hardware settings. Implementation issues in hardware design of such controls can expose such registers to a race condition security flaw. For example, consider a hardware design that has two different software/firmware modules executing in parallel. One module is trusted (module A) and another is untrusted (module B). In this design it could be possible for Module B to send write cycles to the write-once register before Module A. Since the field is write-once the programmed value from Module A will be ignored and the pre-empted value programmed by Module B will be used by hardware.

## Applicable platforms / languages
Verilog, VHDL, System on Chip

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: During hardware design, all register write-once or sticky fields must be evaluated for proper configuration.

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)

## Related weaknesses
- CWE-362 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1223.html
