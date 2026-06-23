---
cwe_id: CWE-585
name: Empty Synchronized Block
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/585.html
tags: [mitre-cwe, weakness, CWE-585]
---

# CWE-585 - Empty Synchronized Block

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-585](https://cwe.mitre.org/data/definitions/585.html)

## Description
The product contains an empty synchronized block.

## Extended description
An empty synchronized block does not actually accomplish any synchronization and may indicate a troubled section of code. An empty synchronized block can occur because code no longer needed within the synchronized block is commented out without removing the synchronized block.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Other

## Potential mitigations
- **Implementation**: When you come across an empty synchronized statement, or a synchronized statement in which the code has been commented out, try to determine what the original intentions were and whether or not the synchronized block is still necessary.

## Related weaknesses
- CWE-1071 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/585.html
