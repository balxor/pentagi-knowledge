---
cwe_id: CWE-690
name: Unchecked Return Value to NULL Pointer Dereference
type: weakness
abstraction: Compound
status: Draft
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/690.html
tags: [mitre-cwe, weakness, CWE-690]
---

# CWE-690 - Unchecked Return Value to NULL Pointer Dereference

**Abstraction:** Compound  -  **Status:** Draft  -  **CWE:** [CWE-690](https://cwe.mitre.org/data/definitions/690.html)

## Description
The product does not check for an error after calling a function that can return with a NULL pointer if the function fails, which leads to a resultant NULL pointer dereference.

## Extended description
While unchecked return value weaknesses are not limited to returns of NULL pointers (see the examples in CWE-252), functions often return NULL to indicate an error status. When this error condition is not checked, a NULL pointer dereference can occur.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands, Read Memory, Modify Memory

## Related weaknesses
- CWE-252 (StartsWith)
- CWE-252 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-1052**: Large Content-Length value leads to NULL pointer dereference when malloc fails.
- **CVE-2006-6227**: Large message length field leads to NULL pointer dereference when malloc fails.
- **CVE-2006-2555**: Parsing routine encounters NULL dereference when input is missing a colon separator.
- **CVE-2003-1054**: URI parsing API sets argument to NULL when a parsing failure occurs, such as when the Referer header is missing a hostname, leading to NULL dereference.
- **CVE-2008-5183**: chain: unchecked return value can lead to NULL dereference

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/690.html
