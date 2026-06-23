---
cwe_id: CWE-1060
name: Excessive Number of Inefficient Server-Side Data Accesses
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1060.html
tags: [mitre-cwe, weakness, CWE-1060]
---

# CWE-1060 - Excessive Number of Inefficient Server-Side Data Accesses

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1060](https://cwe.mitre.org/data/definitions/1060.html)

## Description
The product performs too many data queries without using efficient data processing functionality such as stored procedures.

## Extended description
While the interpretation of "too many data queries" may vary for each product or developer, CISQ recommends a default maximum of 5 data queries for an inefficient function/procedure.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-1120 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1060.html
