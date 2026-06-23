---
cwe_id: CWE-1043
name: Data Element Aggregating an Excessively Large Number of Non-Primitive Elements
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1043.html
tags: [mitre-cwe, weakness, CWE-1043]
---

# CWE-1043 - Data Element Aggregating an Excessively Large Number of Non-Primitive Elements

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1043](https://cwe.mitre.org/data/definitions/1043.html)

## Description
The product uses a data element that has an excessively large number of sub-elements with non-primitive data types such as structures or aggregated objects.

## Extended description
While the interpretation of "excessively large" may vary for each product or developer, CISQ recommends a default of 5 sub-elements.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-1093 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1043.html
