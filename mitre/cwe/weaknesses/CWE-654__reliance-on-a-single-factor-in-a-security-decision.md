---
cwe_id: CWE-654
name: Reliance on a Single Factor in a Security Decision
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-16, CAPEC-274, CAPEC-49, CAPEC-55, CAPEC-560, CAPEC-565, CAPEC-600, CAPEC-652, CAPEC-653, CAPEC-70]
url: https://cwe.mitre.org/data/definitions/654.html
tags: [mitre-cwe, weakness, CWE-654]
---

# CWE-654 - Reliance on a Single Factor in a Security Decision

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-654](https://cwe.mitre.org/data/definitions/654.html)

## Description
A protection mechanism relies exclusively, or to a large extent, on the evaluation of a single condition or the integrity of a single object or entity in order to make a decision about granting access to restricted resources or functionality.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Non-Repudiation**: Hide Activities

## Potential mitigations
- **Architecture and Design**: Use multiple simultaneous checks before granting access to critical operations or granting critical privileges. A weaker but helpful mitigation is to use several successive checks (multiple layers of security).
- **Architecture and Design**: Use redundant access rules on different choke points (e.g., firewalls).

## Related attack patterns (CAPEC)
- [CAPEC-16](https://capec.mitre.org/data/definitions/16.html)
- [CAPEC-274](https://capec.mitre.org/data/definitions/274.html)
- [CAPEC-49](https://capec.mitre.org/data/definitions/49.html)
- [CAPEC-55](https://capec.mitre.org/data/definitions/55.html)
- [CAPEC-560](https://capec.mitre.org/data/definitions/560.html)
- [CAPEC-565](https://capec.mitre.org/data/definitions/565.html)
- [CAPEC-600](https://capec.mitre.org/data/definitions/600.html)
- [CAPEC-652](https://capec.mitre.org/data/definitions/652.html)
- [CAPEC-653](https://capec.mitre.org/data/definitions/653.html)
- [CAPEC-70](https://capec.mitre.org/data/definitions/70.html)

## Related weaknesses
- CWE-657 (ChildOf)
- CWE-693 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-35248**: Chat application skips validation when Central Authentication Service (CAS) is enabled, effectively removing the second factor from two-factor authentication

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/654.html
