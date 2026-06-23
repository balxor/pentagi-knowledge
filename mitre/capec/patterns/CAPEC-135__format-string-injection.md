---
capec_id: CAPEC-135
name: Format String Injection
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-134, CWE-20, CWE-74]
related_attack: []
url: https://capec.mitre.org/data/definitions/135.html
tags: [mitre-capec, attack-pattern, CAPEC-135]
---

# CAPEC-135 - Format String Injection

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-135](https://capec.mitre.org/data/definitions/135.html)

## Description
An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.

## Prerequisites
- The target application must accept a strings as user input, fail to sanitize string formatting characters in the user input, and process this string using functions that interpret string formatting characters.

## Skills required
- **High**: In order to discover format string vulnerabilities it takes only low skill, however, converting this discovery into a working exploit requires advanced knowledge on the part of the adversary.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey application: The adversary takes an inventory of the entry points of the application. Techniques Spider web sites for all available links List parameters, external variables, configuration files variables, etc. that are possibly used by the application. Experiment Determine user-controllable input susceptible to format string injection: Determine the user-controllable input susceptible to format string injection. For each user-controllable input that the adversary suspects is vulnerable to format string injection, attempt to inject formatting characters such as %n, %s, etc.. The goal is to manipulate the string creation using these formatting characters. Techniques Inject probe payload which contains formatting characters (%s, %d, %n, etc.) through input parameters. Exploit Try to exploit the Format String Injection vulnerability: After determining that a given input is vulnerable to format string injection, hypothesize what the underlying usage looks like and the associated constraints. Techniques Insert various formatting characters to read or write the memory, e.g. overwrite return address, etc.

## Mitigations
- Limit the usage of formatting string functions.
- Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.

## Related weaknesses (CWE)
- [CWE-134](https://cwe.mitre.org/data/definitions/134.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/135.html
