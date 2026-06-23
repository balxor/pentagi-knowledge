---
cwe_id: CWE-756
name: Missing Custom Error Page
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/756.html
tags: [mitre-cwe, weakness, CWE-756]
---

# CWE-756 - Missing Custom Error Page

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-756](https://cwe.mitre.org/data/definitions/756.html)

## Description
The product does not return custom error pages to the user, possibly exposing sensitive information.

## Applicable platforms / languages
Not Language-Specific, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-755 (ChildOf)
- CWE-209 (CanPrecede)

## Observed examples (CVE)
- **CVE-2023-27998**: analytics platform does not have a custom error page, allowing access to sensitive information

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/756.html
