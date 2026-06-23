---
cwe_id: CWE-768
name: Incorrect Short Circuit Evaluation
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, C]
related_capec: []
url: https://cwe.mitre.org/data/definitions/768.html
tags: [mitre-cwe, weakness, CWE-768]
---

# CWE-768 - Incorrect Short Circuit Evaluation

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-768](https://cwe.mitre.org/data/definitions/768.html)

## Description
The product contains a conditional statement with multiple logical expressions in which one of the non-leading expressions may produce side effects. This may lead to an unexpected state in the program after the execution of the conditional, because short-circuiting logic may prevent the side effects from occurring.

## Extended description
Usage of short circuit evaluation, though well-defined in the C standard, may alter control flow in a way that introduces logic errors that are difficult to detect, possibly causing errors later during the product's execution. If an attacker can discover such an inconsistency, it may be exploitable to gain arbitrary control over a system. If the first condition of an "or" statement is assumed to be true under normal circumstances, or if the first condition of an "and" statement is assumed to be false, then any subsequent conditional may contain its own logic errors that are not detected during code review or testing. Finally, the usage of short circuit evaluation may decrease the maintainability of the code.

## Applicable platforms / languages
Not Language-Specific, C

## Common consequences
- **Confidentiality, Integrity, Availability**: Varies by Context

## Potential mitigations
- **Implementation**: Minimizing the number of statements in a conditional that produce side effects will help to prevent the likelihood of short circuit evaluation to alter control flow in an unexpected way.

## Related weaknesses
- CWE-691 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/768.html
