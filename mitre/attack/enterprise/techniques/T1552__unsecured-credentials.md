---
attack_id: T1552
name: Unsecured Credentials
type: technique
parent: null
tactics: [Credential Access]
platforms: [Windows, SaaS, IaaS, Linux, macOS, Containers, Network Devices, Office Suite, Identity Provider]
url: https://attack.mitre.org/techniques/T1552
tags: [mitre-attack, technique, T1552]
---

# T1552 - Unsecured Credentials

**Tactic(s):** Credential Access  -  **Platforms:** Windows, SaaS, IaaS, Linux, macOS, Containers, Network Devices, Office Suite, Identity Provider  -  **ATT&CK:** [T1552](https://attack.mitre.org/techniques/T1552)

## Summary
Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. [Shell History](https://attack.mitre.org/techniques/T1552/003)), operating system or application-specific repositories (e.g. [Credentials in Registry](https://attack.mitre.org/techniques/T1552/002)),  or other specialized files/artifacts (e.g. [Private Keys](https://attack.mitre.org/techniques/T1552/004)).(Citation: Brining MimiKatz to Unix)

## Role in the attack flow
Used to achieve the **Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows, SaaS, IaaS, Linux, macOS, Containers, Network Devices, Office Suite, Identity Provider.

## Mitigations
- **M1041 Encrypt Sensitive Information** - Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures:
- **M1051 Update Software** - Software updates ensure systems are protected against known vulnerabilities by applying patches and upgrades provided by vendors. Regular updates reduce the attack surface and prevent adversaries from exploiting known security gaps. This includes patching operating systems, applications, drivers, and firmware. This mitigation can be implemented through the following measures:
- **M1017 User Training** - User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures:
- **M1015 Active Directory Configuration** - Implement robust Active Directory (AD) configurations using group policies to secure user accounts, control access, and minimize the attack surface. AD configurations enable centralized control over account settings, logon policies, and permissions, reducing the risk of unauthorized access and lateral movement within the network. This mitigation can be implemented through the following measures:
- **M1027 Password Policies** - Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures:
- **M1028 Operating System Configuration** - Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: 
- **M1037 Filter Network Traffic** - Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:
- **M1022 Restrict File and Directory Permissions** - Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files.
- **M1035 Limit Access to Resource Over Network** - Restrict access to network resources, such as file shares, remote systems, and services, to only those users, accounts, or systems with a legitimate business requirement. This can include employing technologies like network concentrators, RDP gateways, and zero-trust network access (ZTNA) models, alongside hardening services and protocols. This mitigation can be implemented through the following measures:
- **M1047 Audit** - Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.
- **M1026 Privileged Account Management** - Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1552
