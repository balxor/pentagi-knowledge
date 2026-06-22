---
attack_id: T1534
name: Internal Spearphishing
type: technique
parent: null
tactics: [Lateral Movement]
platforms: [Linux, macOS, Office Suite, SaaS, Windows]
url: https://attack.mitre.org/techniques/T1534
tags: [mitre-attack, technique, T1534]
---

# T1534 - Internal Spearphishing

**Tactic(s):** Lateral Movement  -  **Platforms:** Linux, macOS, Office Suite, SaaS, Windows  -  **ATT&CK:** [T1534](https://attack.mitre.org/techniques/T1534)

## Summary
After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating [Impersonation](https://attack.mitre.org/techniques/T1684/001).(Citation: Trend Micro - Int SP)

For example, adversaries may leverage [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001) or [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002) as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through [Input Capture](https://attack.mitre.org/techniques/T1056) on sites that mimic login interfaces.

Adversaries may also leverage internal chat apps, such as Microsoft Teams, to spread malicious content or engage users in attempts to capture sensitive information and/or credentials.(Citation: Int SP - chat apps)

## Role in the attack flow
Used to achieve the **Lateral Movement** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Office Suite, SaaS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1534
