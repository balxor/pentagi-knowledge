---
cwe_id: CWE-430
name: Deployment of Wrong Handler
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-11]
url: https://cwe.mitre.org/data/definitions/430.html
tags: [mitre-cwe, weakness, CWE-430]
---

# CWE-430 - Deployment of Wrong Handler

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-430](https://cwe.mitre.org/data/definitions/430.html)

## Description
The wrong "handler" is assigned to process an object.

## Extended description
An example of deploying the wrong handler would be calling a servlet to reveal source code of a .JSP file, or automatically "determining" type of the object even if it is contradictory to an explicitly specified type.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State

## Potential mitigations
- **Architecture and Design**: Perform a type check before interpreting an object.
- **Architecture and Design**: Reject any inconsistent types, such as a file with a .GIF extension that appears to consist of PHP code.

## Related attack patterns (CAPEC)
- [CAPEC-11](https://capec.mitre.org/data/definitions/11.html)

## Related weaknesses
- CWE-691 (ChildOf)
- CWE-433 (CanPrecede)
- CWE-434 (PeerOf)

## Observed examples (CVE)
- **CVE-2001-0004**: Source code disclosure via manipulated file extension that causes parsing by wrong DLL.
- **CVE-2002-0025**: Web browser does not properly handle the Content-Type header field, causing a different application to process the document.
- **CVE-2000-1052**: Source code disclosure by directly invoking a servlet.
- **CVE-2002-1742**: Arbitrary Perl functions can be loaded by calling a non-existent function that activates a handler.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/430.html
