---
cwe_id: CWE-439
name: Behavioral Change in New Version or Environment
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/439.html
tags: [mitre-cwe, weakness, CWE-439]
---

# CWE-439 - Behavioral Change in New Version or Environment

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-439](https://cwe.mitre.org/data/definitions/439.html)

## Description
A's behavior or functionality changes with a new version of A, or a new environment, which is not known (or manageable) by B.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Related weaknesses
- CWE-435 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1976**: Linux kernel 2.2 and above allow promiscuous mode using a different method than previous versions, and ifconfig is not aware of the new method (alternate path property).
- **CVE-2005-1711**: Product uses defunct method from another product that does not return an error code and allows detection avoidance.
- **CVE-2003-0411**: chain: Code was ported from a case-sensitive Unix platform to a case-insensitive Windows platform where filetype handlers treat .jsp and .JSP as different extensions. JSP source code may be read because .JSP defaults to the filetype "text".

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/439.html
