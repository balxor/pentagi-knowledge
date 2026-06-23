---
cwe_id: CWE-1094
name: Excessive Index Range Scan for a Data Resource
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1094.html
tags: [mitre-cwe, weakness, CWE-1094]
---

# CWE-1094 - Excessive Index Range Scan for a Data Resource

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1094](https://cwe.mitre.org/data/definitions/1094.html)

## Description
The product contains an index range scan for a large data table, but the scan can cover a large number of rows.

## Extended description
While the interpretation of "large data table" and "excessive index range" may vary for each product or developer, CISQ recommends a threshold of 1000000 table rows and a threshold of 10 for the index range.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-405 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1094.html
