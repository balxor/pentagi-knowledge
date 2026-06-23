---
cwe_id: CWE-385
name: Covert Timing Channel
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-462]
url: https://cwe.mitre.org/data/definitions/385.html
tags: [mitre-cwe, weakness, CWE-385]
---

# CWE-385 - Covert Timing Channel

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-385](https://cwe.mitre.org/data/definitions/385.html)

## Description
Covert timing channels convey information by modulating some aspect of system behavior over time, so that the program receiving the information can observe system behavior and infer protected information.

## Extended description
In some instances, knowing when data is transmitted between parties can provide a malicious user with privileged information. Also, externally monitoring the timing of operations can potentially reveal sensitive data. For example, a cryptographic operation can expose its internal state if the time it takes to perform the operation varies, based on the state. Covert channels are frequently classified as either storage or timing channels. Some examples of covert timing channels are the system's paging rate, the time a certain transaction requires to execute, and the time it takes to gain access to a shared bus.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Other**: Read Application Data, Other

## Potential mitigations
- **Architecture and Design**: Whenever possible, specify implementation strategies that do not introduce time variances in operations.
- **Implementation**: Often one can artificially manipulate the time which operations take or -- when operations occur -- can remove information from the attacker.
- **Implementation**: It is reasonable to add artificial or random delays so that the amount of CPU time consumed is independent of the action being taken by the application.

## Related attack patterns (CAPEC)
- [CAPEC-462](https://capec.mitre.org/data/definitions/462.html)

## Related weaknesses
- CWE-514 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/385.html
