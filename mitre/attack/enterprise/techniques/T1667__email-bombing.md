---
attack_id: T1667
name: Email Bombing
type: technique
parent: null
tactics: [Impact]
platforms: [Linux, Office Suite, Windows, macOS]
url: https://attack.mitre.org/techniques/T1667
tags: [mitre-attack, technique, T1667]
---

# T1667 - Email Bombing

**Tactic(s):** Impact  -  **Platforms:** Linux, Office Suite, Windows, macOS  -  **ATT&CK:** [T1667](https://attack.mitre.org/techniques/T1667)

## Summary
Adversaries may flood targeted email addresses with an overwhelming volume of messages. This may bury legitimate emails in a flood of spam and disrupt business operations.(Citation: sophos-bombing)(Citation: krebs-email-bombing)

An adversary may accomplish email bombing by leveraging an automated bot to register a targeted address for e-mail lists that do not validate new signups, such as online newsletters. The result can be a wave of thousands of e-mails that effectively overloads the victim’s inbox.(Citation: krebs-email-bombing)(Citation: hhs-email-bombing)

By sending hundreds or thousands of e-mails in quick succession, adversaries may successfully divert attention away from and bury legitimate messages including security alerts, daily business processes like help desk tickets and client correspondence, or ongoing scams.(Citation: hhs-email-bombing) This behavior can also be used as a tool of harassment.(Citation: krebs-email-bombing)

This behavior may be a precursor for [Spearphishing Voice](https://attack.mitre.org/techniques/T1566/004). For example, an adversary may email bomb a target and then follow up with a phone call to fraudulently offer assistance. This social engineering may lead to the use of [Remote Access Software](https://attack.mitre.org/techniques/T1663) to steal credentials, deploy ransomware, conduct [Financial Theft](https://attack.mitre.org/techniques/T1657)(Citation: sophos-bombing), or engage in other malicious activity.(Citation: rapid7-email-bombing)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, Office Suite, Windows, macOS.

## Mitigations
- **M1017 User Training** - User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures:
- **M1054 Software Configuration** - Software configuration refers to making security-focused adjustments to the settings of applications, middleware, databases, or other software to mitigate potential threats. These changes help reduce the attack surface, enforce best practices, and protect sensitive data. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1667
