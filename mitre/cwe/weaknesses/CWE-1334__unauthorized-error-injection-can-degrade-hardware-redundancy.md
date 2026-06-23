---
cwe_id: CWE-1334
name: Unauthorized Error Injection Can Degrade Hardware Redundancy
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-624, CAPEC-625]
url: https://cwe.mitre.org/data/definitions/1334.html
tags: [mitre-cwe, weakness, CWE-1334]
---

# CWE-1334 - Unauthorized Error Injection Can Degrade Hardware Redundancy

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1334](https://cwe.mitre.org/data/definitions/1334.html)

## Description
An unauthorized agent can inject errors into a redundant block to deprive the system of redundancy or put the system in a degraded operating mode.

## Extended description
To ensure the performance and functional reliability of certain components, hardware designers can implement hardware blocks for redundancy in the case that others fail. This redundant block can be prevented from performing as intended if the design allows unauthorized agents to inject errors into it. In this way, a path with injected errors may become unavailable to serve as a redundant channel. This may put the system into a degraded mode of operation which could be exploited by a subsequent attack.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Integrity, Availability**: DoS: Crash, Exit, or Restart, DoS: Instability, Quality Degradation, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other), Reduce Performance, Reduce Reliability, Unexpected State

## Potential mitigations
- **Architecture and Design**: Ensure the design does not allow error injection in modes intended for normal run-time operation. Provide access controls on interfaces for injecting errors.
- **Implementation**: Disallow error injection in modes which are expected to be used for normal run-time operation. Provide access controls on interfaces for injecting errors.
- **Integration**: Add an access control layer atop any unprotected interfaces for injecting errors.

## Related attack patterns (CAPEC)
- [CAPEC-624](https://capec.mitre.org/data/definitions/624.html)
- [CAPEC-625](https://capec.mitre.org/data/definitions/625.html)

## Related weaknesses
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1334.html
