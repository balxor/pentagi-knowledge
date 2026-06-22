---
attack_id: T1615
name: Group Policy Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Windows]
url: https://attack.mitre.org/techniques/T1615
tags: [mitre-attack, technique, T1615]
---

# T1615 - Group Policy Discovery

**Tactic(s):** Discovery  ·  **Platforms:** Windows  ·  **ATT&CK:** [T1615](https://attack.mitre.org/techniques/T1615)

## Summary
Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence 2016)

Adversaries may use commands such as <code>gpresult</code> or various publicly available PowerShell functions, such as <code>Get-DomainGPO</code> and <code>Get-DomainGPOLocalGroup</code>, to gather information on Group Policy settings.(Citation: Microsoft gpresult)(Citation: Github PowerShell Empire) Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. [Domain or Tenant Policy Modification](https://attack.mitre.org/techniques/T1484)) for their benefit.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1615
