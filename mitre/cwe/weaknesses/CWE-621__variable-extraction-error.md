---
cwe_id: CWE-621
name: Variable Extraction Error
type: weakness
abstraction: Variant
status: Incomplete
languages: [PHP]
related_capec: []
url: https://cwe.mitre.org/data/definitions/621.html
tags: [mitre-cwe, weakness, CWE-621]
---

# CWE-621 - Variable Extraction Error

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-621](https://cwe.mitre.org/data/definitions/621.html)

## Description
The product uses external input to determine the names of variables into which information is extracted, without verifying that the names of the specified variables are valid. This could cause the program to overwrite unintended variables.

## Extended description
For example, in PHP, extraction can be used to provide functionality similar to register_globals, a dangerous functionality that is frequently disabled in production systems. Calling extract() or import_request_variables() without the proper arguments could allow arbitrary global variables to be overwritten, including superglobals. Similar functionality is possible in other interpreted languages, including custom languages.

## Applicable platforms / languages
PHP

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation**: Use allowlists of variable names that can be extracted.
- **Implementation**: Consider refactoring your code to avoid extraction routines altogether.
- **Implementation**: In PHP, call extract() with options such as EXTR_SKIP and EXTR_PREFIX_ALL; call import_request_variables() with a prefix argument. Note that these capabilities are not present in all PHP versions.

## Related weaknesses
- CWE-914 (ChildOf)
- CWE-471 (CanPrecede)

## Observed examples (CVE)
- **CVE-2006-7135**: extract issue enables file inclusion
- **CVE-2006-7079**: Chain: PHP app uses extract for register_globals compatibility layer (CWE-621), enabling path traversal (CWE-22)
- **CVE-2007-0649**: extract() buried in include files makes post-disclosure analysis confusing; original report had seemed incorrect.
- **CVE-2006-6661**: extract() enables static code injection
- **CVE-2006-2828**: import_request_variables() buried in include files makes post-disclosure analysis confusing

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/621.html
