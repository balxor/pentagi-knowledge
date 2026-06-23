---
cwe_id: CWE-628
name: Function Call with Incorrectly Specified Arguments
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/628.html
tags: [mitre-cwe, weakness, CWE-628]
---

# CWE-628 - Function Call with Incorrectly Specified Arguments

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-628](https://cwe.mitre.org/data/definitions/628.html)

## Description
The product calls a function, procedure, or routine with arguments that are not correctly specified, leading to always-incorrect behavior and resultant weaknesses.

## Extended description
There are multiple ways in which this weakness can be introduced, including: the wrong variable or reference; an incorrect number of arguments; incorrect order of arguments; wrong type of arguments; or wrong value.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other, Access Control**: Quality Degradation, Gain Privileges or Assume Identity

## Potential mitigations
- **Build and Compilation**: Once found, these issues are easy to fix. Use code inspection tools and relevant compiler features to identify potential violations. Pay special attention to code that is not likely to be exercised heavily during QA.
- **Architecture and Design**: Make sure your API's are stable before you use them in production code.

## Related weaknesses
- CWE-573 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-7049**: The method calls the functions with the wrong argument order, which allows remote attackers to bypass intended access restrictions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/628.html
