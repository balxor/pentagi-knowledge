---
cwe_id: CWE-1046
name: Creation of Immutable Text Using String Concatenation
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1046.html
tags: [mitre-cwe, weakness, CWE-1046]
---

# CWE-1046 - Creation of Immutable Text Using String Concatenation

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1046](https://cwe.mitre.org/data/definitions/1046.html)

## Description
The product creates an immutable text string using string concatenation operations.

## Extended description
When building a string via a looping feature (e.g., a FOR or WHILE loop), the use of += to append to the existing string will result in the creation of a new object with each iteration, which can be inefficient in comparison with use of text buffer data elements.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-1176 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1046.html
