---
capec_id: CAPEC-654
name: Credential Prompt Impersonation
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-1021]
related_attack: [T1056, T1548.004]
url: https://capec.mitre.org/data/definitions/654.html
tags: [mitre-capec, attack-pattern, CAPEC-654]
---

# CAPEC-654 - Credential Prompt Impersonation

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-654](https://capec.mitre.org/data/definitions/654.html)

## Description
An adversary, through a previously installed malicious application, impersonates a credential prompt in an attempt to steal a user's credentials.

## Extended description
The adversary may monitor the task list maintained by the operating system and wait for a specific legitimate credential prompt to become active. Once the prompt is detected, the adversary launches a new credential prompt in the foreground that mimics the user interface of the legitimate credential prompt. At this point, the user thinks that they are interacting with the legitimate credential prompt, but instead they are interacting with the malicious credential prompt. A second approach involves the adversary impersonating an unexpected credential prompt, but one that may often be spawned by legitimate background processes. For example, an adversary may randomly impersonate a system credential prompt, implying that a background process or commonly used application (e.g., email reader) requires authentication for some purpose. The user, believing they are interacting with a legitimate credential prompt, enters their credentials which the adversary then leverages for nefarious purposes. The ultimate goal of this attack is to obtain sensitive information (e.g., credentials) from the user.

## Prerequisites
- The adversary must already have access to the target system via some means.
- A legitimate task must exist that an adversary can impersonate to glean credentials.

## Skills required
- **Low**: Once an adversary has gained access to the target system, impersonating a credential prompt is not difficult.

## Resources required
- Malware or some other means to initially comprise the target system.
- Additional malware to impersonate a legitimate credential prompt.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges

## Execution flow
Execution Flow Explore Determine suitable tasks to exploit: Determine what tasks exist on the target system that may result in a user providing their credentials. Techniques Determine what tasks prompt a user for their credentials. Exploit Impersonate Task: Impersonate a legitimate task, either expected or unexpected, in an attempt to gain user credentials. Techniques Prompt a user for their credentials, while making the user believe the credential request is legitimate.

## Mitigations
- The only known mitigation to this attack is to avoid installing the malicious application on the device. However, to impersonate a running task the malicious application does need the GET_TASKS permission to be able to query the task list, and being suspicious of applications with that permission can help.

## Related weaknesses (CWE)
- [CWE-1021](https://cwe.mitre.org/data/definitions/1021.html)

## Related ATT&CK techniques
- T1056
- T1548.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/654.html
