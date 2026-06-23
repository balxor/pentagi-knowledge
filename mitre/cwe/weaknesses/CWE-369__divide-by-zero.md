---
cwe_id: CWE-369
name: Divide By Zero
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/369.html
tags: [mitre-cwe, weakness, CWE-369]
---

# CWE-369 - Divide By Zero

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-369](https://cwe.mitre.org/data/definitions/369.html)

## Description
The product divides a value by zero.

## Extended description
This weakness typically occurs when an unexpected value is provided to the product, or if an error occurs that is not properly detected. It frequently occurs in calculations involving physical dimensions such as size, length, width, and height.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart

## Related weaknesses
- CWE-682 (ChildOf)
- CWE-682 (ChildOf)
- CWE-682 (ChildOf)
- CWE-682 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-3268**: Invalid size value leads to divide by zero.
- **CVE-2007-2723**: "Empty" content triggers divide by zero.
- **CVE-2007-2237**: Height value of 0 triggers divide by zero.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/369.html
