---
cwe_id: CWE-412
name: Unrestricted Externally Accessible Lock
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-25]
url: https://cwe.mitre.org/data/definitions/412.html
tags: [mitre-cwe, weakness, CWE-412]
---

# CWE-412 - Unrestricted Externally Accessible Lock

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-412](https://cwe.mitre.org/data/definitions/412.html)

## Description
The product properly checks for the existence of a lock, but the lock can be externally controlled or influenced by an actor that is outside of the intended sphere of control.

## Extended description
This prevents the product from acting on associated resources or performing other behaviors that are controlled by the presence of the lock. Relevant locks might include an exclusive lock or mutex, or modifying a shared resource that is treated as a lock. If the lock can be held for an indefinite period of time, then the denial of service could be permanent.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design, Implementation**: Use any access control that is offered by the functionality that is offering the lock.
- **Architecture and Design, Implementation**: Use unpredictable names or identifiers for the locks. This might not always be possible or feasible.
- **Architecture and Design**: Consider modifying your code to use non-blocking synchronization methods.

## Related attack patterns (CAPEC)
- [CAPEC-25](https://capec.mitre.org/data/definitions/25.html)

## Related weaknesses
- CWE-667 (ChildOf)
- CWE-410 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2001-0682**: Program can not execute when attacker obtains a mutex.
- **CVE-2002-1914**: Program can not execute when attacker obtains a lock on a critical output file.
- **CVE-2002-1915**: Program can not execute when attacker obtains a lock on a critical output file.
- **CVE-2002-0051**: Critical file can be opened with exclusive read access by user, preventing application of security policy. Possibly related to improper permissions, large-window race condition.
- **CVE-2000-0338**: Chain: predictable file names used for locking, allowing attacker to create the lock beforehand. Resultant from permissions and randomness.
- **CVE-2000-1198**: Chain: Lock files with predictable names. Resultant from randomness.
- **CVE-2002-1869**: Product does not check if it can write to a log file, allowing attackers to avoid logging by accessing the file using an exclusive lock. Overlaps unchecked error condition. This is not quite CWE-412, but close.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/412.html
