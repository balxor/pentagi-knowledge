---
cwe_id: CWE-74
name: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-10, CAPEC-101, CAPEC-105, CAPEC-108, CAPEC-120, CAPEC-13, CAPEC-135, CAPEC-14, CAPEC-24, CAPEC-250, CAPEC-267, CAPEC-273, CAPEC-28, CAPEC-3, CAPEC-34, CAPEC-42, CAPEC-43, CAPEC-45, CAPEC-46, CAPEC-47, CAPEC-51, CAPEC-52, CAPEC-53, CAPEC-6, CAPEC-64, CAPEC-67, CAPEC-7, CAPEC-71, CAPEC-72, CAPEC-76, CAPEC-78, CAPEC-79, CAPEC-8, CAPEC-80, CAPEC-83, CAPEC-84, CAPEC-9]
url: https://cwe.mitre.org/data/definitions/74.html
tags: [mitre-cwe, weakness, CWE-74]
---

# CWE-74 - Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

## Description
The product constructs all or part of a command, data structure, or record using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify how it is parsed or interpreted when it is sent to a downstream component.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data
- **Access Control**: Bypass Protection Mechanism
- **Other**: Alter Execution Logic
- **Integrity, Other**: Other
- **Non-Repudiation**: Hide Activities

## Potential mitigations
- **Requirements**: Programming languages and supporting technologies might be chosen which are not subject to these issues.
- **Implementation**: Utilize an appropriate mix of allowlist and denylist parsing to filter control-plane syntax from all input.

## Related attack patterns (CAPEC)
- [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
- [CAPEC-101](https://capec.mitre.org/data/definitions/101.html)
- [CAPEC-105](https://capec.mitre.org/data/definitions/105.html)
- [CAPEC-108](https://capec.mitre.org/data/definitions/108.html)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
- [CAPEC-135](https://capec.mitre.org/data/definitions/135.html)
- [CAPEC-14](https://capec.mitre.org/data/definitions/14.html)
- [CAPEC-24](https://capec.mitre.org/data/definitions/24.html)
- [CAPEC-250](https://capec.mitre.org/data/definitions/250.html)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-273](https://capec.mitre.org/data/definitions/273.html)
- [CAPEC-28](https://capec.mitre.org/data/definitions/28.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-34](https://capec.mitre.org/data/definitions/34.html)
- [CAPEC-42](https://capec.mitre.org/data/definitions/42.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
- [CAPEC-46](https://capec.mitre.org/data/definitions/46.html)
- [CAPEC-47](https://capec.mitre.org/data/definitions/47.html)
- [CAPEC-51](https://capec.mitre.org/data/definitions/51.html)
- [CAPEC-52](https://capec.mitre.org/data/definitions/52.html)
- [CAPEC-53](https://capec.mitre.org/data/definitions/53.html)
- [CAPEC-6](https://capec.mitre.org/data/definitions/6.html)
- [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
- [CAPEC-67](https://capec.mitre.org/data/definitions/67.html)
- [CAPEC-7](https://capec.mitre.org/data/definitions/7.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
- [CAPEC-72](https://capec.mitre.org/data/definitions/72.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
- [CAPEC-8](https://capec.mitre.org/data/definitions/8.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)
- [CAPEC-83](https://capec.mitre.org/data/definitions/83.html)
- [CAPEC-84](https://capec.mitre.org/data/definitions/84.html)
- [CAPEC-9](https://capec.mitre.org/data/definitions/9.html)

## Related weaknesses
- CWE-707 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-5184**: API service using a large generative AI model allows direct prompt injection to leak hard-coded system prompts or execute other prompts.
- **CVE-2022-36069**: Python-based dependency management tool avoids OS command injection when generating Git commands but allows injection of optional arguments with input beginning with a dash (CWE-88), potentially allowing for code execution.
- **CVE-1999-0067**: Canonical example of OS command injection. CGI program does not neutralize "|" metacharacter when invoking a phonebook program.
- **CVE-2022-1509**: injection of sed script syntax ("sed injection")
- **CVE-2020-9054**: Chain: improper input validation (CWE-20) in username parameter, leading to OS command injection (CWE-78), as exploited in the wild per CISA KEV.
- **CVE-2021-44228**: Product does not neutralize ${xyz} style expressions, allowing remote code execution. (log4shell vulnerability)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/74.html
