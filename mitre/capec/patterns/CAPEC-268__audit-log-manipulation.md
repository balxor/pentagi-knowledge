---
capec_id: CAPEC-268
name: Audit Log Manipulation
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-117]
related_attack: [T1070, T1562.002, T1562.003, T1562.008]
url: https://capec.mitre.org/data/definitions/268.html
tags: [mitre-capec, attack-pattern, CAPEC-268]
---

# CAPEC-268 - Audit Log Manipulation

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-268](https://capec.mitre.org/data/definitions/268.html)

## Description
The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cover tracks of an attack. Due to either insufficient access controls of the log files or the logging mechanism, the attacker is able to perform such actions.

## Prerequisites
- The target host is logging the action and data of the user.
- The target host insufficiently protects access to the logs or logging mechanisms.

## Resources required
- The attacker must understand how the logging mechanism works. Optionally, the attacker must know the location and the format of individual entries of the log files.

## Related weaknesses (CWE)
- [CWE-117](https://cwe.mitre.org/data/definitions/117.html)

## Related ATT&CK techniques
- T1070
- T1562.002
- T1562.003
- T1562.008

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/268.html
