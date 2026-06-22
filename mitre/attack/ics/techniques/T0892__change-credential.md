---
attack_id: T0892
name: Change Credential
type: technique
parent: null
tactics: [Inhibit Response Function]
platforms: [None]
url: https://attack.mitre.org/techniques/T0892
tags: [mitre-attack, technique, T0892]
---

# T0892 - Change Credential

**Tactic(s):** Inhibit Response Function  -  **Platforms:** None  -  **ATT&CK:** [T0892](https://attack.mitre.org/techniques/T0892)

## Summary
Adversaries may modify software and device credentials to prevent operator and responder access. Depending on the device, the modification or addition of this password could prevent any device configuration actions from being accomplished and may require a factory reset or replacement of hardware. These credentials are often built-in features provided by the device vendors as a means to restrict access to management interfaces.

An adversary with access to valid or hardcoded credentials could change the credential to prevent future authorized device access. Change Credential may be especially damaging when paired with other techniques such as Modify Program, Data Destruction, or Modify Controller Tasking. In these cases, a device’s configuration may be destroyed or include malicious actions for the process environment, which cannot not be removed through normal device configuration actions. 

Additionally, recovery of the device and original configuration may be difficult depending on the features provided by the device. In some cases, these passwords cannot be removed onsite and may require that the device be sent back to the vendor for additional recovery steps.


A chain of incidents occurred in Germany, where adversaries locked operators out of their building automation system (BAS) controllers by enabling a previously unset BCU key. (Citation: German BAS Lockout Dec 2021)

## Role in the attack flow
Used to achieve the **Inhibit Response Function** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0927 Password Policies** - Set and enforce secure password policies for accounts.
- **M0953 Data Backup** - Take and store data backups from end user systems and critical servers. Ensure backup and storage systems are hardened and kept separate from the corporate network to prevent compromise.   Maintain and exercise incident response plans  (Citation: Department of Homeland Security October 2009), including the management of  'gold-copy' back-up images and configurations for key systems to enable quick recovery and response from adversarial activities that impact control, view, or availability.
- **M0811 Redundancy of Service** - Redundancy could be provided for both critical ICS devices and services, such as back-up devices or hot-standbys.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0892
