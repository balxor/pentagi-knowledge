---
cwe_id: CWE-396
name: Declaration of Catch for Generic Exception
type: weakness
abstraction: Base
status: Draft
languages: [C++, Java, C#, Python]
related_capec: []
url: https://cwe.mitre.org/data/definitions/396.html
tags: [mitre-cwe, weakness, CWE-396]
---

# CWE-396 - Declaration of Catch for Generic Exception

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-396](https://cwe.mitre.org/data/definitions/396.html)

## Description
Catching overly broad exceptions promotes complex error handling code that is more likely to contain security vulnerabilities.

## Extended description
Multiple catch blocks can get ugly and repetitive, but "condensing" catch blocks by catching a high-level class like Exception can obscure exceptions that deserve special treatment or that should not be caught at this point in the program. Catching an overly broad exception essentially defeats the purpose of a language's typed exceptions, and can become particularly dangerous if the program grows and begins to throw new types of exceptions. The new exception types will not receive any attention.

## Applicable platforms / languages
C++, Java, C#, Python

## Common consequences
- **Non-Repudiation, Other**: Hide Activities

## Related weaknesses
- CWE-705 (ChildOf)
- CWE-755 (ChildOf)
- CWE-221 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/396.html
