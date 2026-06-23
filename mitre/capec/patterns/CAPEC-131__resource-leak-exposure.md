---
capec_id: CAPEC-131
name: Resource Leak Exposure
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: Medium
related_cwe: [CWE-404]
related_attack: [T1499]
url: https://capec.mitre.org/data/definitions/131.html
tags: [mitre-capec, attack-pattern, CAPEC-131]
---

# CAPEC-131 - Resource Leak Exposure

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-131](https://capec.mitre.org/data/definitions/131.html)

## Description
An adversary utilizes a resource leak on the target to deplete the quantity of the resource available to service legitimate requests.

## Extended description
Resource leaks most often come in the form of memory leaks where memory is allocated but never released after it has served its purpose, however, theoretically, any other resource that can be reserved can be targeted if the target fails to release the reservation when the reserved resource block is no longer needed. In this attack, the adversary determines what activity results in leaked resources and then triggers that activity on the target. Since some leaks may be small, this may require a large number of requests by the adversary. However, this attack differs from a flooding attack in that the rate of requests is generally not significant. This is because the lost resources due to the leak accumulate until the target is reset, usually by restarting it. Thus, a resource-poor adversary who would be unable to flood the target can still utilize this attack. Resource depletion through leak differs from resource depletion through allocation in that, in the former, the adversary may not be able to control the size of each leaked allocation, but instead allows the leak to accumulate until it is large enough to affect the target's performance. When depleting resources through allocation, the allocated resource may eventually be released by the target so the attack relies on making sure that the allocation size itself is prohibitive of normal operations by the target.

## Prerequisites
- The target must have a resource leak that the adversary can repeatedly trigger.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Availability**: Unreliable Execution (A successful resource leak exposure attack compromises the availability of the target system's services.), Resource Consumption (A successful resource leak exposure attack compromises the availability of the target system's services.)

## Mitigations
- If possible, leverage coding language(s) that do not allow this weakness to occur (e.g., Java, Ruby, and Python all perform automatic garbage collection that releases memory for objects that have been deallocated).
- Memory should always be allocated/freed using matching functions (e.g., malloc/free, new/delete, etc.)
- Implement best practices with respect to memory management, including the freeing of all allocated resources at all exit points and ensuring consistency with how and where memory is freed in a function.

## Related weaknesses (CWE)
- [CWE-404](https://cwe.mitre.org/data/definitions/404.html)

## Related ATT&CK techniques
- T1499

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/131.html
