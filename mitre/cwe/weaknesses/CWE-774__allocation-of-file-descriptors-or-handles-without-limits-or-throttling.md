---
cwe_id: CWE-774
name: Allocation of File Descriptors or Handles Without Limits or Throttling
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/774.html
tags: [mitre-cwe, weakness, CWE-774]
---

# CWE-774 - Allocation of File Descriptors or Handles Without Limits or Throttling

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-774](https://cwe.mitre.org/data/definitions/774.html)

## Description
The product allocates file descriptors or handles on behalf of an actor without imposing any restrictions on how many descriptors can be allocated, in violation of the intended security policy for that actor.

## Extended description
This can cause the product to consume all available file descriptors or handles, which can prevent other processes from performing critical file processing operations.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (Other)

## Potential mitigations
- **Operation, Architecture and Design**: Use resource-limiting settings provided by the operating system or environment. For example, when managing system resources in POSIX, setrlimit() can be used to set limits for certain types of resources, and getrlimit() can determine how many resources are available. However, these functions are not available on all operating systems. When the current levels get close to the maximum that is defined for the application (see CWE-770), then limit the allocation of further resources to privileged users; alternately, begin releasing resources for less-privileged users. While this mitigation may protect the system from attack, it will not necessarily stop attackers from adversely impacting other users. Ensure that the application performs the appropriate error checks and error handling in case resources become unavailable (CWE-703).

## Related weaknesses
- CWE-770 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/774.html
