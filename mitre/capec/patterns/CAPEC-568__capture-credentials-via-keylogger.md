---
capec_id: CAPEC-568
name: Capture Credentials via Keylogger
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: []
related_attack: [T1056.001]
url: https://capec.mitre.org/data/definitions/568.html
tags: [mitre-capec, attack-pattern, CAPEC-568]
---

# CAPEC-568 - Capture Credentials via Keylogger

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-568](https://capec.mitre.org/data/definitions/568.html)

## Description
An adversary deploys a keylogger in an effort to obtain credentials directly from a system's user. After capturing all the keystrokes made by a user, the adversary can analyze the data and determine which string are likely to be passwords or other credential related information.

## Prerequisites
- The ability to install the keylogger, either in person or remote.

## Execution flow
Execution Flow Explore Determine which user's credentials to capture: Since this is a more targeted attack, an adversary will first identify a particular user they wish the capture the credentials of. Experiment Deploy keylogger: Once a user is identified, an adversary will deploy a keylogger to the user's system in one of many ways. Techniques Send a phishing email with a malicious attachment that installs a keylogger on a user's system Conceal a keylogger behind fake software and get the user to download the software Get a user to click on a malicious URL that directs them to a webpage that will install a keylogger without their knowledge Gain access to the user's system through a vulnerability and manually install a keylogger Record keystrokes: Once the keylogger is deployed on the user's system, the adversary will record keystrokes over a period of time. Analyze data and determine credentials: Using the captured keystrokes, the adversary will be able to determine the credentials of the user. Techniques Search for repeated sequences that are following by the enter key Search for repeated sequences that are not found in a dictionary Search for several backspaces in a row. This could indicate a mistyped password. The correct password can then be inferred using the whole key sequence Exploit Use found credentials: After the adversary has found the credentials for the target user, they will then use them to gain access to a system in order to perform some follow-up attack

## Mitigations
- Strong physical security can help reduce the ability of an adversary to install a keylogger.

## Related ATT&CK techniques
- T1056.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/568.html
