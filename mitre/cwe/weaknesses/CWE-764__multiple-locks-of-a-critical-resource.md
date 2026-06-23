---
cwe_id: CWE-764
name: Multiple Locks of a Critical Resource
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/764.html
tags: [mitre-cwe, weakness, CWE-764]
---

# CWE-764 - Multiple Locks of a Critical Resource

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-764](https://cwe.mitre.org/data/definitions/764.html)

## Description
The product locks a critical resource more times than intended, leading to an unexpected state in the system.

## Extended description
When a product is operating in a concurrent environment and repeatedly locks a critical resource, the consequences will vary based on the type of lock, the lock's implementation, and the resource being protected. In some situations such as with semaphores, the resources are pooled and extra locking calls will reduce the size of the total available pool, possibly leading to degraded performance or a denial of service. If this can be triggered by an attacker, it will be similar to an unrestricted lock (CWE-412). In the context of a binary lock, it is likely that any duplicate locking attempts will never succeed since the lock is already held and progress may not be possible.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability, Integrity**: DoS: Resource Consumption (CPU), DoS: Crash, Exit, or Restart, Unexpected State

## Potential mitigations
- **Implementation**: When locking and unlocking a resource, try to be sure that all control paths through the code in which the resource is locked one or more times correspond to exactly as many unlocks. If the software acquires a lock and then determines it is not able to perform its intended behavior, be sure to release the lock(s) before waiting for conditions to improve. Reacquire the lock(s) before trying again.

## Related weaknesses
- CWE-667 (ChildOf)
- CWE-675 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/764.html
