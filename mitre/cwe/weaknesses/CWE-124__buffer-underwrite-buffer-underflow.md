---
cwe_id: CWE-124
name: Buffer Underwrite ('Buffer Underflow')
type: weakness
abstraction: Base
status: Incomplete
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/124.html
tags: [mitre-cwe, weakness, CWE-124]
---

# CWE-124 - Buffer Underwrite ('Buffer Underflow')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-124](https://cwe.mitre.org/data/definitions/124.html)

## Description
The product writes to a buffer using an index or pointer that references a memory location prior to the beginning of the buffer.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Integrity, Availability**: Modify Memory, DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability, Access Control, Other**: Execute Unauthorized Code or Commands, Modify Memory, Bypass Protection Mechanism, Other
- **Access Control, Other**: Bypass Protection Mechanism, Other

## Potential mitigations
- **Requirements**: Choose a language that is not susceptible to these issues.
- **Implementation**: All calculated values that are used as index or for pointer arithmetic should be validated to ensure that they are within an expected range.

## Related weaknesses
- CWE-786 (ChildOf)
- CWE-787 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-24018**: buffer underwrite in firmware verification routine allows code execution via a crafted firmware image
- **CVE-2002-2227**: Unchecked length of SSLv2 challenge value leads to buffer underflow.
- **CVE-2007-4580**: Buffer underflow from a small size value with a large buffer (length parameter inconsistency, CWE-130)
- **CVE-2007-1584**: Buffer underflow from an all-whitespace string, which causes a counter to be decremented before the buffer while looking for a non-whitespace character.
- **CVE-2007-0886**: Buffer underflow resultant from encoded data that triggers an integer overflow.
- **CVE-2006-6171**: Product sets an incorrect buffer size limit, leading to "off-by-two" buffer underflow.
- **CVE-2006-4024**: Negative value is used in a memcpy() operation, leading to buffer underflow.
- **CVE-2004-2620**: Buffer underflow due to mishandled special characters

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/124.html
