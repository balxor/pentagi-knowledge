---
cwe_id: CWE-1075
name: Unconditional Control Flow Transfer outside of Switch Block
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1075.html
tags: [mitre-cwe, weakness, CWE-1075]
---

# CWE-1075 - Unconditional Control Flow Transfer outside of Switch Block

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1075](https://cwe.mitre.org/data/definitions/1075.html)

## Description
The product performs unconditional control transfer (such as a "goto") in code outside of a branching structure such as a switch block.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability, Increase Analytical Complexity

## Related weaknesses
- CWE-1120 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1075.html
