---
attack_id: TA0100
name: Collection
type: tactic
shortname: collection
killchain_order: 8
url: https://attack.mitre.org/tactics/TA0100
tags: [mitre-attack, tactic, collection]
---

# TA0100 - Collection (Tactic)

> The adversary is trying to gather data of interest and domain knowledge on your ICS environment to inform their goal.

## Goal
The adversary is trying to gather data of interest and domain knowledge on your ICS environment to inform their goal.

Collection consists of techniques adversaries use to gather domain knowledge and obtain contextual feedback in an ICS environment. This tactic is often performed as part of [Discovery](https://attack.mitre.org/tactics/TA0102), to compile data on control systems and targets of interest that may be used to follow through on the adversary’s objective. Examples of these techniques include observing operation states, capturing screenshots, identifying unique device roles, and gathering system and diagram schematics. Collection of this data can play a key role in planning, executing, and even revising an ICS-targeted attack. Methods of collection depend on the categories of data being targeted, which can include protocol specific, device specific, and process specific configurations and functionality. Information collected may pertain to a combination of system, supervisory, device, and network related data, which conceptually fall under high, medium, and low levels of plan operations. For example, information repositories on plant data at a high level or device specific programs at a low level. Sensitive floor plans, vendor device manuals, and other references may also be at risk and exposed on the internet or otherwise publicly accessible.

## Position in the attack flow
Phase 8 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (11)
- [T0801](https://attack.mitre.org/techniques/T0801) Monitor Process State
- [T0802](https://attack.mitre.org/techniques/T0802) Automated Collection
- [T0811](https://attack.mitre.org/techniques/T0811) Data from Information Repositories
- [T0830](https://attack.mitre.org/techniques/T0830) Adversary-in-the-Middle
- [T0845](https://attack.mitre.org/techniques/T0845) Program Upload
- [T0852](https://attack.mitre.org/techniques/T0852) Screen Capture
- [T0861](https://attack.mitre.org/techniques/T0861) Point & Tag Identification
- [T0868](https://attack.mitre.org/techniques/T0868) Detect Operating Mode
- [T0877](https://attack.mitre.org/techniques/T0877) I/O Image
- [T0887](https://attack.mitre.org/techniques/T0887) Wireless Sniffing
- [T0893](https://attack.mitre.org/techniques/T0893) Data from Local System

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0100
