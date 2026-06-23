---
cwe_id: CWE-676
name: Use of Potentially Dangerous Function
type: weakness
abstraction: Base
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/676.html
tags: [mitre-cwe, weakness, CWE-676]
---

# CWE-676 - Use of Potentially Dangerous Function

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-676](https://cwe.mitre.org/data/definitions/676.html)

## Description
The product invokes a potentially dangerous function that could introduce a vulnerability if it is used incorrectly, but the function can also be used safely.

## Applicable platforms / languages
C, C++

## Common consequences
- **Other**: Varies by Context, Quality Degradation, Unexpected State

## Potential mitigations
- **Build and Compilation, Implementation**: Identify a list of prohibited API functions and prohibit developers from using these functions, providing safer alternatives. In some cases, automatic code analysis tools or the compiler can be instructed to spot use of prohibited functions, such as the "banned.h" include file from Microsoft's SDL. [REF-554] [REF-1009] [REF-7]

## Related weaknesses
- CWE-1177 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-1470**: Library has multiple buffer overflows using sprintf() and strcpy()
- **CVE-2009-3849**: Buffer overflow using strcat()
- **CVE-2006-2114**: Buffer overflow using strcpy()
- **CVE-2006-0963**: Buffer overflow using strcpy()
- **CVE-2011-0712**: Vulnerable use of strcpy() changed to use safer strlcpy()
- **CVE-2008-5005**: Buffer overflow using strcpy()

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/676.html
