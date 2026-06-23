---
cwe_id: CWE-1303
name: Non-Transparent Sharing of Microarchitectural Resources
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-663]
url: https://cwe.mitre.org/data/definitions/1303.html
tags: [mitre-cwe, weakness, CWE-1303]
---

# CWE-1303 - Non-Transparent Sharing of Microarchitectural Resources

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1303](https://cwe.mitre.org/data/definitions/1303.html)

## Description
Hardware structures shared across execution contexts (e.g., caches and branch predictors) can violate the expected architecture isolation between contexts.

## Extended description
Modern processors use techniques such as out-of-order execution, speculation, prefetching, data forwarding, and caching to increase performance. Details about the implementation of these techniques are hidden from the programmer's view. This is problematic when the hardware implementation of these techniques results in resources being shared across supposedly isolated contexts. Contention for shared resources between different contexts opens covert channels that allow malicious programs executing in one context to recover information from another context. Some examples of shared micro-architectural resources that have been used to leak information between contexts are caches, branch prediction logic, and load or store buffers. Speculative and out-of-order execution provides an attacker with increased control over which data is leaked through the covert channel. If the extent of resource sharing between contexts in the design microarchitecture is undocumented, it is extremely difficult to ensure system assets are protected against disclosure.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data, Read Memory

## Potential mitigations
- **Architecture and Design**: Microarchitectural covert channels can be addressed using a mixture of hardware and software mitigation techniques. These include partitioned caches, new barrier and flush instructions, and disabling high resolution performance counters and timers.
- **Requirements**: Microarchitectural covert channels can be addressed using a mixture of hardware and software mitigation techniques. These include partitioned caches, new barrier and flush instructions, and disabling high resolution performance counters and timers.

## Related attack patterns (CAPEC)
- [CAPEC-663](https://capec.mitre.org/data/definitions/663.html)

## Related weaknesses
- CWE-1189 (ChildOf)
- CWE-203 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1303.html
