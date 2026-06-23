---
cwe_id: CWE-773
name: Missing Reference to Active File Descriptor or Handle
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/773.html
tags: [mitre-cwe, weakness, CWE-773]
---

# CWE-773 - Missing Reference to Active File Descriptor or Handle

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-773](https://cwe.mitre.org/data/definitions/773.html)

## Description
The product does not properly maintain references to a file descriptor or handle, which prevents that file descriptor/handle from being reclaimed.

## Extended description
This can cause the product to consume all available file descriptors or handles, which can prevent other processes from performing critical file processing operations.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (Other)

## Potential mitigations
- **Operation, Architecture and Design**: Use resource-limiting settings provided by the operating system or environment. For example, when managing system resources in POSIX, setrlimit() can be used to set limits for certain types of resources, and getrlimit() can determine how many resources are available. However, these functions are not available on all operating systems. When the current levels get close to the maximum that is defined for the application (see CWE-770), then limit the allocation of further resources to privileged users; alternately, begin releasing resources for less-privileged users. While this mitigation may protect the system from attack, it will not necessarily stop attackers from adversely impacting other users. Ensure that the application performs the appropriate error checks and error handling in case resources become unavailable (CWE-703).

## Related weaknesses
- CWE-771 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/773.html
