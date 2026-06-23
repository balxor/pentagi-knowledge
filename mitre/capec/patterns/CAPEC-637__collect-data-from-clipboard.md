---
capec_id: CAPEC-637
name: Collect Data from Clipboard
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Low
related_cwe: [CWE-267]
related_attack: [T1115]
url: https://capec.mitre.org/data/definitions/637.html
tags: [mitre-capec, attack-pattern, CAPEC-637]
---

# CAPEC-637 - Collect Data from Clipboard

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-637](https://capec.mitre.org/data/definitions/637.html)

## Description
The adversary exploits an application that allows for the copying of sensitive data or information by collecting information copied to the clipboard. Data copied to the clipboard can be accessed by other applications, such as malware built to exfiltrate or log clipboard contents on a periodic basis. In this way, the adversary aims to garner information to which they are unauthorized.

## Prerequisites
- The adversary must have a means (i.e., a pre-installed tool or background process) by which to collect data from the clipboard and store it. That is, when the target copies data to the clipboard (e.g., to paste into another application), the adversary needs some means of capturing that data in a third location.

## Skills required
- **High**: To deploy a hidden process or malware on the system to automatically collect clipboard data.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Find an application that allows copying sensititve data to clipboad: An adversary first needs to find an application that allows copying and pasting of sensitive information. This could be an application that prints out temporary passwords to the screen, private email addresses, or any other sensitive information or data Experiment Target users of the application: An adversary will target users of the application in order to obtain the information in their clipboard on a periodic basic Techniques Install malware on a user's system designed to log clipboard contents periodically Get the user to click on a malicious link that will bring them to an application to log the contents of the clipboard Exploit Follow-up attack: Use any sensitive information found to carry out a follow-up attack

## Mitigations
- While copying and pasting of data with the clipboard is a legitimate and practical function, certain situations and context may require the disabling of this feature. Just as certain applications disable screenshot capability, applications that handle highly sensitive information should consider disabling copy and paste functionality.
- Employ a robust identification and audit/blocking via using an allowlist of applications on your system. Malware may contain the functionality associated with this attack pattern.

## Related weaknesses (CWE)
- [CWE-267](https://cwe.mitre.org/data/definitions/267.html)

## Related ATT&CK techniques
- T1115

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/637.html
