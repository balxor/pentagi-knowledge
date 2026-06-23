---
cwe_id: CWE-550
name: Server-generated Error Message Containing Sensitive Information
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/550.html
tags: [mitre-cwe, weakness, CWE-550]
---

# CWE-550 - Server-generated Error Message Containing Sensitive Information

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-550](https://cwe.mitre.org/data/definitions/550.html)

## Description
Certain conditions, such as network failure, will cause a server error message to be displayed.

## Extended description
While error messages in and of themselves are not dangerous, per se, it is what an attacker can glean from them that might cause eventual problems.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design, System Configuration**: Recommendations include designing and adding consistent error handling mechanisms which are capable of handling any user input to your web application, providing meaningful detail to end-users, and preventing error messages that might provide information useful to an attacker from being displayed.

## Related weaknesses
- CWE-209 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/550.html
