---
capec_id: CAPEC-26
name: Leveraging Race Conditions
type: attack-pattern
abstraction: Meta
likelihood: High
severity: High
related_cwe: [CWE-368, CWE-363, CWE-366, CWE-370, CWE-362, CWE-662, CWE-689, CWE-667, CWE-665, CWE-1223, CWE-1254, CWE-1298]
related_attack: []
url: https://capec.mitre.org/data/definitions/26.html
tags: [mitre-capec, attack-pattern, CAPEC-26]
---

# CAPEC-26 - Leveraging Race Conditions

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)

## Description
The adversary targets a race condition occurring when multiple processes access and manipulate the same resource concurrently, and the outcome of the execution depends on the particular order in which the access takes place. The adversary can leverage a race condition by "running the race", modifying the resource and modifying the normal execution flow. For instance, a race condition can occur while accessing a file: the adversary can trick the system by replacing the original file with their version and cause the system to read the malicious file.

## Prerequisites
- A resource is accessed/modified concurrently by multiple processes such that a race condition exists.
- The adversary has the ability to modify the resource.

## Skills required
- **Medium**: Being able to "run the race" requires basic knowledge of concurrent processing including synchonization techniques.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore The adversary explores to gauge what level of access they have. Experiment The adversary gains access to a resource on the target host. The adversary modifies the targeted resource. The resource's value is used to determine the next normal execution action. Exploit The resource is modified/checked concurrently by multiple processes. By using one of the processes, the adversary is able to modify the value just before it is consumed by a different process. A race condition occurs and is exploited by the adversary to abuse the target host.

## Mitigations
- Use safe libraries to access resources such as files.
- Be aware that improper use of access function calls such as chown(), tempfile(), chmod(), etc. can cause a race condition.
- Use synchronization to control the flow of execution.
- Use static analysis tools to find race conditions.
- Pay attention to concurrency problems related to the access of resources.

## Related weaknesses (CWE)
- [CWE-368](https://cwe.mitre.org/data/definitions/368.html)
- [CWE-363](https://cwe.mitre.org/data/definitions/363.html)
- [CWE-366](https://cwe.mitre.org/data/definitions/366.html)
- [CWE-370](https://cwe.mitre.org/data/definitions/370.html)
- [CWE-362](https://cwe.mitre.org/data/definitions/362.html)
- [CWE-662](https://cwe.mitre.org/data/definitions/662.html)
- [CWE-689](https://cwe.mitre.org/data/definitions/689.html)
- [CWE-667](https://cwe.mitre.org/data/definitions/667.html)
- [CWE-665](https://cwe.mitre.org/data/definitions/665.html)
- [CWE-1223](https://cwe.mitre.org/data/definitions/1223.html)
- [CWE-1254](https://cwe.mitre.org/data/definitions/1254.html)
- [CWE-1298](https://cwe.mitre.org/data/definitions/1298.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/26.html
