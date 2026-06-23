---
cwe_id: CWE-1109
name: Use of Same Variable for Multiple Purposes
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1109.html
tags: [mitre-cwe, weakness, CWE-1109]
---

# CWE-1109 - Use of Same Variable for Multiple Purposes

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1109](https://cwe.mitre.org/data/definitions/1109.html)

## Description
The code contains a callable, block, or other code element in which the same variable is used to control more than one unique task or store more than one instance of data.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability
- **Other**: Increase Analytical Complexity

## Related weaknesses
- CWE-1078 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-26463**: Chain: IPSec VPN product uses the same variable for multiple purposes in the same function (CWE-1109), leading to incorrect access control (CWE-284) and expired pointer dereference (CWE-825)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1109.html
