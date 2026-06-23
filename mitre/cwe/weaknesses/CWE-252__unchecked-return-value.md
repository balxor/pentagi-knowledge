---
cwe_id: CWE-252
name: Unchecked Return Value
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/252.html
tags: [mitre-cwe, weakness, CWE-252]
---

# CWE-252 - Unchecked Return Value

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-252](https://cwe.mitre.org/data/definitions/252.html)

## Description
The product does not check the return value from a method or function, which can prevent it from detecting unexpected states and conditions.

## Extended description
Two common programmer assumptions are "this function call can never fail" and "it doesn't matter if this function call fails". If an attacker can force the function to fail or otherwise return a value that is not expected, then the subsequent program logic could lead to a vulnerability, because the product is not in a state that the programmer assumes. For example, if the program calls a function to drop privileges but does not check the return code to ensure that privileges were successfully dropped, then the program will continue to operate with the higher privileges.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability, Integrity**: Unexpected State, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Check the results of all functions that return a value and verify that the value is expected.
- **Implementation**: For any pointers that could have been modified or provided from a function that can return NULL, check the pointer for NULL before use. When working with a multithreaded or otherwise asynchronous environment, ensure that proper locking APIs are used to lock before the check, and unlock when it has finished [REF-1484].
- **Implementation**: Ensure that you account for all possible return values from the function.
- **Implementation**: When designing a function, make sure you return a value or throw an exception in case of an error.

## Related weaknesses
- CWE-754 (ChildOf)
- CWE-754 (ChildOf)
- CWE-476 (CanPrecede)

## Observed examples (CVE)
- **CVE-2020-17533**: Chain: unchecked return value (CWE-252) of some functions for policy enforcement leads to authorization bypass (CWE-862)
- **CVE-2020-6078**: Chain: The return value of a function returning a pointer is not checked for success (CWE-252) resulting in the later use of an uninitialized variable (CWE-456) and a null pointer dereference (CWE-476)
- **CVE-2019-15900**: Chain: sscanf() call is used to check if a username and group exists, but the return value of sscanf() call is not checked (CWE-252), causing an uninitialized variable to be checked (CWE-457), returning success to allow authorization bypass for executing a privileged (CWE-863).
- **CVE-2007-3798**: Unchecked return value leads to resultant integer overflow and code execution.
- **CVE-2006-4447**: Program does not check return value when invoking functions to drop privileges, which could leave users with higher privileges than expected by forcing those functions to fail.
- **CVE-2006-2916**: Program does not check return value when invoking functions to drop privileges, which could leave users with higher privileges than expected by forcing those functions to fail.
- **CVE-2008-5183**: chain: unchecked return value can lead to NULL dereference
- **CVE-2010-0211**: chain: unchecked return value (CWE-252) leads to free of invalid, uninitialized pointer (CWE-824).
- **CVE-2017-6964**: Linux-based device mapper encryption program does not check the return value of setuid and setgid allowing attackers to execute code with unintended privileges.
- **CVE-2002-1372**: Chain: Return values of file/socket operations are not checked (CWE-252), allowing resultant consumption of file descriptors (CWE-772).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/252.html
