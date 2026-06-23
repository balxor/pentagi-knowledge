---
capec_id: CAPEC-52
name: Embedding NULL Bytes
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-158, CWE-172, CWE-173, CWE-74, CWE-20, CWE-697, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/52.html
tags: [mitre-capec, attack-pattern, CAPEC-52]
---

# CAPEC-52 - Embedding NULL Bytes

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-52](https://capec.mitre.org/data/definitions/52.html)

## Description
An adversary embeds one or more null bytes in input to the target software. This attack relies on the usage of a null-valued byte as a string terminator in many environments. The goal is for certain components of the target software to stop processing the input when it encounters the null byte(s).

## Prerequisites
- The program does not properly handle postfix NULL terminators

## Skills required
- **High**: Execution of arbitrary code
- **Medium**: Directory traversal

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser, an automated tool or by inspecting the application, an adversary records all entry points to the application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Manually inspect the application to find entry points. Experiment Probe entry points to locate vulnerabilities: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects postfix null byte(s) to observe how the application handles them as input. The adversary is looking for areas where user input is placed in the middle of a string, and the null byte causes the application to stop processing the string at the end of the user input. Techniques Try different encodings for null such as \0 or %00 Exploit Remove data after null byte(s): After determined entry points that are vulnerable, the adversary places a null byte(s) such that they remove data after the null byte(s) in a way that is beneficial to them. Techniques If the input is a directory as part of a longer file path, add a null byte(s) at the end of the input to try to traverse to the given directory.

## Mitigations
- Properly handle the NULL characters supplied as part of user input prior to doing anything with the data.

## Related weaknesses (CWE)
- [CWE-158](https://cwe.mitre.org/data/definitions/158.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/52.html
