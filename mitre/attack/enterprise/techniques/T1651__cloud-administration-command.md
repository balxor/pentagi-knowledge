---
attack_id: T1651
name: Cloud Administration Command
type: technique
parent: null
tactics: [Execution]
platforms: [IaaS]
url: https://attack.mitre.org/techniques/T1651
tags: [mitre-attack, technique, T1651]
---

# T1651 - Cloud Administration Command

**Tactic(s):** Execution  ·  **Platforms:** IaaS  ·  **ATT&CK:** [T1651](https://attack.mitre.org/techniques/T1651)

## Summary
Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. (Citation: AWS Systems Manager Run Command)(Citation: Microsoft Run Command)

If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider or delegated administrator account may similarly be able to leverage a [Trusted Relationship](https://attack.mitre.org/techniques/T1199) to execute commands in connected virtual machines.(Citation: MSTIC Nobelium Oct 2021)

## Role in the attack flow
Used to achieve the **Execution** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: IaaS.

## Mitigations
- **M1026 Privileged Account Management** - Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1651
