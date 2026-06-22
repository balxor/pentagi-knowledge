---
attack_id: T1219
name: Remote Access Tools
type: technique
parent: null
tactics: [Command and Control]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1219
tags: [mitre-attack, technique, T1219]
---

# T1219 - Remote Access Tools

**Tactic(s):** Command and Control  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1219](https://attack.mitre.org/techniques/T1219)

## Summary
An adversary may use legitimate remote access tools to establish an interactive command and control channel within a network. Remote access tools create a session between two trusted hosts through a graphical interface, a command line interaction, a protocol tunnel via development or management software, or hardware-level access such as KVM (Keyboard, Video, Mouse) over IP solutions. Desktop support software (usually graphical interface) and remote management software (typically command line interface) allow a user to control a computer remotely as if they are a local user inheriting the user or software permissions. This software is commonly used for troubleshooting, software installation, and system management.(Citation: Symantec Living off the Land)(Citation: CrowdStrike 2015 Global Threat Report)(Citation: CrySyS Blog TeamSpy) Adversaries may similarly abuse response features included in EDR and other defensive tools that enable remote access.

Remote access tools may be installed and used post-compromise as an alternate communications channel for redundant access or to establish an interactive remote desktop session with the target system. It may also be used as a malware component to establish a reverse connection or back-connect to a service or adversary-controlled system.

Installation of many remote access tools may also include persistence (e.g., the software's installation routine creates a [Windows Service](https://attack.mitre.org/techniques/T1543/003)). Remote access modules/features may also exist as part of otherwise existing software (e.g., Google Chrome’s Remote Desktop).(Citation: Google Chrome Remote Desktop)(Citation: Chrome Remote Desktop)

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1038 Execution Prevention** - Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:
- **M1037 Filter Network Traffic** - Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:
- **M1034 Limit Hardware Installation** - Prevent unauthorized users or groups from installing or using hardware, such as external drives, peripheral devices, or unapproved internal hardware components, by enforcing hardware usage policies and technical controls. This includes disabling USB ports, restricting driver installation, and implementing endpoint security tools to monitor and block unapproved devices. This mitigation can be implemented through the following measures:
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.
- **M1042 Disable or Remove Feature or Program** - Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: 

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1219
