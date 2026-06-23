---
capec_id: CAPEC-137
name: Parameter Injection
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: Medium
related_cwe: [CWE-88]
related_attack: []
url: https://capec.mitre.org/data/definitions/137.html
tags: [mitre-capec, attack-pattern, CAPEC-137]
---

# CAPEC-137 - Parameter Injection

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-137](https://capec.mitre.org/data/definitions/137.html)

## Description
An adversary manipulates the content of request parameters for the purpose of undermining the security of the target. Some parameter encodings use text characters as separators. For example, parameters in a HTTP GET message are encoded as name-value pairs separated by an ampersand (&). If an attacker can supply text strings that are used to fill in these parameters, then they can inject special characters used in the encoding scheme to add or modify parameters. For example, if user input is fed directly into an HTTP GET request and the user provides the value "myInput&new_param=myValue", then the input parameter is set to myInput, but a new parameter (new_param) is also added with a value of myValue. This can significantly change the meaning of the query that is processed by the server. Any encoding scheme where parameters are identified and separated by text characters is potentially vulnerable to this attack - the HTTP GET encoding used above is just one example.

## Prerequisites
- The target application must use a parameter encoding where separators and parameter identifiers are expressed in regular text.
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in the parameter encoding, and insert the user-supplied string in an encoding which is then processed.

## Resources required
- None: No specialized resources are required to execute this type of attack. The only requirement is the ability to provide string input to the target.

## Consequences
- **Integrity**: Modify Data (Successful parameter injection attacks mean a compromise to integrity of the application.)

## Mitigations
- Implement an audit log written to a separate host. In the event of a compromise, the audit log may be able to provide evidence and details of the compromise.
- Treat all user input as untrusted data that must be validated before use.

## Related weaknesses (CWE)
- [CWE-88](https://cwe.mitre.org/data/definitions/88.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/137.html
