---
cwe_id: CWE-1250
name: Improper Preservation of Consistency Between Independent Representations of Shared State
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Cloud Computing, Security Hardware]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1250.html
tags: [mitre-cwe, weakness, CWE-1250]
---

# CWE-1250 - Improper Preservation of Consistency Between Independent Representations of Shared State

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1250](https://cwe.mitre.org/data/definitions/1250.html)

## Description
The product has or supports multiple distributed components or sub-systems that are each required to keep their own local copy of shared data - such as state or cache - but the product does not ensure that all local copies remain consistent with each other.

## Extended description
In highly distributed environments, or on systems with distinct physical components that operate independently, there is often a need for each component to store and update its own local copy of key data such as state or cache, so that all components have the same "view" of the overall system and operate in a coordinated fashion. For example, users of a social media service or a massively multiplayer online game might be using their own personal computers while also interacting with different physical hosts in a globally distributed service, but all participants must be able to have the same "view" of the world. Alternately, a processor's Memory Management Unit (MMU) might have "shadow" MMUs to distribute its workload, and all shadow MMUs are expected to have the same accessible ranges of memory. In such environments, it becomes critical for the product to ensure that this "shared state" is consistently modified across all distributed systems. If state is not consistently maintained across all systems, then critical transactions might take place out of order, or some users might not get the same data as other users. When this inconsistency affects correctness of operations, it can introduce vulnerabilities in mechanisms that depend on consistent state.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Cloud Computing, Security Hardware

## Common consequences
- **Other**: Unexpected State

## Related weaknesses
- CWE-664 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1250.html
