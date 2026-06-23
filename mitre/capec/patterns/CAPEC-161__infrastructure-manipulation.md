---
capec_id: CAPEC-161
name: Infrastructure Manipulation
type: attack-pattern
abstraction: Meta
likelihood: n/a
severity: High
related_cwe: [CWE-923]
related_attack: []
url: https://capec.mitre.org/data/definitions/161.html
tags: [mitre-capec, attack-pattern, CAPEC-161]
---

# CAPEC-161 - Infrastructure Manipulation

**Abstraction:** Meta  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-161](https://capec.mitre.org/data/definitions/161.html)

## Description
An attacker exploits characteristics of the infrastructure of a network entity in order to perpetrate attacks or information gathering on network objects or effect a change in the ordinary information flow between network objects. Most often, this involves manipulation of the routing of network messages so, instead of arriving at their proper destination, they are directed towards an entity of the attackers' choosing, usually a server controlled by the attacker. The victim is often unaware that their messages are not being processed correctly. For example, a targeted client may believe they are connecting to their own bank but, in fact, be connecting to a Pharming site controlled by the attacker which then collects the user's login information in order to hijack the actual bank account.

## Prerequisites
- The targeted client must access the site via infrastructure that the attacker has co-opted and must fail to adequately verify that the communication channel is operating correctly (e.g. by verifying that they are, in fact, connected to the site they intended.)

## Resources required
- The attacker must be able to corrupt the infrastructure used by the client. For some variants of this attack, the attacker must be able to stand up their own services that mimic the services the targeted client intends to use.

## Related weaknesses (CWE)
- [CWE-923](https://cwe.mitre.org/data/definitions/923.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/161.html
