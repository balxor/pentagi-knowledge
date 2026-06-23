---
cwe_id: CWE-290
name: Authentication Bypass by Spoofing
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-21, CAPEC-22, CAPEC-459, CAPEC-461, CAPEC-473, CAPEC-476, CAPEC-59, CAPEC-60, CAPEC-667, CAPEC-94]
url: https://cwe.mitre.org/data/definitions/290.html
tags: [mitre-cwe, weakness, CWE-290]
---

# CWE-290 - Authentication Bypass by Spoofing

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-290](https://cwe.mitre.org/data/definitions/290.html)

## Description
This attack-focused weakness is caused by incorrectly implemented authentication schemes that are subject to spoofing attacks.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Related attack patterns (CAPEC)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-22](https://capec.mitre.org/data/definitions/22.html)
- [CAPEC-459](https://capec.mitre.org/data/definitions/459.html)
- [CAPEC-461](https://capec.mitre.org/data/definitions/461.html)
- [CAPEC-473](https://capec.mitre.org/data/definitions/473.html)
- [CAPEC-476](https://capec.mitre.org/data/definitions/476.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
- [CAPEC-667](https://capec.mitre.org/data/definitions/667.html)
- [CAPEC-94](https://capec.mitre.org/data/definitions/94.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-287 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30319**: S-bus functionality in a home automation product performs access control using an IP allowlist, which can be bypassed by a forged IP address.
- **CVE-2009-1048**: VOIP product allows authentication bypass using 127.0.0.1 in the Host header.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/290.html
