---
cwe_id: CWE-626
name: Null Byte Interaction Error (Poison Null Byte)
type: weakness
abstraction: Variant
status: Draft
languages: [PHP, Perl, ASP.NET]
related_capec: []
url: https://cwe.mitre.org/data/definitions/626.html
tags: [mitre-cwe, weakness, CWE-626]
---

# CWE-626 - Null Byte Interaction Error (Poison Null Byte)

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-626](https://cwe.mitre.org/data/definitions/626.html)

## Description
The product does not properly handle null bytes or NUL characters when passing data between different representations or components.

## Extended description
A null byte (NUL character) can have different meanings across representations or languages. For example, it is a string terminator in standard C libraries, but Perl and PHP strings do not treat it as a terminator. When two representations are crossed - such as when Perl or PHP invokes underlying C functionality - this can produce an interaction error with unexpected results. Similar issues have been reported for ASP. Other interpreters written in C might also be affected. The poison null byte is frequently useful in path traversal attacks by terminating hard-coded extensions that are added to a filename. It can play a role in regular expression processing in PHP.

## Applicable platforms / languages
PHP, Perl, ASP.NET

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Implementation**: Remove null bytes from all incoming strings.

## Related weaknesses
- CWE-147 (ChildOf)
- CWE-436 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-4155**: NUL byte bypasses PHP regular expression check
- **CVE-2005-3153**: inserting SQL after a NUL byte bypasses allowlist regexp, enabling SQL injection

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/626.html
