---
attack_id: T1554
name: Compromise Host Software Binary
type: technique
parent: null
tactics: [Persistence]
platforms: [ESXi, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1554
tags: [mitre-attack, technique, T1554]
---

# T1554 - Compromise Host Software Binary

**Tactic(s):** Persistence  -  **Platforms:** ESXi, Linux, macOS, Windows  -  **ATT&CK:** [T1554](https://attack.mitre.org/techniques/T1554)

## Summary
Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.

Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., [Modify Authentication Process](https://attack.mitre.org/techniques/T1556)).(Citation: Google Cloud Mandiant UNC3886 2024)

An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching)(Citation: Unit42 Banking Trojans Hooking 2022) prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.(Citation: ESET FontOnLake Analysis 2021)

After modifying a binary, an adversary may attempt to impair defenses by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).(Citation: Google Cloud Mandiant UNC3886 2024)

## Role in the attack flow
Used to achieve the **Persistence** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Windows.

## Mitigations
- **M1045 Code Signing** - Code Signing is a security process that ensures the authenticity and integrity of software by digitally signing executables, scripts, and other code artifacts. It prevents untrusted or malicious code from executing by verifying the digital signatures against trusted sources. Code signing protects against tampering, impersonation, and distribution of unauthorized or malicious software, forming a critical defense against supply chain and software exploitation attacks. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1554
