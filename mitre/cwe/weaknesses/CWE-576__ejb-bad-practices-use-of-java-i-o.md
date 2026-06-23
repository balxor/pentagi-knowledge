---
cwe_id: CWE-576
name: EJB Bad Practices: Use of Java I/O
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/576.html
tags: [mitre-cwe, weakness, CWE-576]
---

# CWE-576 - EJB Bad Practices: Use of Java I/O

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-576](https://cwe.mitre.org/data/definitions/576.html)

## Description
The product violates the Enterprise JavaBeans (EJB) specification by using the java.io package.

## Extended description
The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the product violates the following EJB guideline: "An enterprise bean must not use the java.io package to attempt to access files and directories in the file system." The specification justifies this requirement in the following way: "The file system APIs are not well-suited for business components to access data. Business components should use a resource manager API, such as JDBC, to store data."

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: Do not use Java I/O when writing EJBs.

## Related weaknesses
- CWE-695 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/576.html
