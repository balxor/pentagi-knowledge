---
cwe_id: CWE-1245
name: Improper Finite State Machines (FSMs) in Hardware Logic
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip]
related_capec: [CAPEC-74]
url: https://cwe.mitre.org/data/definitions/1245.html
tags: [mitre-cwe, weakness, CWE-1245]
---

# CWE-1245 - Improper Finite State Machines (FSMs) in Hardware Logic

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1245](https://cwe.mitre.org/data/definitions/1245.html)

## Description
Faulty finite state machines (FSMs) in the hardware logic allow an attacker to put the system in an undefined state, to cause a denial of service (DoS) or gain privileges on the victim's system.

## Extended description
The functionality and security of the system heavily depend on the implementation of FSMs. FSMs can be used to indicate the current security state of the system. Lots of secure data operations and data transfers rely on the state reported by the FSM.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Availability, Access Control**: Unexpected State, DoS: Crash, Exit, or Restart, DoS: Instability, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Implementation**: Define all possible states and handle all unused states through default statements. Ensure that system defaults to a secure state.

## Related attack patterns (CAPEC)
- [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)

## Related weaknesses
- CWE-684 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1245.html
