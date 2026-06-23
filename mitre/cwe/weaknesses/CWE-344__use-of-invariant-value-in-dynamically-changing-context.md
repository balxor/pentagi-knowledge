---
cwe_id: CWE-344
name: Use of Invariant Value in Dynamically Changing Context
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/344.html
tags: [mitre-cwe, weakness, CWE-344]
---

# CWE-344 - Use of Invariant Value in Dynamically Changing Context

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-344](https://cwe.mitre.org/data/definitions/344.html)

## Description
The product uses a constant value, name, or reference, but this value can (or should) vary across different environments.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Related weaknesses
- CWE-330 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0980**: Component for web browser writes an error message to a known location, which can then be referenced by attackers to process HTML/script in a less restrictive context

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/344.html
