---
attack_id: T1003
name: OS Credential Dumping
type: technique
parent: null
tactics: [Credential Access]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1003
tags: [mitre-attack, technique, T1003]
---

# T1003 - OS Credential Dumping

**Tactic(s):** Credential Access  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1003](https://attack.mitre.org/techniques/T1003)

## Summary
Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures.(Citation: Brining MimiKatz to Unix) Credentials can then be used to perform [Lateral Movement](https://attack.mitre.org/tactics/TA0008) and access restricted information.

Several of the tools mentioned in associated sub-techniques may be used by both adversaries and professional security testers. Additional custom tools likely exist as well.

## Role in the attack flow
Used to achieve the **Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1041 Encrypt Sensitive Information** - Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures:
- **M1040 Behavior Prevention on Endpoint** - Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures:
- **M1027 Password Policies** - Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures:
- **M1017 User Training** - User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures:
- **M1026 Privileged Account Management** - Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:
- **M1025 Privileged Process Integrity** - Privileged Process Integrity focuses on defending highly privileged processes (e.g., system services, antivirus, or authentication processes) from tampering, injection, or compromise by adversaries. These processes often interact with critical components, making them prime targets for techniques like code injection, privilege escalation, and process manipulation. This mitigation can be implemented through the following measures:
- **M1043 Credential Access Protection** - Credential Access Protection focuses on implementing measures to prevent adversaries from obtaining credentials, such as passwords, hashes, tokens, or keys, that could be used for unauthorized access. This involves restricting access to credential storage mechanisms, hardening configurations to block credential dumping methods, and using monitoring tools to detect suspicious credential-related activity. This mitigation can be implemented through the following measures:
- **M1015 Active Directory Configuration** - Implement robust Active Directory (AD) configurations using group policies to secure user accounts, control access, and minimize the attack surface. AD configurations enable centralized control over account settings, logon policies, and permissions, reducing the risk of unauthorized access and lateral movement within the network. This mitigation can be implemented through the following measures:
- **M1028 Operating System Configuration** - Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: 

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1003
