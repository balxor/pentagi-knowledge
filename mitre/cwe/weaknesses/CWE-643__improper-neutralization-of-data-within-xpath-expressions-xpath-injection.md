---
cwe_id: CWE-643
name: Improper Neutralization of Data within XPath Expressions ('XPath Injection')
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/643.html
tags: [mitre-cwe, weakness, CWE-643]
---

# CWE-643 - Improper Neutralization of Data within XPath Expressions ('XPath Injection')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-643](https://cwe.mitre.org/data/definitions/643.html)

## Description
The product uses external input to dynamically construct an XPath expression used to retrieve data from an XML database, but it does not neutralize or incorrectly neutralizes that input. This allows an attacker to control the structure of the query.

## Extended description
The net effect is that the attacker will have control over the information selected from the XML database and may use that ability to control application flow, modify logic, retrieve unauthorized data, or bypass important checks (e.g. authentication).

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Use parameterized XPath queries (e.g. using XQuery). This will help ensure separation between data plane and control plane.
- **Implementation**: Properly validate user input. Reject data where appropriate, filter where appropriate and escape where appropriate. Make sure input that will be used in XPath queries is safe in that context.

## Related weaknesses
- CWE-943 (ChildOf)
- CWE-91 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/643.html
