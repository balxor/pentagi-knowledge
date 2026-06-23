---
cwe_id: CWE-397
name: Declaration of Throws for Generic Exception
type: weakness
abstraction: Base
status: Draft
languages: [C++, C#, Java, Python]
related_capec: []
url: https://cwe.mitre.org/data/definitions/397.html
tags: [mitre-cwe, weakness, CWE-397]
---

# CWE-397 - Declaration of Throws for Generic Exception

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-397](https://cwe.mitre.org/data/definitions/397.html)

## Description
The product throws or raises an overly broad exceptions that can hide important details and produce inappropriate responses to certain conditions.

## Extended description
Declaring a method to throw Exception or Throwable promotes generic error handling procedures that make it difficult for callers to perform proper error handling and error recovery. For example, Java's exception mechanism makes it easy for callers to anticipate what can go wrong and write code to handle each specific exceptional circumstance. Declaring that a method throws a generic form of exception defeats this system.

## Applicable platforms / languages
C++, C#, Java, Python

## Common consequences
- **Non-Repudiation, Other**: Hide Activities, Alter Execution Logic

## Related weaknesses
- CWE-705 (ChildOf)
- CWE-221 (ChildOf)
- CWE-703 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/397.html
