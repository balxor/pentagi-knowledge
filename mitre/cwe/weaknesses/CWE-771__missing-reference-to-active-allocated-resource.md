---
cwe_id: CWE-771
name: Missing Reference to Active Allocated Resource
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/771.html
tags: [mitre-cwe, weakness, CWE-771]
---

# CWE-771 - Missing Reference to Active Allocated Resource

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-771](https://cwe.mitre.org/data/definitions/771.html)

## Description
The product does not properly maintain a reference to a resource that has been allocated, which prevents the resource from being reclaimed.

## Extended description
This does not necessarily apply in languages or frameworks that automatically perform garbage collection, since the removal of all references may act as a signal that the resource is ready to be reclaimed.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (Other)

## Potential mitigations
- **Operation, Architecture and Design**: Use resource-limiting settings provided by the operating system or environment. For example, when managing system resources in POSIX, setrlimit() can be used to set limits for certain types of resources, and getrlimit() can determine how many resources are available. However, these functions are not available on all operating systems. When the current levels get close to the maximum that is defined for the application (see CWE-770), then limit the allocation of further resources to privileged users; alternately, begin releasing resources for less-privileged users. While this mitigation may protect the system from attack, it will not necessarily stop attackers from adversely impacting other users. Ensure that the application performs the appropriate error checks and error handling in case resources become unavailable (CWE-703).

## Related weaknesses
- CWE-400 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/771.html
