---
attack_id: T1059
name: Command and Scripting Interpreter
type: technique
parent: null
tactics: [Execution]
platforms: [Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows]
url: https://attack.mitre.org/techniques/T1059
tags: [mitre-attack, technique, T1059]
---

# T1059 - Command and Scripting Interpreter

**Tactic(s):** Execution  -  **Platforms:** Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  -  **ATT&CK:** [T1059](https://attack.mitre.org/techniques/T1059)

## Summary
Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions include some flavor of [Unix Shell](https://attack.mitre.org/techniques/T1059/004) while Windows installations include the [Windows Command Shell](https://attack.mitre.org/techniques/T1059/003) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

There are also cross-platform interpreters such as [Python](https://attack.mitre.org/techniques/T1059/006), as well as those commonly associated with client applications such as [JavaScript](https://attack.mitre.org/techniques/T1059/007) and [Visual Basic](https://attack.mitre.org/techniques/T1059/005).

Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in [Initial Access](https://attack.mitre.org/tactics/TA0001) payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells, as well as utilize various [Remote Services](https://attack.mitre.org/techniques/T1021) in order to achieve remote Execution.(Citation: Powershell Remote Commands)(Citation: Cisco IOS Software Integrity Assurance - Command History)(Citation: Remote Shell Execution in Python)

## Role in the attack flow
Used to achieve the **Execution** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows.

## Mitigations
- **M1033 Limit Software Installation** - Prevent users or groups from installing unauthorized or unapproved software to reduce the risk of introducing malicious or vulnerable applications. This can be achieved through allowlists, software restriction policies, endpoint management tools, and least privilege access principles. This mitigation can be implemented through the following measures:
- **M1045 Code Signing** - Code Signing is a security process that ensures the authenticity and integrity of software by digitally signing executables, scripts, and other code artifacts. It prevents untrusted or malicious code from executing by verifying the digital signatures against trusted sources. Code signing protects against tampering, impersonation, and distribution of unauthorized or malicious software, forming a critical defense against supply chain and software exploitation attacks. This mitigation can be implemented through the following measures:
- **M1042 Disable or Remove Feature or Program** - Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: 
- **M1038 Execution Prevention** - Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:
- **M1049 Antivirus/Antimalware** - Antivirus/Antimalware solutions utilize signatures, heuristics, and behavioral analysis to detect, block, and remediate malicious software, including viruses, trojans, ransomware, and spyware. These solutions continuously monitor endpoints and systems for known malicious patterns and suspicious behaviors that indicate compromise. Antivirus/Antimalware software should be deployed across all devices, with automated updates to ensure protection against the latest threats. This mitigation can be implemented through the following measures:
- **M1026 Privileged Account Management** - Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:
- **M1047 Audit** - Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.
- **M1021 Restrict Web-Based Content** - Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures:
- **M1040 Behavior Prevention on Endpoint** - Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1059
