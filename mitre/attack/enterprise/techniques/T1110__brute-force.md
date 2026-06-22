---
attack_id: T1110
name: Brute Force
type: technique
parent: null
tactics: [Credential Access]
platforms: [Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows]
url: https://attack.mitre.org/techniques/T1110
tags: [mitre-attack, technique, T1110]
---

# T1110 - Brute Force

**Tactic(s):** Credential Access  -  **Platforms:** Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  -  **ATT&CK:** [T1110](https://attack.mitre.org/techniques/T1110)

## Summary
Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained.(Citation: TrendMicro Pawn Storm Dec 2020) Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism.(Citation: Dragos Crashoverride 2018) Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes.

Brute forcing credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access to [Valid Accounts](https://attack.mitre.org/techniques/T1078) within a victim environment leveraging knowledge gathered from other post-compromise behaviors such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), [Account Discovery](https://attack.mitre.org/techniques/T1087), or [Password Policy Discovery](https://attack.mitre.org/techniques/T1201). Adversaries may also combine brute forcing activity with behaviors such as [External Remote Services](https://attack.mitre.org/techniques/T1133) as part of Initial Access. 

If an adversary guesses the correct password but fails to login to a compromised account due to location-based conditional access policies, they may change their infrastructure until they match the victim’s location and therefore bypass those policies.(Citation: ReliaQuest Health Care Social Engineering Campaign 2024)

## Role in the attack flow
Used to achieve the **Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows.

## Mitigations
- **M1018 User Account Management** - User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures:
- **M1036 Account Use Policies** - Account Use Policies help mitigate unauthorized access by configuring and enforcing rules that govern how and when accounts can be used. These policies include enforcing account lockout mechanisms, restricting login times, and setting inactivity timeouts. Proper configuration of these policies reduces the risk of brute-force attacks, credential theft, and unauthorized access by limiting the opportunities for malicious actors to exploit accounts. This mitigation can be implemented through the following measures:
- **M1032 Multi-factor Authentication** - Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification to prove their identity before granting access. These factors typically include:
- **M1027 Password Policies** - Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1110
