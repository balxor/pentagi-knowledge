---
cwe_id: CWE-574
name: EJB Bad Practices: Use of Synchronization Primitives
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/574.html
tags: [mitre-cwe, weakness, CWE-574]
---

# CWE-574 - EJB Bad Practices: Use of Synchronization Primitives

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-574](https://cwe.mitre.org/data/definitions/574.html)

## Description
The product violates the Enterprise JavaBeans (EJB) specification by using thread synchronization primitives.

## Extended description
The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the product violates the following EJB guideline: "An enterprise bean must not use thread synchronization primitives to synchronize execution of multiple instances." The specification justifies this requirement in the following way: "This rule is required to ensure consistent runtime semantics because while some EJB containers may use a single JVM to execute all enterprise bean's instances, others may distribute the instances across multiple JVMs."

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: Do not use Synchronization Primitives when writing EJBs.

## Related weaknesses
- CWE-695 (ChildOf)
- CWE-821 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/574.html
