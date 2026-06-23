---
cwe_id: CWE-913
name: Improper Control of Dynamically-Managed Code Resources
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Interpreted]
related_capec: []
url: https://cwe.mitre.org/data/definitions/913.html
tags: [mitre-cwe, weakness, CWE-913]
---

# CWE-913 - Improper Control of Dynamically-Managed Code Resources

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-913](https://cwe.mitre.org/data/definitions/913.html)

## Description
The product does not properly restrict reading from or writing to dynamically-managed code resources such as variables, objects, classes, attributes, functions, or executable instructions or statements.

## Extended description
Many languages offer powerful features that allow the programmer to dynamically create or modify existing code, or resources used by code such as variables and objects. While these features can offer significant flexibility and reduce development time, they can be extremely dangerous if attackers can directly influence these code resources in unexpected ways.

## Applicable platforms / languages
Not Language-Specific, Interpreted

## Common consequences
- **Integrity**: Execute Unauthorized Code or Commands
- **Other, Integrity**: Varies by Context, Alter Execution Logic

## Potential mitigations
- **Implementation**: For any externally-influenced input, check the input against an allowlist of acceptable values.
- **Implementation, Architecture and Design**: Refactor the code so that it does not need to be dynamically managed.

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-2054**: Python compiler uses eval() to execute malicious strings as Python code.
- **CVE-2018-1000613**: Cryptography API uses unsafe reflection when deserializing a private key
- **CVE-2015-8103**: Deserialization issue in commonly-used Java library allows remote execution.
- **CVE-2006-7079**: Chain: extract used for register_globals compatibility layer, enables path traversal (CWE-22)
- **CVE-2012-2055**: Source version control product allows modification of trusted key using mass assignment.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/913.html
