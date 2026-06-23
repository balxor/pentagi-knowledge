---
capec_id: CAPEC-186
name: Malicious Software Update
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: High
related_cwe: [CWE-494]
related_attack: [T1195.002]
url: https://capec.mitre.org/data/definitions/186.html
tags: [mitre-capec, attack-pattern, CAPEC-186]
---

# CAPEC-186 - Malicious Software Update

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-186](https://capec.mitre.org/data/definitions/186.html)

## Description
An adversary uses deceptive methods to cause a user or an automated process to download and install dangerous code believed to be a valid update that originates from an adversary controlled source.

## Extended description
Although there are several variations to this strategy of attack, the attack methods are united in that all rely on the ability of an adversary to position and disguise malicious content such that it masquerades as a legitimate software update which is then processed by a program, undermining application integrity. As such the attack employs 'spoofing' techniques augmented by psychological or technological mechanisms to disguise the update and/or its source. Virtually all software requires frequent updates or patches, giving the adversary immense latitude when structuring the attack, as well as many targets of opportunity. Automated attacks involving malicious software updates require little to no user-directed activity and are therefore advantageous because they avoid the complex preliminary setup stages of manual attacks, which must effectively 'hook' users while avoiding countermeasures such as spam filters or web security filters.

## Skills required
- **High**: This attack requires advanced cyber capabilities

## Resources required
- Manual or user-assisted attacks require deceptive mechanisms to trick the user into clicking a link or downloading and installing software. Automated update attacks require the adversary to host a payload and then trigger the installation of the payload code.

## Consequences
- **Access_Control**: Execute Unauthorized Commands (Utilize the built-in software update mechanisms of the commercial components to deliver software that could compromise security credentials, enable a denial-of-service attack, or enable tracking.)
- **Availability**: Execute Unauthorized Commands (Utilize the built-in software update mechanisms of the commercial components to deliver software that could compromise security credentials, enable a denial-of-service attack, or enable tracking.)
- **Confidentiality**: Execute Unauthorized Commands (Utilize the built-in software update mechanisms of the commercial components to deliver software that could compromise security credentials, enable a denial-of-service attack, or enable tracking.)

## Execution flow
Execution Flow Explore Identify target: The adversary must first identify what they want their target to be. Because malicious software updates can be carried out in a variety of ways, the adversary will first not only identify a target program, but also what users they wish to target. This attack can be targeted (a particular user or group of users) or untargeted (many different users). Experiment Craft a deployment mechanism based on the target: The adversary must craft a deployment mechanism to deploy the malicious software update. This mechanism will differ based on if the attack is targeted or untargeted. Techniques Targeted attack: hosting what appears to be a software update, then harvesting actual email addresses for an organization, or generating commonly used email addresses, and then sending spam, phishing, or spear-phishing emails to the organization's users requesting that they manually download and install the malicious software update. Targeted attack: Instant Messaging virus payload, which harvests the names from a user's contact list and sends instant messages to those users to download and apply the update Untargeted attack: Spam the malicious update to as many users as possible through unsolicited email, instant messages, or social media messages. Untargeted attack: Send phishing emails to as many users as possible and pretend to be a legitimate source suggesting to download an important software update. Untargeted attack: Use trojans/botnets to aid in either of the two untargeted attacks. Exploit Deploy malicious software update: Using the deployment mechanism from the previous step, the adversary gets a user to install the malicious software update.

## Mitigations
- Validate software updates before installing.

## Related weaknesses (CWE)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)

## Related ATT&CK techniques
- T1195.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/186.html
