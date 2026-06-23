---
cwe_id: CWE-1058
name: Invokable Control Element in Multi-Thread Context with non-Final Static Storable or Member Element
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1058.html
tags: [mitre-cwe, weakness, CWE-1058]
---

# CWE-1058 - Invokable Control Element in Multi-Thread Context with non-Final Static Storable or Member Element

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1058](https://cwe.mitre.org/data/definitions/1058.html)

## Description
The code contains a function or method that operates in a multi-threaded environment but owns an unsafe non-final static storable or member data element.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1058.html
