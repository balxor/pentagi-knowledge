---
capec_id: CAPEC-480
name: Escaping Virtualization
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Very High
related_cwe: [CWE-693]
related_attack: [T1611]
url: https://capec.mitre.org/data/definitions/480.html
tags: [mitre-capec, attack-pattern, CAPEC-480]
---

# CAPEC-480 - Escaping Virtualization

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-480](https://capec.mitre.org/data/definitions/480.html)

## Description
An adversary gains access to an application, service, or device with the privileges of an authorized or privileged user by escaping the confines of a virtualized environment. The adversary is then able to access resources or execute unauthorized code within the host environment, generally with the privileges of the user running the virtualized process. Successfully executing an attack of this type is often the first step in executing more complex attacks.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Bypass Protection Mechanism, Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Probing: The adversary probes the target application, service, or device to find a possible weakness that would allow escaping the virtualized environment. Techniques Probing applications, services, or devices for virtualization weaknesses. Experiment Verify the exploitable security weaknesses: Using the found weakness, the adversary attempts to escape the virtualized environment. Techniques Using an application weakness to escape a virtualized environment Exploit Execute more complex attacks: Once outside of the virtualized environment, the adversary attempts to perform other more complex attacks such as accessing system resources or executing unauthorized code within the host environment. Techniques Executing complex attacks when given higher permissions by escaping a virtualized environment

## Mitigations
- Ensure virtualization software is current and up-to-date.
- Abide by the least privilege principle to avoid assigning users more privileges than necessary.

## Related weaknesses (CWE)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

## Related ATT&CK techniques
- T1611

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/480.html
