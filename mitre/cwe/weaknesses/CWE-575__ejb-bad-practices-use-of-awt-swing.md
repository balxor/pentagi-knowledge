---
cwe_id: CWE-575
name: EJB Bad Practices: Use of AWT Swing
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/575.html
tags: [mitre-cwe, weakness, CWE-575]
---

# CWE-575 - EJB Bad Practices: Use of AWT Swing

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-575](https://cwe.mitre.org/data/definitions/575.html)

## Description
The product violates the Enterprise JavaBeans (EJB) specification by using AWT/Swing.

## Extended description
The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the product violates the following EJB guideline: "An enterprise bean must not use the AWT functionality to attempt to output information to a display, or to input information from a keyboard." The specification justifies this requirement in the following way: "Most servers do not allow direct interaction between an application program and a keyboard/display attached to the server system."

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Architecture and Design**: Do not use AWT/Swing when writing EJBs.

## Related weaknesses
- CWE-695 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/575.html
