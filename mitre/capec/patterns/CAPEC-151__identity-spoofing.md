---
capec_id: CAPEC-151
name: Identity Spoofing
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: Medium
related_cwe: [CWE-287]
related_attack: []
url: https://capec.mitre.org/data/definitions/151.html
tags: [mitre-capec, attack-pattern, CAPEC-151]
---

# CAPEC-151 - Identity Spoofing

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-151](https://capec.mitre.org/data/definitions/151.html)

## Description
Identity Spoofing refers to the action of assuming (i.e., taking on) the identity of some other entity (human or non-human) and then using that identity to accomplish a goal. An adversary may craft messages that appear to come from a different principle or use stolen / spoofed authentication credentials.

## Extended description
Alternatively, an adversary may intercept a message from a legitimate sender and attempt to make it look like the message comes from them without changing its content. The latter form of this attack can be used to hijack credentials from legitimate users. Identity Spoofing attacks need not be limited to transmitted messages - any resource that is associated with an identity (for example, a file with a signature) can be the target of an attack where the adversary attempts to change the apparent identity. This attack differs from Content Spoofing attacks where the adversary does not wish to change the apparent identity of the message but instead wishes to change what the message says. In an Identity Spoofing attack, the adversary is attempting to change the identity of the content.

## Prerequisites
- The identity associated with the message or resource must be removable or modifiable in an undetectable way.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Confidentiality**: Gain Privileges
- **Integrity**: Gain Privileges

## Mitigations
- Employ robust authentication processes (e.g., multi-factor authentication).

## Related weaknesses (CWE)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/151.html
