---
capec_id: CAPEC-29
name: Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-367, CWE-368, CWE-366, CWE-370, CWE-362, CWE-662, CWE-691, CWE-663, CWE-665]
related_attack: []
url: https://capec.mitre.org/data/definitions/29.html
tags: [mitre-capec, attack-pattern, CAPEC-29]
---

# CAPEC-29 - Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Description
This attack targets a race condition occurring between the time of check (state) for a resource and the time of use of a resource. A typical example is file access. The adversary can leverage a file access race condition by "running the race", meaning that they would modify the resource between the first time the target program accesses the file and the time the target program uses the file. During that period of time, the adversary could replace or modify the file, causing the application to behave unexpectedly.

## Prerequisites
- A resource is access/modified concurrently by multiple processes.
- The adversary is able to modify resource.
- A race condition exists while accessing a resource.

## Skills required
- **Medium**: This attack can get sophisticated since the attack has to occur within a short interval of time.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Alter Execution Logic, Resource Consumption (Denial of Service)
- **Confidentiality**: Gain Privileges, Alter Execution Logic, Read Data
- **Integrity**: Modify Data, Alter Execution Logic

## Execution flow
Execution Flow Explore The adversary explores to gauge what level of access they have. Experiment The adversary confirms access to a resource on the target host. The adversary confirms ability to modify the targeted resource. Exploit The adversary decides to leverage the race condition by "running the race", meaning that they would modify the resource between the first time the target program accesses the file and the time the target program uses the file. During that period of time, the adversary can replace the resource and cause an escalation of privilege.

## Mitigations
- Use safe libraries to access resources such as files.
- Be aware that improper use of access function calls such as chown(), tempfile(), chmod(), etc. can cause a race condition.
- Use synchronization to control the flow of execution.
- Use static analysis tools to find race conditions.
- Pay attention to concurrency problems related to the access of resources.

## Related weaknesses (CWE)
- [CWE-367](https://cwe.mitre.org/data/definitions/367.html)
- [CWE-368](https://cwe.mitre.org/data/definitions/368.html)
- [CWE-366](https://cwe.mitre.org/data/definitions/366.html)
- [CWE-370](https://cwe.mitre.org/data/definitions/370.html)
- [CWE-362](https://cwe.mitre.org/data/definitions/362.html)
- [CWE-662](https://cwe.mitre.org/data/definitions/662.html)
- [CWE-691](https://cwe.mitre.org/data/definitions/691.html)
- [CWE-663](https://cwe.mitre.org/data/definitions/663.html)
- [CWE-665](https://cwe.mitre.org/data/definitions/665.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/29.html
