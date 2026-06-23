---
capec_id: CAPEC-166
name: Force the System to Reset Values
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-306, CWE-1221, CWE-1232]
related_attack: []
url: https://capec.mitre.org/data/definitions/166.html
tags: [mitre-capec, attack-pattern, CAPEC-166]
---

# CAPEC-166 - Force the System to Reset Values

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-166](https://capec.mitre.org/data/definitions/166.html)

## Description
An attacker forces the target into a previous state in order to leverage potential weaknesses in the target dependent upon a prior configuration or state-dependent factors. Even in cases where an attacker may not be able to directly control the configuration of the targeted application, they may be able to reset the configuration to a prior state since many applications implement reset functions.

## Extended description
Since these functions are usually intended as emergency features to return an application to a stable configuration if the current configuration degrades functionality, they may not be as strongly secured as other configuration options. The resetting of values is dangerous as it may enable undesired functionality, disable services, or modify access controls. At the very least this is a nuisance attack since the administrator will need to re-apply their configuration. At worst, this attack can open avenues for powerful attacks against the application, and, if it isn't obvious that the configuration has been reset, these vulnerabilities may be present a long time before they are notices.

## Prerequisites
- The targeted application must have a reset function that returns the configuration of the application to an earlier state.
- The reset functionality must be inadequately protected against use.

## Resources required
- None: No specialized resources are required to execute this type of attack. In some cases, the attacker may need special client applications in order to execute the reset functionality.

## Related weaknesses (CWE)
- [CWE-306](https://cwe.mitre.org/data/definitions/306.html)
- [CWE-1221](https://cwe.mitre.org/data/definitions/1221.html)
- [CWE-1232](https://cwe.mitre.org/data/definitions/1232.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/166.html
