---
cwe_id: CWE-1057
name: Data Access Operations Outside of Expected Data Manager Component
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1057.html
tags: [mitre-cwe, weakness, CWE-1057]
---

# CWE-1057 - Data Access Operations Outside of Expected Data Manager Component

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1057](https://cwe.mitre.org/data/definitions/1057.html)

## Description
The product uses a dedicated, central data manager component as required by design, but it contains code that performs data-access operations that do not use this data manager.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: Reduce Performance

## Related weaknesses
- CWE-1061 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1057.html
