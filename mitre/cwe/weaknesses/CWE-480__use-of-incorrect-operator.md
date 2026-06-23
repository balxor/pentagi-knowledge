---
cwe_id: CWE-480
name: Use of Incorrect Operator
type: weakness
abstraction: Base
status: Draft
languages: [C, C++, Perl, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/480.html
tags: [mitre-cwe, weakness, CWE-480]
---

# CWE-480 - Use of Incorrect Operator

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-480](https://cwe.mitre.org/data/definitions/480.html)

## Description
The product accidentally uses the wrong operator, which changes the logic in security-relevant ways.

## Extended description
These types of errors are generally the result of a typo by the programmer.

## Applicable platforms / languages
C, C++, Perl, Not Language-Specific

## Common consequences
- **Other**: Alter Execution Logic

## Related weaknesses
- CWE-670 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-3979**: Chain: data visualization program written in PHP uses the "!=" operator instead of the type-strict "!==" operator (CWE-480) when validating hash values, potentially leading to an incorrect type conversion (CWE-704)
- **CVE-2021-3116**: Chain: Python-based HTTP Proxy server uses the wrong boolean operators (CWE-480) causing an incorrect comparison (CWE-697) that identifies an authN failure if all three conditions are met instead of only one, allowing bypass of the proxy authentication (CWE-1390)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/480.html
