---
capec_id: CAPEC-203
name: Manipulate Registry Information
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-15]
related_attack: [T1112, T1647]
url: https://capec.mitre.org/data/definitions/203.html
tags: [mitre-capec, attack-pattern, CAPEC-203]
---

# CAPEC-203 - Manipulate Registry Information

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-203](https://capec.mitre.org/data/definitions/203.html)

## Description
An adversary exploits a weakness in authorization in order to modify content within a registry (e.g., Windows Registry, Mac plist, application registry). Editing registry information can permit the adversary to hide configuration information or remove indicators of compromise to cover up activity. Many applications utilize registries to store configuration and service information. As such, modification of registry information can affect individual services (affecting billing, authorization, or even allowing for identity spoofing) or the overall configuration of a targeted application. For example, both Java RMI and SOAP use registries to track available services. Changing registry values is sometimes a preliminary step towards completing another attack pattern, but given the long term usage of many registry values, manipulation of registry information could be its own end.

## Prerequisites
- The targeted application must rely on values stored in a registry.
- The adversary must have a means of elevating permissions in order to access and modify registry content through either administrator privileges (e.g., credentialed access), or a remote access tool capable of editing a registry through an API.

## Skills required
- **High**: The adversary requires privileged credentials or the development/acquiring of a tailored remote access tool.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Mitigations
- Ensure proper permissions are set for Registry hives to prevent users from modifying keys.
- Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.
- Employ robust identification and audit/blocking using an allowlist of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.

## Related weaknesses (CWE)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)

## Related ATT&CK techniques
- T1112
- T1647

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/203.html
