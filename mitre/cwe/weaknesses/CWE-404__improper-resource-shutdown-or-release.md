---
cwe_id: CWE-404
name: Improper Resource Shutdown or Release
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-125, CAPEC-130, CAPEC-131, CAPEC-494, CAPEC-495, CAPEC-496, CAPEC-666]
url: https://cwe.mitre.org/data/definitions/404.html
tags: [mitre-cwe, weakness, CWE-404]
---

# CWE-404 - Improper Resource Shutdown or Release

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-404](https://cwe.mitre.org/data/definitions/404.html)

## Description
The product does not release or incorrectly releases a resource before it is made available for re-use.

## Extended description
When a resource is created or allocated, the developer is responsible for properly releasing the resource as well as accounting for all potential paths of expiration or invalidation, such as a set period of time or revocation.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability, Other**: DoS: Resource Consumption (Other), Varies by Context
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Requirements**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, languages such as Java, Ruby, and Lisp perform automatic garbage collection that releases memory for objects that have been deallocated.
- **Implementation**: It is good practice to be responsible for freeing all resources you allocate and to be consistent with how and where you free memory in a function. If you allocate memory that you intend to free upon completion of the function, you must be sure to free the memory at all exit points for that function including error conditions.
- **Implementation**: Memory should be allocated/freed using matching functions such as malloc/free, new/delete, and new[]/delete[].
- **Implementation**: When releasing a complex object or structure, ensure that you properly dispose of all of its member components, not just the object itself.

## Related attack patterns (CAPEC)
- [CAPEC-125](https://capec.mitre.org/data/definitions/125.html)
- [CAPEC-130](https://capec.mitre.org/data/definitions/130.html)
- [CAPEC-131](https://capec.mitre.org/data/definitions/131.html)
- [CAPEC-494](https://capec.mitre.org/data/definitions/494.html)
- [CAPEC-495](https://capec.mitre.org/data/definitions/495.html)
- [CAPEC-496](https://capec.mitre.org/data/definitions/496.html)
- [CAPEC-666](https://capec.mitre.org/data/definitions/666.html)

## Related weaknesses
- CWE-664 (ChildOf)
- CWE-405 (PeerOf)
- CWE-619 (CanPrecede)

## Observed examples (CVE)
- **CVE-1999-1127**: Does not shut down named pipe connections if malformed data is sent.
- **CVE-2001-0830**: Sockets not properly closed when attacker repeatedly connects and disconnects from server.
- **CVE-2002-1372**: Chain: Return values of file/socket operations are not checked (CWE-252), allowing resultant consumption of file descriptors (CWE-772).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/404.html
