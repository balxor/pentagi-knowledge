---
capec_id: CAPEC-310
name: Scanning for Vulnerable Software
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/310.html
tags: [mitre-capec, attack-pattern, CAPEC-310]
---

# CAPEC-310 - Scanning for Vulnerable Software

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-310](https://capec.mitre.org/data/definitions/310.html)

## Description
An attacker engages in scanning activity to find vulnerable software versions or types, such as operating system versions or network services. Vulnerable or exploitable network configurations, such as improperly firewalled systems, or misconfigured systems in the DMZ or external network, provide windows of opportunity for an attacker. Common types of vulnerable software include unpatched operating systems or services (e.g FTP, Telnet, SMTP, SNMP) running on open ports that the attacker has identified. Attackers usually begin probing for vulnerable software once the external network has been port scanned and potential targets have been revealed.

## Prerequisites
- Access to the network on which the targeted system resides.
- Software tools used to probe systems over a range of ports and protocols.

## Skills required
- **Medium**: To probe a system remotely without detection requires careful planning and patience.

## Resources required
- Probing requires the ability to interactively send and receive data from a target, whereas passive listening requires a sufficient understanding of the protocol to analyze a preexisting channel of communication.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/310.html
