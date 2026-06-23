---
cwe_id: CWE-652
name: Improper Neutralization of Data within XQuery Expressions ('XQuery Injection')
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/652.html
tags: [mitre-cwe, weakness, CWE-652]
---

# CWE-652 - Improper Neutralization of Data within XQuery Expressions ('XQuery Injection')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-652](https://cwe.mitre.org/data/definitions/652.html)

## Description
The product uses external input to dynamically construct an XQuery expression used to retrieve data from an XML database, but it does not neutralize or incorrectly neutralizes that input. This allows an attacker to control the structure of the query.

## Extended description
The net effect is that the attacker will have control over the information selected from the XML database and may use that ability to control application flow, modify logic, retrieve unauthorized data, or bypass important checks (e.g. authentication).

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Use parameterized queries. This will help ensure separation between data plane and control plane.
- **Implementation**: Properly validate user input. Reject data where appropriate, filter where appropriate and escape where appropriate. Make sure input that will be used in XQL queries is safe in that context.

## Related weaknesses
- CWE-943 (ChildOf)
- CWE-91 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/652.html
