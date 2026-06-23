---
capec_id: CAPEC-698
name: Install Malicious Extension
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-507, CWE-829]
related_attack: [T1176, T1505.004]
url: https://capec.mitre.org/data/definitions/698.html
tags: [mitre-capec, attack-pattern, CAPEC-698]
---

# CAPEC-698 - Install Malicious Extension

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-698](https://capec.mitre.org/data/definitions/698.html)

## Description
<xhtml:p>An adversary directly installs or tricks a user into installing a malicious extension into existing trusted software, with the goal of achieving a variety of negative technical impacts.</xhtml:p>

## Extended description
Many software applications allow users to install third-party software extensions/plugins that provide additional features and functionality. Adversaries can take advantage of this behavior to install malware on a system with relative ease. This may require the adversary compromising a system and then installing the malicious extension themself. An alternate approach entails masquerading the malicious extension as a legitimate extension. The adversary then convinces users to install the malicious component, via means such as social engineering, or simply waits for victims to unknowingly install the malware on their systems. Once the malicious extension has been installed, the adversary can achieve a variety of negative technical impacts such as obtaining sensitive information, executing unauthorized commands, observing/modifying network traffic, and more.

## Prerequisites
- The adversary must craft malware based on the type of software and system(s) they intend to exploit.
- If the adversary intends to install the malicious extension themself, they must first compromise the target machine via some other means.

## Skills required
- **Medium**: Optional: Ability to exploit target system(s) via other means in order to gain entry.

## Consequences
- **Access_Control**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Authorization**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Confidentiality**: Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Identify target(s): The adversary must first identify target software that allows for extensions/plugins and which they wish to exploit, such as a web browser or desktop application. To increase the attack space, this will often be popular software with a large user-base. Experiment Create malicious extension: Having identified a suitable target, the adversary crafts a malicious extension/plugin that can be installed by the underlying target software. This malware may be targeted to execute on specific operating systems or be operating system agnostic. Exploit Install malicious extension: The malicious extension/plugin is installed by the underlying target software and executes the adversary-created malware, resulting in a variety of negative technical impacts. Techniques Adversary-Installed: Having already compromised the target system, the adversary simply installs the malicious extension/plugin themself. User-Installed: The adversary tricks the user into installing the malicious extension/plugin, via means such as social engineering, or may upload the malware on a reputable extension/plugin hosting site and wait for unknowing victims to install the malicious component.

## Mitigations
- Only install extensions/plugins from official/verifiable sources.
- Confirm extensions/plugins are legitimate and not malware masquerading as a legitimate extension/plugin.
- Ensure the underlying software leveraging the extension/plugin (including operating systems) is up-to-date.
- Implement an extension/plugin allow list, based on the given security policy.
- If applicable, confirm extensions/plugins are properly signed by the official developers.
- For web browsers, close sessions when finished to prevent malicious extensions/plugins from executing the the background.

## Related weaknesses (CWE)
- [CWE-507](https://cwe.mitre.org/data/definitions/507.html)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

## Related ATT&CK techniques
- T1176
- T1505.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/698.html
