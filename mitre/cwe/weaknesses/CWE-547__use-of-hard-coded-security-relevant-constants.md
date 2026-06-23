---
cwe_id: CWE-547
name: Use of Hard-coded, Security-relevant Constants
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/547.html
tags: [mitre-cwe, weakness, CWE-547]
---

# CWE-547 - Use of Hard-coded, Security-relevant Constants

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-547](https://cwe.mitre.org/data/definitions/547.html)

## Description
The product uses hard-coded constants instead of symbolic names for security-critical values, which increases the likelihood of mistakes during code maintenance or security policy change.

## Extended description
If the developer does not find all occurrences of the hard-coded constants, an incorrect policy decision may be made if one of the constants is not changed. Making changes to these values will require code changes that may be difficult or impossible once the system is released to the field. In addition, these hard-coded values may become available to attackers if the code is ever disclosed.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context, Quality Degradation, Reduce Maintainability

## Potential mitigations
- **Implementation**: Avoid using hard-coded constants. Configuration files offer a more flexible solution.

## Related weaknesses
- CWE-1078 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/547.html
