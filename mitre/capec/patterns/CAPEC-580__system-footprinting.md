---
capec_id: CAPEC-580
name: System Footprinting
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Low
related_cwe: [CWE-204, CWE-205, CWE-208]
related_attack: [T1082]
url: https://capec.mitre.org/data/definitions/580.html
tags: [mitre-capec, attack-pattern, CAPEC-580]
---

# CAPEC-580 - System Footprinting

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-580](https://capec.mitre.org/data/definitions/580.html)

## Description
An adversary engages in active probing and exploration activities to determine security information about a remote target system. Often times adversaries will rely on remote applications that can be probed for system configurations.

## Prerequisites
- The adversary must have logical access to the target network and system.

## Skills required
- **Low**: The adversary needs to know basic linux commands.

## Consequences
- **Confidentiality**: Read Data

## Mitigations
- Keep patches up to date by installing weekly or daily if possible.
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related weaknesses (CWE)
- [CWE-204](https://cwe.mitre.org/data/definitions/204.html)
- [CWE-205](https://cwe.mitre.org/data/definitions/205.html)
- [CWE-208](https://cwe.mitre.org/data/definitions/208.html)

## Related ATT&CK techniques
- T1082

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/580.html
