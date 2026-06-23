---
capec_id: CAPEC-96
name: Block Access to Libraries
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Medium
related_cwe: [CWE-589]
related_attack: []
url: https://capec.mitre.org/data/definitions/96.html
tags: [mitre-capec, attack-pattern, CAPEC-96]
---

# CAPEC-96 - Block Access to Libraries

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-96](https://capec.mitre.org/data/definitions/96.html)

## Description
An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. It is possible that the application does not handle situations properly where access to these libraries has been blocked. Depending on the error handling within the application, blocked access to libraries may leave the system in an insecure state that could be leveraged by an attacker.

## Prerequisites
- An application requires access to external libraries.
- An attacker has the privileges to block application access to external libraries.

## Skills required
- **Low**: Knowledge of how to block access to libraries, as well as knowledge of how to leverage the resulting state of the application based on the failed call.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Bypass Protection Mechanism
- **Availability**: Alter Execution Logic
- **Confidentiality**: Other, Bypass Protection Mechanism

## Execution flow
Execution Flow Explore Determine what external libraries the application accesses. Experiment Block access to the external libraries accessed by the application. Monitor the behavior of the system to see if it goes into an insecure/inconsistent state. If the system does go into an insecure/inconsistent state, leverage that to obtain information about the system functionality or data, elevate access control, etc. The rest of this attack will depend on the context and the desired goal.

## Mitigations
- Ensure that application handles situations where access to APIs in external libraries is not available securely. If the application cannot continue its execution safely it should fail in a consistent and secure fashion.

## Related weaknesses (CWE)
- [CWE-589](https://cwe.mitre.org/data/definitions/589.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/96.html
