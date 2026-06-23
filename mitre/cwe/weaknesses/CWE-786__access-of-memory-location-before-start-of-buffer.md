---
cwe_id: CWE-786
name: Access of Memory Location Before Start of Buffer
type: weakness
abstraction: Base
status: Incomplete
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/786.html
tags: [mitre-cwe, weakness, CWE-786]
---

# CWE-786 - Access of Memory Location Before Start of Buffer

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-786](https://cwe.mitre.org/data/definitions/786.html)

## Description
The product reads or writes to a buffer using an index or pointer that references a memory location prior to the beginning of the buffer.

## Extended description
This typically occurs when a pointer or its index is decremented to a position before the buffer, when pointer arithmetic results in a position before the beginning of the valid memory location, or when a negative index is used.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality**: Read Memory
- **Integrity, Availability**: Modify Memory, DoS: Crash, Exit, or Restart
- **Integrity**: Modify Memory, Execute Unauthorized Code or Commands

## Related weaknesses
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-2227**: Unchecked length of SSLv2 challenge value leads to buffer underflow.
- **CVE-2007-4580**: Buffer underflow from a small size value with a large buffer (length parameter inconsistency, CWE-130)
- **CVE-2007-1584**: Buffer underflow from an all-whitespace string, which causes a counter to be decremented before the buffer while looking for a non-whitespace character.
- **CVE-2007-0886**: Buffer underflow resultant from encoded data that triggers an integer overflow.
- **CVE-2006-6171**: Product sets an incorrect buffer size limit, leading to "off-by-two" buffer underflow.
- **CVE-2006-4024**: Negative value is used in a memcpy() operation, leading to buffer underflow.
- **CVE-2004-2620**: Buffer underflow due to mishandled special characters

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/786.html
