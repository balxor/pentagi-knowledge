---
capec_id: CAPEC-509
name: Kerberoasting
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: [CWE-522, CWE-308, CWE-309, CWE-294, CWE-263, CWE-262, CWE-521]
related_attack: [T1558.003]
url: https://capec.mitre.org/data/definitions/509.html
tags: [mitre-capec, attack-pattern, CAPEC-509]
---

# CAPEC-509 - Kerberoasting

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-509](https://capec.mitre.org/data/definitions/509.html)

## Description
Through the exploitation of how service accounts leverage Kerberos authentication with Service Principal Names (SPNs), the adversary obtains and subsequently cracks the hashed credentials of a service account target to exploit its privileges. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. As an authenticated user, the adversary may request Active Directory and obtain a service ticket with portions encrypted via RC4 with the private key of the authenticated account. By extracting the local ticket and saving it disk, the adversary can brute force the hashed value to reveal the target account credentials.

## Prerequisites
- The adversary requires access as an authenticated user on the system. This attack pattern relates to elevating privileges.
- The adversary requires use of a third-party credential harvesting tool (e.g., Mimikatz).
- The adversary requires a brute force tool.

## Skills required
- **Medium**: 

## Consequences
- **Confidentiality**: Gain Privileges

## Execution flow
Execution Flow Explore Scan for user accounts with set SPN values Techniques These can be found via Powershell or LDAP queries, as well as enumerating startup name accounts and other means. Request service tickets Techniques Using user account's SPN value, request other service tickets from Active Directory Experiment Extract ticket and save to disk Techniques Certain tools like Mimikatz can extract local tickets and save them to memory/disk. Exploit Crack the encrypted ticket to harvest plain text credentials Techniques Leverage a brute force application/script on the hashed value offline until cracked. The shorter the password, the easier it is to crack.

## Mitigations
- Monitor system and domain logs for abnormal access.
- Employ a robust password policy for service accounts. Passwords should be of adequate length and complexity, and they should expire after a period of time.
- Employ the principle of least privilege: limit service accounts privileges to what is required for functionality and no more.
- Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.

## Related weaknesses (CWE)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-521](https://cwe.mitre.org/data/definitions/521.html)

## Related ATT&CK techniques
- T1558.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/509.html
