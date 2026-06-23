---
capec_id: CAPEC-504
name: Task Impersonation
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-1021]
related_attack: [T1036.004]
url: https://capec.mitre.org/data/definitions/504.html
tags: [mitre-capec, attack-pattern, CAPEC-504]
---

# CAPEC-504 - Task Impersonation

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-504](https://capec.mitre.org/data/definitions/504.html)

## Description
An adversary, through a previously installed malicious application, impersonates an expected or routine task in an attempt to steal sensitive information or leverage a user's privileges.

## Extended description
When impersonating an expected task, the adversary monitors the task list maintained by the operating system and waits for a specific legitimate task to become active. Once the task is detected, the malicious application launches a new task in the foreground that mimics the user interface of the legitimate task. At this point, the user thinks that they are interacting with the legitimate task that they started, but instead they are interacting with the malicious application. Once the adversary's goal is reached, the malicious application can exit, leaving the original trusted application visible and the appearance that nothing out of the ordinary has occurred. A second approach entails the adversary impersonating an unexpected task, but one that may often be spawned by legitimate background processes. For example, an adversary may randomly impersonate a system credential prompt, implying that a background process requires authentication for some purpose. The user, believing they are interacting with a legitimate task, enters their credentials or authorizes the use of their stored credentials, which the adversary then leverages for nefarious purposes. This type of attack is most often used to obtain sensitive information (e.g., credentials) from the user, but may also be used to ride the user's privileges.

## Prerequisites
- The adversary must already have access to the target system via some means.
- A legitimate task must exist that an adversary can impersonate to glean credentials.
- The user's privileges allow them to execute certain tasks with elevated privileges.

## Skills required
- **Low**: Once an adversary has gained access to the target system, impersonating a task is trivial.

## Resources required
- Malware or some other means to initially comprise the target system.
- Additional malware to impersonate a legitimate task.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges

## Execution flow
Execution Flow Explore Determine suitable tasks to exploit: Determine what tasks exist on the target system that may result in a user providing sensitive information. Techniques Determine what tasks prompt a user for their credentials. Determine what tasks may prompt a user to authorize a process to execute with elevated privileges. Exploit Impersonate Task: Impersonate a legitimate task, either expected or unexpected, in an attempt to gain user credentials or to ride the user's privileges. Techniques Prompt a user for their credentials, while making the user believe the credential request is legitimate. Prompt a user to authorize a task to run with elevated privileges, while making the user believe the request is legitimate.

## Mitigations
- The only known mitigation to this attack is to avoid installing the malicious application on the device. However, to impersonate a running task the malicious application does need the GET_TASKS permission to be able to query the task list, and being suspicious of applications with that permission can help.

## Related weaknesses (CWE)
- [CWE-1021](https://cwe.mitre.org/data/definitions/1021.html)

## Related ATT&CK techniques
- T1036.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/504.html
