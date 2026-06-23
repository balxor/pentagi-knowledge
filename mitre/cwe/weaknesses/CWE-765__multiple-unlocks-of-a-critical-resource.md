---
cwe_id: CWE-765
name: Multiple Unlocks of a Critical Resource
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/765.html
tags: [mitre-cwe, weakness, CWE-765]
---

# CWE-765 - Multiple Unlocks of a Critical Resource

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-765](https://cwe.mitre.org/data/definitions/765.html)

## Description
The product unlocks a critical resource more times than intended, leading to an unexpected state in the system.

## Extended description
When the product is operating in a concurrent environment and repeatedly unlocks a critical resource, the consequences will vary based on the type of lock, the lock's implementation, and the resource being protected. In some situations such as with semaphores, the resources are pooled and extra calls to unlock will increase the count for the number of available resources, likely resulting in a crash or unpredictable behavior when the system nears capacity.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability, Integrity**: DoS: Crash, Exit, or Restart, Modify Memory, Unexpected State

## Potential mitigations
- **Implementation**: When locking and unlocking a resource, try to be sure that all control paths through the code in which the resource is locked one or more times correspond to exactly as many unlocks. If the product acquires a lock and then determines it is not able to perform its intended behavior, be sure to release the lock(s) before waiting for conditions to improve. Reacquire the lock(s) before trying again.

## Related weaknesses
- CWE-667 (ChildOf)
- CWE-675 (ChildOf)

## Observed examples (CVE)
- **CVE-2009-0935**: Attacker provides invalid address to a memory-reading function, causing a mutex to be unlocked twice

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/765.html
