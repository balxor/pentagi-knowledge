---
attack_id: T1555
name: Credentials from Password Stores
type: technique
parent: null
tactics: [Credential Access]
platforms: [IaaS, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1555
tags: [mitre-attack, technique, T1555]
---

# T1555 - Credentials from Password Stores

**Tactic(s):** Credential Access  ·  **Platforms:** IaaS, Linux, macOS, Windows  ·  **ATT&CK:** [T1555](https://attack.mitre.org/techniques/T1555)

## Summary
Adversaries may search for common password storage locations to obtain user credentials.(Citation: F-Secure The Dukes) Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications and services that store passwords to make them easier for users to manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Role in the attack flow
Used to achieve the **Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: IaaS, Linux, macOS, Windows.

## Mitigations
- **M1026 Privileged Account Management** - Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:
- **M1051 Update Software** - Software updates ensure systems are protected against known vulnerabilities by applying patches and upgrades provided by vendors. Regular updates reduce the attack surface and prevent adversaries from exploiting known security gaps. This includes patching operating systems, applications, drivers, and firmware. This mitigation can be implemented through the following measures:
- **M1027 Password Policies** - Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1555
