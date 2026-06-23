---
capec_id: CAPEC-38
name: Leveraging/Manipulating Configuration File Search Paths
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-426, CWE-427]
related_attack: [T1574.007, T1574.009]
url: https://capec.mitre.org/data/definitions/38.html
tags: [mitre-capec, attack-pattern, CAPEC-38]
---

# CAPEC-38 - Leveraging/Manipulating Configuration File Search Paths

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-38](https://capec.mitre.org/data/definitions/38.html)

## Description
This pattern of attack sees an adversary load a malicious resource into a program's standard path so that when a known command is executed then the system instead executes the malicious component. The adversary can either modify the search path a program uses, like a PATH variable or classpath, or they can manipulate resources on the path to point to their malicious components. J2EE applications and other component based applications that are built from multiple binaries can have very long list of dependencies to execute. If one of these libraries and/or references is controllable by the attacker then application controls can be circumvented by the attacker.

## Prerequisites
- The attacker must be able to write to redirect search paths on the victim host.

## Skills required
- **Low**: To identify and execute against an over-privileged system interface

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Mitigations
- Design: Enforce principle of least privilege
- Design: Ensure that the program's compound parts, including all system dependencies, classpath, path, and so on, are secured to the same or higher level assurance as the program
- Implementation: Host integrity monitoring

## Related weaknesses (CWE)
- [CWE-426](https://cwe.mitre.org/data/definitions/426.html)
- [CWE-427](https://cwe.mitre.org/data/definitions/427.html)

## Related ATT&CK techniques
- T1574.007
- T1574.009

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/38.html
