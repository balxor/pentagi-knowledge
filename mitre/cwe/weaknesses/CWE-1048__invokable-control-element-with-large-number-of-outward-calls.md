---
cwe_id: CWE-1048
name: Invokable Control Element with Large Number of Outward Calls
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1048.html
tags: [mitre-cwe, weakness, CWE-1048]
---

# CWE-1048 - Invokable Control Element with Large Number of Outward Calls

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1048](https://cwe.mitre.org/data/definitions/1048.html)

## Description
The code contains callable control elements that contain an excessively large number of references to other application objects external to the context of the callable, i.e. a Fan-Out value that is excessively large.

## Extended description
While the interpretation of "excessively large Fan-Out value" may vary for each product or developer, CISQ recommends a default of 5 referenced objects.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability, Increase Analytical Complexity

## Related weaknesses
- CWE-710 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1048.html
