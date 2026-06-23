---
cwe_id: CWE-546
name: Suspicious Comment
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/546.html
tags: [mitre-cwe, weakness, CWE-546]
---

# CWE-546 - Suspicious Comment

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-546](https://cwe.mitre.org/data/definitions/546.html)

## Description
The code contains comments that suggest the presence of bugs, incomplete functionality, or weaknesses.

## Extended description
Many suspicious comments, such as BUG, HACK, FIXME, LATER, LATER2, TODO, in the code indicate missing security functionality and checking. Others indicate code problems that programmers should fix, such as hard-coded variables, error handling, not using stored procedures, and performance issues.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Documentation**: Remove comments that suggest the presence of bugs, incomplete functionality, or weaknesses, before deploying the application.

## Related weaknesses
- CWE-1078 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/546.html
