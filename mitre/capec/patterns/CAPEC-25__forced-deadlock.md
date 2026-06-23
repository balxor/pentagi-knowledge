---
capec_id: CAPEC-25
name: Forced Deadlock
type: attack-pattern
abstraction: Meta
likelihood: Low
severity: High
related_cwe: [CWE-412, CWE-567, CWE-662, CWE-667, CWE-833, CWE-1322]
related_attack: [T1499.004]
url: https://capec.mitre.org/data/definitions/25.html
tags: [mitre-capec, attack-pattern, CAPEC-25]
---

# CAPEC-25 - Forced Deadlock

**Abstraction:** Meta  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-25](https://capec.mitre.org/data/definitions/25.html)

## Description
The adversary triggers and exploits a deadlock condition in the target software to cause a denial of service. A deadlock can occur when two or more competing actions are waiting for each other to finish, and thus neither ever does. Deadlock conditions can be difficult to detect.

## Prerequisites
- The target host has a deadlock condition. There are four conditions for a deadlock to occur, known as the Coffman conditions. [REF-101]
- The target host exposes an API to the user.

## Skills required
- **Medium**: This type of attack may be sophisticated and require knowledge about the system's resources and APIs.

## Consequences
- **Availability**: Resource Consumption (A successful forced deadlock attack compromises the availability of the system by exhausting its available resources.)

## Execution flow
Execution Flow Explore The adversary initiates an exploratory phase to get familiar with the system. The adversary triggers a first action (such as holding a resource) and initiates a second action which will wait for the first one to finish. If the target program has a deadlock condition, the program waits indefinitely resulting in a denial of service.

## Mitigations
- Use known algorithm to avoid deadlock condition (for instance non-blocking synchronization algorithms).
- For competing actions, use well-known libraries which implement synchronization.

## Related weaknesses (CWE)
- [CWE-412](https://cwe.mitre.org/data/definitions/412.html)
- [CWE-567](https://cwe.mitre.org/data/definitions/567.html)
- [CWE-662](https://cwe.mitre.org/data/definitions/662.html)
- [CWE-667](https://cwe.mitre.org/data/definitions/667.html)
- [CWE-833](https://cwe.mitre.org/data/definitions/833.html)
- [CWE-1322](https://cwe.mitre.org/data/definitions/1322.html)

## Related ATT&CK techniques
- T1499.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/25.html
