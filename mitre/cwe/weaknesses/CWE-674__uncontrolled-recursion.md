---
cwe_id: CWE-674
name: Uncontrolled Recursion
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-230, CAPEC-231]
url: https://cwe.mitre.org/data/definitions/674.html
tags: [mitre-cwe, weakness, CWE-674]
---

# CWE-674 - Uncontrolled Recursion

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-674](https://cwe.mitre.org/data/definitions/674.html)

## Description
The product does not properly control the amount of recursion that takes place, consuming excessive resources, such as allocated memory or the program stack.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Ensure that an end condition will be reached under all logic conditions. The end condition may include checking against the depth of recursion and exiting with an error if the recursion goes too deep. The complexity of the end condition contributes to the effectiveness of this action.
- **Implementation**: Increase the stack size.

## Related attack patterns (CAPEC)
- [CAPEC-230](https://capec.mitre.org/data/definitions/230.html)
- [CAPEC-231](https://capec.mitre.org/data/definitions/231.html)

## Related weaknesses
- CWE-834 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-1285**: Deeply nested arrays trigger stack exhaustion.
- **CVE-2007-3409**: Self-referencing pointers create infinite loop and resultant stack exhaustion.
- **CVE-2016-10707**: Javascript application accidentally changes input in a way that prevents a recursive call from detecting an exit condition.
- **CVE-2016-3627**: An attempt to recover a corrupted XML file infinite recursion protection counter was not always incremented missing the exit condition.
- **CVE-2019-15118**: USB-audio driver's descriptor code parsing allows unlimited recursion leading to stack exhaustion.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/674.html
