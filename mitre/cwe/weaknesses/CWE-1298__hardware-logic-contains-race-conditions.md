---
cwe_id: CWE-1298
name: Hardware Logic Contains Race Conditions
type: weakness
abstraction: Base
status: Draft
languages: [Verilog, VHDL, System on Chip]
related_capec: [CAPEC-26]
url: https://cwe.mitre.org/data/definitions/1298.html
tags: [mitre-cwe, weakness, CWE-1298]
---

# CWE-1298 - Hardware Logic Contains Race Conditions

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1298](https://cwe.mitre.org/data/definitions/1298.html)

## Description
A race condition in the hardware logic results in undermining security guarantees of the system.

## Extended description
A race condition in logic circuits typically occurs when a logic gate gets inputs from signals that have traversed different paths while originating from the same source. Such inputs to the gate can change at slightly different times in response to a change in the source signal. This results in a timing error or a glitch (temporary or permanent) that causes the output to change to an unwanted state before settling back to the desired state. If such timing errors occur in access control logic or finite state machines that are implemented in security sensitive flows, an attacker might exploit them to circumvent existing protections.

## Applicable platforms / languages
Verilog, VHDL, System on Chip

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity, Alter Execution Logic

## Potential mitigations
- **Architecture and Design**: Adopting design practices that encourage designers to recognize and eliminate race conditions, such as Karnaugh maps, could result in the decrease in occurrences of race conditions.
- **Implementation**: Logic redundancy can be implemented along security critical paths to prevent race conditions. To avoid metastability, it is a good practice in general to default to a secure state in which access is not given to untrusted agents.

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)

## Related weaknesses
- CWE-362 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1298.html
