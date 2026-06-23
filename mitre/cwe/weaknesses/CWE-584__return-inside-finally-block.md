---
cwe_id: CWE-584
name: Return Inside Finally Block
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/584.html
tags: [mitre-cwe, weakness, CWE-584]
---

# CWE-584 - Return Inside Finally Block

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-584](https://cwe.mitre.org/data/definitions/584.html)

## Description
The code has a return statement inside a finally block, which will cause any thrown exception in the try block to be discarded.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Alter Execution Logic

## Potential mitigations
- **Implementation**: Do not use a return statement inside the finally block. The finally block should have "cleanup" code.

## Related weaknesses
- CWE-705 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/584.html
