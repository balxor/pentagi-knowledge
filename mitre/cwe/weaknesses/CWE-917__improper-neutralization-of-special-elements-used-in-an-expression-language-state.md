---
cwe_id: CWE-917
name: Improper Neutralization of Special Elements used in an Expression Language Statement ('Expression Language Injection')
type: weakness
abstraction: Base
status: Incomplete
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/917.html
tags: [mitre-cwe, weakness, CWE-917]
---

# CWE-917 - Improper Neutralization of Special Elements used in an Expression Language Statement ('Expression Language Injection')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-917](https://cwe.mitre.org/data/definitions/917.html)

## Description
The product constructs all or part of an expression language (EL) statement in a framework such as a Java Server Page (JSP) using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended EL statement before it is executed.

## Extended description
Frameworks such as Java Server Page (JSP) allow a developer to insert executable expressions within otherwise-static content. When the developer is not aware of the executable nature of these expressions and/or does not disable them, then if an attacker can inject expressions, this could lead to code execution or other unexpected behaviors.

## Applicable platforms / languages
Java

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Avoid adding user-controlled data into an expression interpreter when possible.
- **Implementation**: If user-controlled data must be added to an expression interpreter, one or more of the following should be performed: Validate that the user input will not evaluate as an expression Encode the user input in a way that ensures it is not evaluated as an expression
- **System Configuration, Operation**: The framework or tooling might allow the developer to disable or deactivate the processing of EL expressions, such as setting the isELIgnored attribute for a JSP page to "true".

## Related weaknesses
- CWE-77 (ChildOf)
- CWE-1336 (PeerOf)
- CWE-74 (ChildOf)
- CWE-77 (ChildOf)
- CWE-77 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-44228**: Product does not neutralize ${xyz} style expressions, allowing remote code execution. (log4shell vulnerability in log4j)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/917.html
