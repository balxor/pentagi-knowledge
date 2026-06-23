---
cwe_id: CWE-1089
name: Large Data Table with Excessive Number of Indices
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1089.html
tags: [mitre-cwe, weakness, CWE-1089]
---

# CWE-1089 - Large Data Table with Excessive Number of Indices

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1089](https://cwe.mitre.org/data/definitions/1089.html)

## Description
The product uses a large data table that contains an excessively large number of indices.

## Extended description
While the interpretation of "large data table" and "excessively large number of indices" may vary for each product or developer, CISQ recommends a default threshold of 1000000 rows for a "large" table and a default threshold of 3 indices.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-405 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1089.html
