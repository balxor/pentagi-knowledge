---
cwe_id: CWE-1042
name: Static Member Data Element outside of a Singleton Class Element
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1042.html
tags: [mitre-cwe, weakness, CWE-1042]
---

# CWE-1042 - Static Member Data Element outside of a Singleton Class Element

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1042](https://cwe.mitre.org/data/definitions/1042.html)

## Description
The code contains a member element that is declared as static (but not final), in which its parent class element is not a singleton class - that is, a class element that can be used only once in the 'to' association of a Create action.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-1176 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1042.html
