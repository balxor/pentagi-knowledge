---
cwe_id: CWE-479
name: Signal Handler Use of a Non-reentrant Function
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/479.html
tags: [mitre-cwe, weakness, CWE-479]
---

# CWE-479 - Signal Handler Use of a Non-reentrant Function

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-479](https://cwe.mitre.org/data/definitions/479.html)

## Description
The product defines a signal handler that calls a non-reentrant function.

## Extended description
Non-reentrant functions are functions that cannot safely be called, interrupted, and then recalled before the first call has finished without resulting in memory corruption. This can lead to an unexpected system state and unpredictable results with a variety of potential consequences depending on context, including denial of service and code execution. Many functions are not reentrant, but some of them can result in the corruption of memory if they are used in a signal handler. The function call syslog() is an example of this. In order to perform its functionality, it allocates a small amount of memory as "scratch space." If syslog() is suspended by a signal call and the signal handler calls syslog(), the memory used by both of these functions enters an undefined, and possibly, exploitable state. Implementations of malloc() and free() manage metadata in global structures in order to track which memory is allocated versus which memory is available, but they are non-reentrant. Simultaneous calls to these functions can cause corruption of the metadata.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands
- **Integrity**: Modify Memory, Modify Application Data

## Potential mitigations
- **Requirements**: Require languages or libraries that provide reentrant functionality, or otherwise make it easier to avoid this weakness.
- **Architecture and Design**: Design signal handlers to only set flags rather than perform complex functionality.
- **Implementation**: Ensure that non-reentrant functions are not found in signal handlers.
- **Implementation**: Use sanity checks to reduce the timing window for exploitation of race conditions. This is only a partial solution, since many attacks might fail, but other attacks still might work within the narrower window, even accidentally.

## Related weaknesses
- CWE-828 (ChildOf)
- CWE-663 (ChildOf)
- CWE-123 (CanPrecede)

## Observed examples (CVE)
- **CVE-2005-0893**: signal handler calls function that ultimately uses malloc()
- **CVE-2004-2259**: SIGCHLD signal to FTP server can cause crash under heavy load while executing non-reentrant functions like malloc/free.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/479.html
