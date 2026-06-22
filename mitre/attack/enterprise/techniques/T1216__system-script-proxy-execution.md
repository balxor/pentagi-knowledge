---
attack_id: T1216
name: System Script Proxy Execution
type: technique
parent: null
tactics: [Stealth]
platforms: [Windows]
url: https://attack.mitre.org/techniques/T1216
tags: [mitre-attack, technique, T1216]
---

# T1216 - System Script Proxy Execution

**Tactic(s):** Stealth  ·  **Platforms:** Windows  ·  **ATT&CK:** [T1216](https://attack.mitre.org/techniques/T1216)

## Summary
Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files.(Citation: LOLBAS Project) This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems.(Citation: GitHub Ultimate AppLocker Bypass List)

## Role in the attack flow
Used to achieve the **Stealth** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows.

## Mitigations
- **M1038 Execution Prevention** - Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1216
