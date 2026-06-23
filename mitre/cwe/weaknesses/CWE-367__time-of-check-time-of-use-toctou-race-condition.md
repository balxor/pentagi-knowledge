---
cwe_id: CWE-367
name: Time-of-check Time-of-use (TOCTOU) Race Condition
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-27, CAPEC-29]
url: https://cwe.mitre.org/data/definitions/367.html
tags: [mitre-cwe, weakness, CWE-367]
---

# CWE-367 - Time-of-check Time-of-use (TOCTOU) Race Condition

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-367](https://cwe.mitre.org/data/definitions/367.html)

## Description
The product checks the state of a resource before using that resource, but the resource's state can change between the check and the use in a way that invalidates the results of the check.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Alter Execution Logic, Unexpected State
- **Integrity, Other**: Modify Application Data, Modify Files or Directories, Modify Memory, Other
- **Integrity, Other**: Other
- **Non-Repudiation**: Hide Activities
- **Non-Repudiation, Other**: Other
- **Other**: Unexpected State

## Potential mitigations
- **Implementation**: The most basic advice for TOCTOU vulnerabilities is to not perform a check before the use. This does not resolve the underlying issue of the execution of a function on a resource whose state and identity cannot be assured, but it does help to limit the false sense of security given by the check.
- **Implementation**: When the file being altered is owned by the current user and group, set the effective gid and uid to that of the current user and group when executing this statement.
- **Architecture and Design**: Limit the interleaving of operations on files from multiple processes.
- **Implementation, Architecture and Design**: If you cannot perform operations atomically and you must share access to the resource between multiple processes or threads, then try to limit the amount of time (CPU cycles) between the check and use of the resource. This will not fix the problem, but it could make it more difficult for an attack to succeed.
- **Implementation**: Recheck the resource after the use call to verify that the action was taken appropriately.
- **Architecture and Design**: Ensure that some environmental locking mechanism can be used to protect resources effectively.
- **Implementation**: Ensure that locking occurs before the check, as opposed to afterwards, such that the resource, as checked, is the same as it is when in use.

## Related attack patterns (CAPEC)
- [CAPEC-27](https://capec.mitre.org/data/definitions/27.html)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Related weaknesses
- CWE-362 (ChildOf)
- CWE-362 (ChildOf)

## Observed examples (CVE)
- **CVE-2015-1743**: TOCTOU in sandbox process allows installation of untrusted browser add-ons by replacing a file after it has been verified, but before it is executed
- **CVE-2003-0813**: Chain: A multi-threaded race condition (CWE-367) allows attackers to cause two threads to process the same RPC request, which causes a use-after-free (CWE-416) in one thread
- **CVE-2004-0594**: PHP flaw allows remote attackers to execute arbitrary code by aborting execution before the initialization of key data structures is complete.
- **CVE-2008-2958**: chain: time-of-check time-of-use (TOCTOU) race condition in program allows bypass of protection mechanism that was designed to prevent symlink attacks.
- **CVE-2008-1570**: chain: time-of-check time-of-use (TOCTOU) race condition in program allows bypass of protection mechanism that was designed to prevent symlink attacks.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/367.html
