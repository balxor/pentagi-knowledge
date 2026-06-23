---
capec_id: CAPEC-594
name: Traffic Injection
type: attack-pattern
abstraction: Meta
likelihood: n/a
severity: n/a
related_cwe: [CWE-940]
related_attack: []
url: https://capec.mitre.org/data/definitions/594.html
tags: [mitre-capec, attack-pattern, CAPEC-594]
---

# CAPEC-594 - Traffic Injection

**Abstraction:** Meta  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-594](https://capec.mitre.org/data/definitions/594.html)

## Description
An adversary injects traffic into the target's network connection. The adversary is therefore able to degrade or disrupt the connection, and potentially modify the content. This is not a flooding attack, as the adversary is not focusing on exhausting resources. Instead, the adversary is crafting a specific input to affect the system in a particular way.

## Prerequisites
- The target application must leverage an open communications channel.
- The channel on which the target communicates must be vulnerable to interception (e.g., adversary in the middle attack - CAPEC-94).

## Resources required
- A tool, such as a MITM Proxy, that is capable of generating and injecting custom inputs to be used in the attack.

## Consequences
- **Availability**: Unreliable Execution (The injection of specific content into a connection can trigger a disruption in that communications channel, thereby denying availability of the service.)
- **Integrity**: Other (An adversary's injection of additional content into a communication channel negatively impacts the integrity of that channel.)

## Related weaknesses (CWE)
- [CWE-940](https://cwe.mitre.org/data/definitions/940.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/594.html
