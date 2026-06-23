---
cwe_id: CWE-435
name: Improper Interaction Between Multiple Correctly-Behaving Entities
type: weakness
abstraction: Pillar
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/435.html
tags: [mitre-cwe, weakness, CWE-435]
---

# CWE-435 - Improper Interaction Between Multiple Correctly-Behaving Entities

**Abstraction:** Pillar  -  **Status:** Draft  -  **CWE:** [CWE-435](https://cwe.mitre.org/data/definitions/435.html)

## Description
An interaction error occurs when two entities have correct behavior when running independently of each other, but when they are integrated as components in a larger system or process, they introduce incorrect behaviors that may cause resultant weaknesses.

## Extended description
When a system or process combines multiple independent components, this often produces new, emergent behaviors at the system level. However, if the interactions between these components are not fully accounted for, some of the emergent behaviors can be incorrect or even insecure.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity**: Unexpected State, Varies by Context

## Observed examples (CVE)
- **CVE-2002-0485**: Anti-virus product allows bypass via Content-Type and Content-Disposition headers that are mixed case, which are still processed by some clients.
- **CVE-2003-0411**: chain: Code was ported from a case-sensitive Unix platform to a case-insensitive Windows platform where filetype handlers treat .jsp and .JSP as different extensions. JSP source code may be read because .JSP defaults to the filetype "text".

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/435.html
