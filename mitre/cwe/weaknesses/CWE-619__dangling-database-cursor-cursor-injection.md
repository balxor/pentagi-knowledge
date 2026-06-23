---
cwe_id: CWE-619
name: Dangling Database Cursor ('Cursor Injection')
type: weakness
abstraction: Base
status: Incomplete
languages: [SQL, Database Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/619.html
tags: [mitre-cwe, weakness, CWE-619]
---

# CWE-619 - Dangling Database Cursor ('Cursor Injection')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-619](https://cwe.mitre.org/data/definitions/619.html)

## Description
If a database cursor is not closed properly, then it could become accessible to other users while retaining the same privileges that were originally assigned, leaving the cursor "dangling."

## Extended description
For example, an improper dangling cursor could arise from unhandled exceptions. The impact of the issue depends on the cursor's role, but SQL injection attacks are commonly possible.

## Applicable platforms / languages
SQL, Database Server

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Potential mitigations
- **Implementation**: Close cursors immediately after access to them is complete. Ensure that you close cursors if exceptions occur.

## Related weaknesses
- CWE-402 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/619.html
