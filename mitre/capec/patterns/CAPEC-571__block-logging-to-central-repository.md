---
capec_id: CAPEC-571
name: Block Logging to Central Repository
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Low
related_cwe: []
related_attack: [T1562.002, T1562.002, T1562.006, T1562.008]
url: https://capec.mitre.org/data/definitions/571.html
tags: [mitre-capec, attack-pattern, CAPEC-571]
---

# CAPEC-571 - Block Logging to Central Repository

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-571](https://capec.mitre.org/data/definitions/571.html)

## Description
<xhtml:p>An adversary prevents host-generated logs being delivered to a central location in an attempt to hide indicators of compromise.</xhtml:p>

## Extended description
In the case of network based reporting of indicators, an adversary may block traffic associated with reporting to prevent central station analysis. This may be accomplished by many means such as stopping a local process to creating a host-based firewall rule to block traffic to a specific server. In the case of local based reporting of indicators, an adversary may block delivery of locally-generated log files themselves to the central repository.

## Related ATT&CK techniques
- T1562.002
- T1562.002
- T1562.006
- T1562.008

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/571.html
