---
capec_id: CAPEC-148
name: Content Spoofing
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: Medium
related_cwe: [CWE-345]
related_attack: [T1491]
url: https://capec.mitre.org/data/definitions/148.html
tags: [mitre-capec, attack-pattern, CAPEC-148]
---

# CAPEC-148 - Content Spoofing

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-148](https://capec.mitre.org/data/definitions/148.html)

## Description
An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.

## Prerequisites
- The target must provide content but fail to adequately protect it against modification.The adversary must have the means to alter data to which they are not authorized. If the content is to be modified in transit, the adversary must be able to intercept the targeted messages.

## Resources required
- If the content is to be modified in transit, the adversary requires a tool capable of intercepting the target's communication and generating/creating custom packets to impact the communications. In some variants, the targeted content is altered so that all or some of it is redirected towards content published by the attacker (for example, images and frames in the target's web site might be modified to be loaded from a source controlled by the attacker). In these cases, the attacker requires the necessary resources to host the replacement content.

## Consequences
- **Integrity**: Modify Data (A successful content spoofing attack compromises the integrity of the application data.)

## Related weaknesses (CWE)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)

## Related ATT&CK techniques
- T1491

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/148.html
