---
capec_id: CAPEC-89
name: Pharming
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-346, CWE-350]
related_attack: []
url: https://capec.mitre.org/data/definitions/89.html
tags: [mitre-capec, attack-pattern, CAPEC-89]
---

# CAPEC-89 - Pharming

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-89](https://capec.mitre.org/data/definitions/89.html)

## Description
A pharming attack occurs when the victim is fooled into entering sensitive data into supposedly trusted locations, such as an online bank site or a trading platform. An attacker can impersonate these supposedly trusted sites and have the victim be directed to their site rather than the originally intended one. Pharming does not require script injection or clicking on malicious links for the attack to succeed.

## Prerequisites
- Vulnerable DNS software or improperly protected hosts file or router that can be poisoned
- A website that handles sensitive information but does not use a secure connection and a certificate that is valid is also prone to pharming

## Skills required
- **Medium**: The attacker needs to be able to poison the resolver - DNS entries or local hosts file or router entry pointing to a trusted DNS server - in order to successfully carry out a pharming attack. Setting up a fake website, identical to the targeted one, does not require special skills.

## Resources required
- None: No specialized resources are required to execute this type of attack. Having knowledge of the way the target site has been structured, in order to create a fake version, is required. Poisoning the resolver requires knowledge of a vulnerability that can be exploited.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Exploit Attacker sets up a system mocking the one trusted by the users. This is usually a website that requires or handles sensitive information. The attacker then poisons the resolver for the targeted site. This is achieved by poisoning the DNS server, or the local hosts file, that directs the user to the original website When the victim requests the URL for the site, the poisoned records direct the victim to the attackers' system rather than the original one. Because of the identical nature of the original site and the attacker controlled one, and the fact that the URL is still the original one, the victim trusts the website reached and the attacker can now "farm" sensitive information such as credentials or account numbers.

## Mitigations
- All sensitive information must be handled over a secure connection.
- Known vulnerabilities in DNS or router software or in operating systems must be patched as soon as a fix has been released and tested.
- End users must ensure that they provide sensitive information only to websites that they trust, over a secure connection with a valid certificate issued by a well-known certificate authority.

## Related weaknesses (CWE)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-350](https://cwe.mitre.org/data/definitions/350.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/89.html
