---
cwe_id: CWE-558
name: Use of getlogin() in Multithreaded Application
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/558.html
tags: [mitre-cwe, weakness, CWE-558]
---

# CWE-558 - Use of getlogin() in Multithreaded Application

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-558](https://cwe.mitre.org/data/definitions/558.html)

## Description
The product uses the getlogin() function in a multithreaded context, potentially causing it to return incorrect values.

## Extended description
The getlogin() function returns a pointer to a string that contains the name of the user associated with the calling process. The function is not reentrant, meaning that if it is called from another process, the contents are not locked out and the value of the string can be changed by another process. This makes it very risky to use because the username can be changed by other processes, so the results of the function cannot be trusted.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity, Access Control, Other**: Modify Application Data, Bypass Protection Mechanism, Other

## Potential mitigations
- **Architecture and Design**: Using names for security purposes is not advised. Names are easy to forge and can have overlapping user IDs, potentially causing confusion or impersonation.
- **Implementation**: Use getlogin_r() instead, which is reentrant, meaning that other processes are locked out from changing the username.

## Related weaknesses
- CWE-663 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/558.html
