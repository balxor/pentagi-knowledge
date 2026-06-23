---
cwe_id: CWE-230
name: Improper Handling of Missing Values
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/230.html
tags: [mitre-cwe, weakness, CWE-230]
---

# CWE-230 - Improper Handling of Missing Values

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-230](https://cwe.mitre.org/data/definitions/230.html)

## Description
The product does not handle or incorrectly handles when a parameter, field, or argument name is specified, but the associated value is missing, i.e. it is empty, blank, or null.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-229 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0422**: Blank Host header triggers resultant infoleak.
- **CVE-2000-1006**: Blank "charset" attribute in MIME header triggers crash.
- **CVE-2004-1504**: Blank parameter causes external error infoleak.
- **CVE-2005-2053**: Blank parameter causes external error infoleak.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/230.html
