---
cwe_id: CWE-506
name: Embedded Malicious Code
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-442, CAPEC-448, CAPEC-636]
url: https://cwe.mitre.org/data/definitions/506.html
tags: [mitre-cwe, weakness, CWE-506]
---

# CWE-506 - Embedded Malicious Code

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-506](https://cwe.mitre.org/data/definitions/506.html)

## Description
The product contains code that appears to be malicious in nature.

## Extended description
Malicious flaws have acquired colorful names, including Trojan horse, trapdoor, timebomb, and logic-bomb. A developer might insert malicious code with the intent to subvert the security of a product or its host system at some time in the future. It generally refers to a program that performs a useful service but exploits rights of the program's user in a way the user does not intend.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation, Operation**: Remove the malicious code and start an effort to ensure that no more malicious code exists. This may require a detailed review of all code, as it is possible to hide a serious attack in only one or two lines of code. These lines may be located almost anywhere in an application and may have been intentionally obfuscated by the attacker.

## Related attack patterns (CAPEC)
- [CAPEC-442](https://capec.mitre.org/data/definitions/442.html)
- [CAPEC-448](https://capec.mitre.org/data/definitions/448.html)
- [CAPEC-636](https://capec.mitre.org/data/definitions/636.html)

## Related weaknesses
- CWE-912 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30877**: A command history tool was shipped with a code-execution backdoor inserted by a malicious party.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/506.html
