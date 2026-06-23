---
cwe_id: CWE-663
name: Use of a Non-reentrant Function in a Concurrent Context
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, C]
related_capec: [CAPEC-29]
url: https://cwe.mitre.org/data/definitions/663.html
tags: [mitre-cwe, weakness, CWE-663]
---

# CWE-663 - Use of a Non-reentrant Function in a Concurrent Context

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-663](https://cwe.mitre.org/data/definitions/663.html)

## Description
The product calls a non-reentrant function in a concurrent context in which a competing code sequence (e.g. thread or signal handler) may have an opportunity to call the same function or otherwise influence its state.

## Applicable platforms / languages
Not Language-Specific, C

## Common consequences
- **Integrity, Confidentiality, Other**: Modify Memory, Read Memory, Modify Application Data, Read Application Data, Alter Execution Logic

## Potential mitigations
- **Implementation**: Use reentrant functions if available.
- **Implementation**: Add synchronization to your non-reentrant function.
- **Implementation**: In Java, use the ReentrantLock Class.

## Related attack patterns (CAPEC)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Related weaknesses
- CWE-662 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-1349**: unsafe calls to library functions from signal handler
- **CVE-2004-2259**: SIGCHLD signal to FTP server can cause crash under heavy load while executing non-reentrant functions like malloc/free.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/663.html
