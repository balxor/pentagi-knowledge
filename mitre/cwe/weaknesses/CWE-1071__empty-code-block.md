---
cwe_id: CWE-1071
name: Empty Code Block
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1071.html
tags: [mitre-cwe, weakness, CWE-1071]
---

# CWE-1071 - Empty Code Block

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1071](https://cwe.mitre.org/data/definitions/1071.html)

## Description
The source code contains a block that does not contain any code, i.e., the block is empty.

## Extended description
Empty code blocks can occur in the bodies of conditionals, function or method definitions, exception handlers, etc. While an empty code block might be intentional, it might also indicate incomplete implementation, accidental code deletion, unexpected macro expansion, etc. For some programming languages and constructs, an empty block might be allowed by the syntax, but the lack of any behavior within the block might violate a convention or API in such a way that it is an error.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-1164 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1071.html
