---
attack_id: T1662
name: Data Destruction
type: technique
parent: null
tactics: [Impact]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1662
tags: [mitre-attack, technique, T1662]
---

# T1662 - Data Destruction

**Tactic(s):** Impact  -  **Platforms:** Android  -  **ATT&CK:** [T1662](https://attack.mitre.org/techniques/T1662)

## Summary
Adversaries may destroy data and files on specific devices or in large numbers to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.  

To achieve data destruction, adversaries may use the `pm uninstall` command to uninstall packages or the `rm` command to remove specific files. For example, adversaries may first use `pm uninstall` to uninstall non-system apps, and then use `rm (-f) <file(s)>` to delete specific files, further hiding malicious activity.(Citation: rootnik_rooting_tool)(Citation: abuse_native_linux_tools)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1662
