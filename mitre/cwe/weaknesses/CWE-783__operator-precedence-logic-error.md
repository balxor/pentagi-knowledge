---
cwe_id: CWE-783
name: Operator Precedence Logic Error
type: weakness
abstraction: Base
status: Draft
languages: [C, C++, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/783.html
tags: [mitre-cwe, weakness, CWE-783]
---

# CWE-783 - Operator Precedence Logic Error

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-783](https://cwe.mitre.org/data/definitions/783.html)

## Description
The product uses an expression in which operator precedence causes incorrect logic to be used.

## Extended description
While often just a bug, operator precedence logic errors can have serious consequences if they are used in security-critical code, such as making an authentication decision.

## Applicable platforms / languages
C, C++, Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Varies by Context, Unexpected State

## Potential mitigations
- **Implementation**: Regularly wrap sub-expressions in parentheses, especially in security-critical code.

## Related weaknesses
- CWE-670 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-2516**: Authentication module allows authentication bypass because it uses "(x = call(args) == SUCCESS)" instead of "((x = call(args)) == SUCCESS)".
- **CVE-2008-0599**: Chain: Language interpreter calculates wrong buffer size (CWE-131) by using "size = ptr ? X : Y" instead of "size = (ptr ? X : Y)" expression.
- **CVE-2001-1155**: Chain: product does not properly check the result of a reverse DNS lookup because of operator precedence (CWE-783), allowing bypass of DNS-based access restrictions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/783.html
