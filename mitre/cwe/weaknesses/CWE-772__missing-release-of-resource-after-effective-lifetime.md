---
cwe_id: CWE-772
name: Missing Release of Resource after Effective Lifetime
type: weakness
abstraction: Base
status: Draft
languages: [Mobile]
related_capec: [CAPEC-469]
url: https://cwe.mitre.org/data/definitions/772.html
tags: [mitre-cwe, weakness, CWE-772]
---

# CWE-772 - Missing Release of Resource after Effective Lifetime

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-772](https://cwe.mitre.org/data/definitions/772.html)

## Description
The product does not release a resource after its effective lifetime has ended, i.e., after the resource is no longer needed.

## Applicable platforms / languages
Mobile

## Common consequences
- **Availability**: DoS: Resource Consumption (Other), DoS: Resource Consumption (Memory), DoS: Resource Consumption (CPU)

## Potential mitigations
- **Requirements**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, languages such as Java, Ruby, and Lisp perform automatic garbage collection that releases memory for objects that have been deallocated.
- **Implementation**: It is good practice to be responsible for freeing all resources you allocate and to be consistent with how and where you free resources in a function. If you allocate resources that you intend to free upon completion of the function, you must be sure to free the resources at all exit points for that function including error conditions.
- **Operation, Architecture and Design**: Use resource-limiting settings provided by the operating system or environment. For example, when managing system resources in POSIX, setrlimit() can be used to set limits for certain types of resources, and getrlimit() can determine how many resources are available. However, these functions are not available on all operating systems. When the current levels get close to the maximum that is defined for the application (see CWE-770), then limit the allocation of further resources to privileged users; alternately, begin releasing resources for less-privileged users. While this mitigation may protect the system from attack, it will not necessarily stop attackers from adversely impacting other users. Ensure that the application performs the appropriate error checks and error handling in case resources become unavailable (CWE-703).

## Related attack patterns (CAPEC)
- [CAPEC-469](https://capec.mitre.org/data/definitions/469.html)

## Related weaknesses
- CWE-404 (ChildOf)
- CWE-404 (ChildOf)
- CWE-404 (ChildOf)
- CWE-404 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-0897**: Chain: anti-virus product encounters a malformed file but returns from a function without closing a file descriptor (CWE-775) leading to file descriptor consumption (CWE-400) and failed scans.
- **CVE-2001-0830**: Sockets not properly closed when attacker repeatedly connects and disconnects from server.
- **CVE-1999-1127**: Does not shut down named pipe connections if malformed data is sent.
- **CVE-2009-2858**: Chain: memory leak (CWE-404) leads to resource exhaustion.
- **CVE-2009-2054**: Product allows exhaustion of file descriptors when processing a large number of TCP packets.
- **CVE-2008-2122**: Port scan triggers CPU consumption with processes that attempt to read data from closed sockets.
- **CVE-2007-4103**: Product allows resource exhaustion via a large number of calls that do not complete a 3-way handshake.
- **CVE-2002-1372**: Chain: Return values of file/socket operations are not checked (CWE-252), allowing resultant consumption of file descriptors (CWE-772).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/772.html
