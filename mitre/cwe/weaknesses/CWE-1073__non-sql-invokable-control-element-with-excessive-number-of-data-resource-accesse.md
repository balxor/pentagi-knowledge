---
cwe_id: CWE-1073
name: Non-SQL Invokable Control Element with Excessive Number of Data Resource Accesses
type: weakness
abstraction: Base
status: Incomplete
languages: [SQL, Database Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1073.html
tags: [mitre-cwe, weakness, CWE-1073]
---

# CWE-1073 - Non-SQL Invokable Control Element with Excessive Number of Data Resource Accesses

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1073](https://cwe.mitre.org/data/definitions/1073.html)

## Description
The product contains a client with a function or method that contains a large number of data accesses/queries that are sent through a data manager, i.e., does not use efficient database capabilities.

## Extended description
While the interpretation of "large number of data accesses/queries" may vary for each product or developer, CISQ recommends a default maximum of 2 data accesses per function/method.

## Applicable platforms / languages
SQL, Database Server

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-405 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1073.html
