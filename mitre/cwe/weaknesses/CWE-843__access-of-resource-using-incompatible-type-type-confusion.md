---
cwe_id: CWE-843
name: Access of Resource Using Incompatible Type ('Type Confusion')
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/843.html
tags: [mitre-cwe, weakness, CWE-843]
---

# CWE-843 - Access of Resource Using Incompatible Type ('Type Confusion')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-843](https://cwe.mitre.org/data/definitions/843.html)

## Description
The product allocates or initializes a resource such as a pointer, object, or variable using one type, but it later accesses that resource using a type that is incompatible with the original type.

## Extended description
When the product accesses the resource using an incompatible type, this could trigger logical errors because the resource does not have expected properties. In languages without memory safety, such as C and C++, type confusion can lead to out-of-bounds memory access. While this weakness is frequently associated with unions when parsing data with many different embedded object types in C, it can be present in any application that can interpret the same variable or memory location in multiple ways. This weakness is not unique to C and C++. For example, errors in PHP applications can be triggered by providing array parameters when scalars are expected, or vice versa. Languages such as Perl, which perform automatic conversion of a variable of one type when it is accessed as if it were another type, can also contain these issues.

## Applicable platforms / languages
C, C++

## Common consequences
- **Availability, Integrity, Confidentiality**: Read Memory, Modify Memory, Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart

## Related weaknesses
- CWE-704 (ChildOf)
- CWE-704 (ChildOf)
- CWE-119 (CanPrecede)

## Observed examples (CVE)
- **CVE-2025-32352**: Type confusion in PHP app allows authentication bypass when users have passwords whose MD5 hashes can be interpreted as numbers
- **CVE-2010-4577**: Type confusion in CSS sequence leads to out-of-bounds read.
- **CVE-2011-0611**: Size inconsistency allows code execution, first discovered when it was actively exploited in-the-wild.
- **CVE-2010-0258**: Improperly-parsed file containing records of different types leads to code execution when a memory location is interpreted as a different object than intended.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/843.html
