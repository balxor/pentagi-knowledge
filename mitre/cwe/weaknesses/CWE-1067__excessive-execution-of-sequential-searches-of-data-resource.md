---
cwe_id: CWE-1067
name: Excessive Execution of Sequential Searches of Data Resource
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1067.html
tags: [mitre-cwe, weakness, CWE-1067]
---

# CWE-1067 - Excessive Execution of Sequential Searches of Data Resource

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1067](https://cwe.mitre.org/data/definitions/1067.html)

## Description
The product contains a data query against an SQL table or view that is configured in a way that does not utilize an index and may cause sequential searches to be performed.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: Reduce Performance

## Related weaknesses
- CWE-1176 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1067.html
