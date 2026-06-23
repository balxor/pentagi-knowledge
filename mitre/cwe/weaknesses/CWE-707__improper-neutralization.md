---
cwe_id: CWE-707
name: Improper Neutralization
type: weakness
abstraction: Pillar
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-250, CAPEC-276, CAPEC-277, CAPEC-278, CAPEC-279, CAPEC-3, CAPEC-43, CAPEC-468, CAPEC-52, CAPEC-53, CAPEC-64, CAPEC-7, CAPEC-78, CAPEC-79, CAPEC-83, CAPEC-84]
url: https://cwe.mitre.org/data/definitions/707.html
tags: [mitre-cwe, weakness, CWE-707]
---

# CWE-707 - Improper Neutralization

**Abstraction:** Pillar  -  **Status:** Incomplete  -  **CWE:** [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

## Description
The product does not ensure or incorrectly ensures that structured messages or data are well-formed and that certain security properties are met before being read from an upstream component or sent to a downstream component.

## Extended description
If a message is malformed, it may cause the message to be incorrectly interpreted. Neutralization is an abstract term for any technique that ensures that input (and output) conforms with expectations and is "safe." This can be done by: checking that the input/output is already "safe" (e.g. validation) transformation of the input/output to be "safe" using techniques such as filtering, encoding/decoding, escaping/unescaping, quoting/unquoting, or canonicalization preventing the input/output from being directly provided by an attacker (e.g. "indirect selection" that maps externally-provided values to internally-controlled values) preventing the input/output from being processed at all This weakness typically applies in cases where the product prepares a control message that another process must act on, such as a command or query, and malicious input that was intended as data, can enter the control plane instead. However, this weakness also applies to more general cases where there are not always control implications.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Other**: Other

## Related attack patterns (CAPEC)
- [CAPEC-250](https://capec.mitre.org/data/definitions/250.html)
- [CAPEC-276](https://capec.mitre.org/data/definitions/276.html)
- [CAPEC-277](https://capec.mitre.org/data/definitions/277.html)
- [CAPEC-278](https://capec.mitre.org/data/definitions/278.html)
- [CAPEC-279](https://capec.mitre.org/data/definitions/279.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-468](https://capec.mitre.org/data/definitions/468.html)
- [CAPEC-52](https://capec.mitre.org/data/definitions/52.html)
- [CAPEC-53](https://capec.mitre.org/data/definitions/53.html)
- [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
- [CAPEC-7](https://capec.mitre.org/data/definitions/7.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
- [CAPEC-83](https://capec.mitre.org/data/definitions/83.html)
- [CAPEC-84](https://capec.mitre.org/data/definitions/84.html)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/707.html
