---
capec_id: CAPEC-564
name: Run Software at Logon
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-284]
related_attack: [T1037, T1543.001, T1543.004, T1547]
url: https://capec.mitre.org/data/definitions/564.html
tags: [mitre-capec, attack-pattern, CAPEC-564]
---

# CAPEC-564 - Run Software at Logon

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-564](https://capec.mitre.org/data/definitions/564.html)

## Description
Operating system allows logon scripts to be run whenever a specific user or users logon to a system. If adversaries can access these scripts, they may insert additional code into the logon script. This code can allow them to maintain persistence or move laterally within an enclave because it is executed every time the affected user or users logon to a computer. Modifying logon scripts can effectively bypass workstation and enclave firewalls. Depending on the access configuration of the logon scripts, either local credentials or a remote administrative account may be necessary.

## Mitigations
- Restrict write access to logon scripts to necessary administrators.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1037
- T1543.001
- T1543.004
- T1547

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/564.html
