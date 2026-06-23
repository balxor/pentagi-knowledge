---
cwe_id: CWE-134
name: Use of Externally-Controlled Format String
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, C, C++, Perl]
related_capec: [CAPEC-135, CAPEC-67]
url: https://cwe.mitre.org/data/definitions/134.html
tags: [mitre-cwe, weakness, CWE-134]
---

# CWE-134 - Use of Externally-Controlled Format String

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-134](https://cwe.mitre.org/data/definitions/134.html)

## Description
The product uses a function that accepts a format string as an argument, but the format string originates from an external source.

## Applicable platforms / languages
Not Language-Specific, C, C++, Perl

## Common consequences
- **Confidentiality**: Read Memory
- **Integrity, Confidentiality, Availability**: Modify Memory, Execute Unauthorized Code or Commands

## Potential mitigations
- **Requirements**: Choose a language that is not subject to this flaw.
- **Implementation**: Ensure that all format string functions are passed a static string which cannot be controlled by the user, and that the proper number of arguments are always sent to that function as well. If at all possible, use functions that do not support the %n operator in format strings. [REF-116] [REF-117]
- **Build and Compilation**: Run compilers and linkers with high warning levels, since they may detect incorrect usage.

## Related attack patterns (CAPEC)
- [CAPEC-135](https://capec.mitre.org/data/definitions/135.html)
- [CAPEC-67](https://capec.mitre.org/data/definitions/67.html)

## Related weaknesses
- CWE-668 (ChildOf)
- CWE-668 (ChildOf)
- CWE-123 (CanPrecede)
- CWE-20 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1825**: format string in Perl program
- **CVE-2001-0717**: format string in bad call to syslog function
- **CVE-2002-0573**: format string in bad call to syslog function
- **CVE-2002-1788**: format strings in NNTP server responses
- **CVE-2006-2480**: Format string vulnerability exploited by triggering errors or warnings, as demonstrated via format string specifiers in a .bmp filename.
- **CVE-2007-2027**: Chain: untrusted search path enabling resultant format string by loading malicious internationalization messages

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/134.html
