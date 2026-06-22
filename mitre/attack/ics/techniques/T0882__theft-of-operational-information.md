---
attack_id: T0882
name: Theft of Operational Information
type: technique
parent: null
tactics: [Impact]
platforms: [None]
url: https://attack.mitre.org/techniques/T0882
tags: [mitre-attack, technique, T0882]
---

# T0882 - Theft of Operational Information

**Tactic(s):** Impact  -  **Platforms:** None  -  **ATT&CK:** [T0882](https://attack.mitre.org/techniques/T0882)

## Summary
Adversaries may steal operational information on a production environment as a direct mission outcome for personal gain or to inform future operations. This information may include design documents, schedules, rotational data, or similar artifacts that provide insight on operations.    In the Bowman Dam incident, adversaries probed systems for operational data. (Citation: Mark Thompson March 2016) (Citation: Danny Yadron December 2015)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0922 Restrict File and Directory Permissions** - Restrict access by setting directory and file permissions that are not specific to users or privileged accounts.
- **M0809 Operational Information Confidentiality** - Deploy mechanisms to protect the confidentiality of information related to operational processes, facility locations, device configurations, programs, or databases that may have information that can be used to infer organizational trade-secrets, recipes, and other intellectual property (IP).
- **M0803 Data Loss Prevention** - Data Loss Prevention (DLP) technologies can be used to help identify adversarial attempts to exfiltrate operational information, such as engineering plans, trade secrets, recipes, intellectual property, or process telemetry. DLP functionality may be built into other security products such as firewalls or standalone suites running on the network and host-based agents. DLP may be configured to prevent the transfer of information through corporate resources such as email, web, and physical media such as USB for host-based solutions.
- **M0941 Encrypt Sensitive Information** - Protect sensitive data-at-rest with strong encryption.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0882
