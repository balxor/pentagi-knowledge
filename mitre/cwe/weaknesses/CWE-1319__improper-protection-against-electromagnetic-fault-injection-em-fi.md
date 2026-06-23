---
cwe_id: CWE-1319
name: Improper Protection against Electromagnetic Fault Injection (EM-FI)
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip, Microcontroller Hardware, Memory Hardware, Power Management Hardware, Processor Hardware, Test/Debug Hardware, Sensor Hardware]
related_capec: [CAPEC-624, CAPEC-625]
url: https://cwe.mitre.org/data/definitions/1319.html
tags: [mitre-cwe, weakness, CWE-1319]
---

# CWE-1319 - Improper Protection against Electromagnetic Fault Injection (EM-FI)

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1319](https://cwe.mitre.org/data/definitions/1319.html)

## Description
The device is susceptible to electromagnetic fault injection attacks, causing device internal information to be compromised or security mechanisms to be bypassed.

## Extended description
Electromagnetic fault injection may allow an attacker to locally and dynamically modify the signals (both internal and external) of an integrated circuit. EM-FI attacks consist of producing a local, transient magnetic field near the device, inducing current in the device wires. A typical EMFI setup is made up of a pulse injection circuit that generates a high current transient in an EMI coil, producing an abrupt magnetic pulse which couples to the target producing faults in the device, which can lead to: Bypassing security mechanisms such as secure JTAG or Secure Boot Leaking device information Modifying program flow Perturbing secure hardware modules (e.g. random number generators)

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip, Microcontroller Hardware, Memory Hardware, Power Management Hardware, Processor Hardware, Test/Debug Hardware, Sensor Hardware

## Common consequences
- **Confidentiality, Integrity, Access Control, Availability**: Modify Memory, Read Memory, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design, Implementation**: 1. Redundancy - By replicating critical operations and comparing the two outputs can help indicate whether a fault has been injected. 2. Error detection and correction codes - Gay, Mael, et al. proposed a new scheme that not only detects faults injected by a malicious adversary but also automatically corrects single nibble/byte errors introduced by low-multiplicity faults. 3. Fail by default coding - When checking conditions (switch or if) check all possible cases and fail by default because the default case in a switch (or the else part of a cascaded if-else-if construct) is used for dealing with the last possible (and valid) value without checking. This is prone to fault injection because this alternative is easily selected as a result of potential data manipulation [REF-1141]. 4. Random Behavior - adding random delays before critical operations, so that timing is not predictable. 5. Program Flow Integrity Protection - The program flow can be secured by integrating run-time checking aiming at detecting control flow inconsistencies. One such example is tagging the source code to indicate the points not to be bypassed [REF-1147]. 6. Sensors - Usage of sensors can detect variations in voltage and current. 7. Shields - physical barriers to protect the chips from malicious manipulation.

## Related attack patterns (CAPEC)
- [CAPEC-624](https://capec.mitre.org/data/definitions/624.html)
- [CAPEC-625](https://capec.mitre.org/data/definitions/625.html)

## Related weaknesses
- CWE-693 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-27211**: Chain: microcontroller system-on-chip uses a register value stored in flash to set product protection state on the memory bus and does not contain protection against fault injection (CWE-1319) which leads to an incorrect initialization of the memory bus (CWE-1419) leading the product to be in an unprotected state.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1319.html
