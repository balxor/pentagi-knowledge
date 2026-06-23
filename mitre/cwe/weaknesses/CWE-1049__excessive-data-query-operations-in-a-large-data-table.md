---
cwe_id: CWE-1049
name: Excessive Data Query Operations in a Large Data Table
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1049.html
tags: [mitre-cwe, weakness, CWE-1049]
---

# CWE-1049 - Excessive Data Query Operations in a Large Data Table

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1049](https://cwe.mitre.org/data/definitions/1049.html)

## Description
The product performs a data query with a large number of joins and sub-queries on a large data table.

## Extended description
While the interpretation of "large data table" and "large number of joins or sub-queries" may vary for each product or developer, CISQ recommends a default of 1 million rows for a "large" data table, a default minimum of 5 joins, and a default minimum of 3 sub-queries.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-1176 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1049.html
