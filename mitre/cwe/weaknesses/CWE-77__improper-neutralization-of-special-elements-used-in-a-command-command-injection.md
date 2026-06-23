---
cwe_id: CWE-77
name: Improper Neutralization of Special Elements used in a Command ('Command Injection')
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, AI/ML]
related_capec: [CAPEC-136, CAPEC-15, CAPEC-183, CAPEC-248, CAPEC-40, CAPEC-43, CAPEC-75, CAPEC-76]
url: https://cwe.mitre.org/data/definitions/77.html
tags: [mitre-cwe, weakness, CWE-77]
---

# CWE-77 - Improper Neutralization of Special Elements used in a Command ('Command Injection')

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-77](https://cwe.mitre.org/data/definitions/77.html)

## Description
The product constructs all or part of a command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended command when it is sent to a downstream component.

## Extended description
Many protocols and products have their own custom command language. While OS or shell command strings are frequently discovered and targeted, developers may not realize that these other command languages might also be vulnerable to attacks.

## Applicable platforms / languages
Not Language-Specific, AI/ML

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: If at all possible, use library calls rather than external processes to recreate the desired functionality.
- **Implementation**: If possible, ensure that all external commands called from the program are statically created.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Operation**: Run time: Run time policy enforcement may be used in an allowlist fashion to prevent use of any non-sanctioned commands.
- **System Configuration**: Assign permissions that prevent the user from accessing/opening privileged files.

## Related attack patterns (CAPEC)
- [CAPEC-136](https://capec.mitre.org/data/definitions/136.html)
- [CAPEC-15](https://capec.mitre.org/data/definitions/15.html)
- [CAPEC-183](https://capec.mitre.org/data/definitions/183.html)
- [CAPEC-248](https://capec.mitre.org/data/definitions/248.html)
- [CAPEC-40](https://capec.mitre.org/data/definitions/40.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-75](https://capec.mitre.org/data/definitions/75.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)

## Related weaknesses
- CWE-74 (ChildOf)
- CWE-74 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-1509**: injection of sed script syntax ("sed injection")
- **CVE-2024-5184**: API service using a large generative AI model allows direct prompt injection to leak hard-coded system prompts or execute other prompts.
- **CVE-2020-11698**: anti-spam product allows injection of SNMP commands into confiuration file
- **CVE-2019-12921**: image program allows injection of commands in "Magick Vector Graphics (MVG)" language.
- **CVE-2022-36069**: Python-based dependency management tool avoids OS command injection when generating Git commands but allows injection of optional arguments with input beginning with a dash (CWE-88), potentially allowing for code execution.
- **CVE-1999-0067**: Canonical example of OS command injection. CGI program does not neutralize "|" metacharacter when invoking a phonebook program.
- **CVE-2020-9054**: Chain: improper input validation (CWE-20) in username parameter, leading to OS command injection (CWE-78), as exploited in the wild per CISA KEV.
- **CVE-2021-41282**: injection of sed script syntax ("sed injection")
- **CVE-2019-13398**: injection of sed script syntax ("sed injection")

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/77.html
