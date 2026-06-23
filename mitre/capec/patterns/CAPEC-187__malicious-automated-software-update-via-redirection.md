---
capec_id: CAPEC-187
name: Malicious Automated Software Update via Redirection
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-494]
related_attack: [T1072]
url: https://capec.mitre.org/data/definitions/187.html
tags: [mitre-capec, attack-pattern, CAPEC-187]
---

# CAPEC-187 - Malicious Automated Software Update via Redirection

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-187](https://capec.mitre.org/data/definitions/187.html)

## Description
An attacker exploits two layers of weaknesses in server or client software for automated update mechanisms to undermine the integrity of the target code-base. The first weakness involves a failure to properly authenticate a server as a source of update or patch content. This type of weakness typically results from authentication mechanisms which can be defeated, allowing a hostile server to satisfy the criteria that establish a trust relationship. The second weakness is a systemic failure to validate the identity and integrity of code downloaded from a remote location, hence the inability to distinguish malicious code from a legitimate update.

## Extended description
One predominate type of redirection attack requires DNS spoofing or hijacking of a domain name corresponding to an update server. The target software initiates an update request and the DNS request resolves the domain name of the update server to the IP address of the attacker, at which point the software accepts updates either transmitted by or pulled from the attackers' server. Attacks against DNS mechanisms comprise an initial phase of a chain of attacks that facilitate automated update hijacking attack, and such attacks have a precedent in targeted activities that have been as complex as DNS/BIND attacks of corporate infrastructures, to untargeted attacks aimed at compromising home broadband routers, as well as attacks involving the compromise of wireless access points, as well as 'evil twin' attacks coupled with DNS redirection. Due to the plethora of options open to the attacker in forcing name resolution to arbitrary servers the Automated Update Hijacking attack strategies are the tip of the spear for many multi-stage attack chains. The second weakness that is exploited by the attacker is the lack of integrity checking by the software in validating the update. Software which relies only upon domain name resolution to establish the identity of update code is particularly vulnerable, because this signals an absence of other security countermeasures that could be applied to invalidate the attackers' payload on basis of code identity, hashing, signing, encryption, and other integrity checking mechanisms. Redirection-based attack patterns work equally well against client-side software as well as local servers or daemons that provide software update functionality.

## Consequences
- **Access_Control**: Execute Unauthorized Commands
- **Availability**: Execute Unauthorized Commands
- **Confidentiality**: Execute Unauthorized Commands

## Related weaknesses (CWE)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)

## Related ATT&CK techniques
- T1072

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/187.html
