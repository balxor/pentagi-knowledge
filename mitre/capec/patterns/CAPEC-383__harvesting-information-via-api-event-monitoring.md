---
capec_id: CAPEC-383
name: Harvesting Information via API Event Monitoring
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-311, CWE-319, CWE-419, CWE-602]
related_attack: [T1056.004]
url: https://capec.mitre.org/data/definitions/383.html
tags: [mitre-capec, attack-pattern, CAPEC-383]
---

# CAPEC-383 - Harvesting Information via API Event Monitoring

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-383](https://capec.mitre.org/data/definitions/383.html)

## Description
An adversary hosts an event within an application framework and then monitors the data exchanged during the course of the event for the purpose of harvesting any important data leaked during the transactions. One example could be harvesting lists of usernames or userIDs for the purpose of sending spam messages to those users. One example of this type of attack involves the adversary creating an event within the sub-application. Assume the adversary hosts a "virtual sale" of rare items. As other users enter the event, the attacker records via AiTM (CAPEC-94) proxy the user_ids and usernames of everyone who attends. The adversary would then be able to spam those users within the application using an automated script.

## Prerequisites
- The target software is utilizing application framework APIs

## Consequences
- **Confidentiality**: Read Data (The adversary is able to gather information to potentially support further nefarious activities.)

## Mitigations
- Leverage encryption techniques during information transactions so as to protect them from attack patterns of this kind.

## Related weaknesses (CWE)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)
- [CWE-319](https://cwe.mitre.org/data/definitions/319.html)
- [CWE-419](https://cwe.mitre.org/data/definitions/419.html)
- [CWE-602](https://cwe.mitre.org/data/definitions/602.html)

## Related ATT&CK techniques
- T1056.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/383.html
