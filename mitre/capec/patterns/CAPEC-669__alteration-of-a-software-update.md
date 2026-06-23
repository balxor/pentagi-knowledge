---
capec_id: CAPEC-669
name: Alteration of a Software Update
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: []
related_attack: [T1195.002]
url: https://capec.mitre.org/data/definitions/669.html
tags: [mitre-capec, attack-pattern, CAPEC-669]
---

# CAPEC-669 - Alteration of a Software Update

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-669](https://capec.mitre.org/data/definitions/669.html)

## Description
<xhtml:p>An adversary with access to an organization’s software update infrastructure inserts malware into the content of an outgoing update to fielded systems where a wide range of malicious effects are possible. With the same level of access, the adversary can alter a software update to perform specific malicious acts including granting the adversary control over the software’s normal functionality.</xhtml:p>

## Prerequisites
- An adversary would need to have penetrated an organization’s software update infrastructure including gaining access to components supporting the configuration management of software versions and updates related to the software maintenance of customer systems.

## Skills required
- **High**: Skills required include the ability to infiltrate the organization’s software update infrastructure either from the Internet or from within the organization, including subcontractors, and be able to change software being delivered to customer/user systems in an undetected manner.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands
- **Confidentiality**: Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Identify software with frequent updates: The adversary must first identify a target software that has updates at least with some frequency, enough that there is am update infrastructure. Experiment Gain access to udpate infrastructure: The adversary must then gain access to the organization's software update infrastructure. This can either be done by gaining remote access from outside the organization, or by having a malicious actor inside the organization gain access. It is often easier if someone within the organization gains access. Exploit Alter the software update: Through access to the software update infrastructure, an adversary will alter the software update by injecting malware into the content of an outgoing update.

## Mitigations
- Have a Software Assurance Plan that includes maintaining strict configuration management control of source code, object code and software development, build and distribution tools; manual code reviews and static code analysis for developmental software; and tracking of all storage and movement of code.
- Require elevated privileges for distribution of software and software updates.

## Related ATT&CK techniques
- T1195.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/669.html
