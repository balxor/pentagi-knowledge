---
cwe_id: CWE-589
name: Call to Non-ubiquitous API
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-96]
url: https://cwe.mitre.org/data/definitions/589.html
tags: [mitre-cwe, weakness, CWE-589]
---

# CWE-589 - Call to Non-ubiquitous API

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-589](https://cwe.mitre.org/data/definitions/589.html)

## Description
The product uses an API function that does not exist on all versions of the target platform. This could cause portability problems or inconsistencies that allow denial of service or other consequences.

## Extended description
Some functions that offer security features supported by the OS are not available on all versions of the OS in common use. Likewise, functions are often deprecated or made obsolete for security reasons and should not be used.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: Always test your code on any platform on which it is targeted to run on.
- **Testing**: Test your code on the newest and oldest platform on which it is targeted to run on.
- **Testing**: Develop a system to test for API functions that are not portable.

## Related attack patterns (CAPEC)
- [CAPEC-96](https://capec.mitre.org/data/definitions/96.html)

## Related weaknesses
- CWE-474 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/589.html
