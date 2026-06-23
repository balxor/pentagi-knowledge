---
capec_id: CAPEC-645
name: Use of Captured Tickets (Pass The Ticket)
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-522, CWE-294, CWE-308]
related_attack: [T1550.003]
url: https://capec.mitre.org/data/definitions/645.html
tags: [mitre-capec, attack-pattern, CAPEC-645]
---

# CAPEC-645 - Use of Captured Tickets (Pass The Ticket)

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-645](https://capec.mitre.org/data/definitions/645.html)

## Description
An adversary uses stolen Kerberos tickets to access systems/resources that leverage the Kerberos authentication protocol. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. An adversary can obtain any one of these tickets (e.g. Service Ticket, Ticket Granting Ticket, Silver Ticket, or Golden Ticket) to authenticate to a system/resource without needing the account's credentials. Depending on the ticket obtained, the adversary may be able to access a particular resource or generate TGTs for any account within an Active Directory Domain.

## Prerequisites
- The adversary needs physical access to the victim system.
- The use of a third-party credential harvesting tool.

## Skills required
- **High**: The adversary uses a third-party tool to obtain the necessary tickets to execute the attack.
- **Low**: Determine if Kerberos authentication is used on the server.

## Consequences
- **Integrity**: Gain Privileges

## Mitigations
- Reset the built-in KRBTGT account password twice to invalidate the existence of any current Golden Tickets and any tickets derived from them.
- Monitor system and domain logs for abnormal access.

## Related weaknesses (CWE)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)

## Related ATT&CK techniques
- T1550.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/645.html
