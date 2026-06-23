---
capec_id: CAPEC-555
name: Remote Services with Stolen Credentials
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Very High
related_cwe: [CWE-522, CWE-308, CWE-309, CWE-294, CWE-263, CWE-262, CWE-521]
related_attack: [T1021, T1114.002, T1133]
url: https://capec.mitre.org/data/definitions/555.html
tags: [mitre-capec, attack-pattern, CAPEC-555]
---

# CAPEC-555 - Remote Services with Stolen Credentials

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-555](https://capec.mitre.org/data/definitions/555.html)

## Description
This pattern of attack involves an adversary that uses stolen credentials to leverage remote services such as RDP, telnet, SSH, and VNC to log into a system. Once access is gained, any number of malicious activities could be performed.

## Mitigations
- Disable RDP, telnet, SSH and enable firewall rules to block such traffic. Limit users and accounts that have remote interactive login access. Remove the Local Administrators group from the list of groups allowed to login through RDP. Limit remote user permissions. Use remote desktop gateways and multifactor authentication for remote logins.

## Related weaknesses (CWE)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-521](https://cwe.mitre.org/data/definitions/521.html)

## Related ATT&CK techniques
- T1021
- T1114.002
- T1133

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/555.html
