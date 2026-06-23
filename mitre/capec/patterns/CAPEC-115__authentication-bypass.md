---
capec_id: CAPEC-115
name: Authentication Bypass
type: attack-pattern
abstraction: Meta
likelihood: n/a
severity: Medium
related_cwe: [CWE-287]
related_attack: [T1548]
url: https://capec.mitre.org/data/definitions/115.html
tags: [mitre-capec, attack-pattern, CAPEC-115]
---

# CAPEC-115 - Authentication Bypass

**Abstraction:** Meta  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-115](https://capec.mitre.org/data/definitions/115.html)

## Description
An attacker gains access to application, service, or device with the privileges of an authorized or privileged user by evading or circumventing an authentication mechanism. The attacker is therefore able to access protected data without authentication ever having taken place.

## Extended description
This refers to an attacker gaining access equivalent to an authenticated user without ever going through an authentication procedure. This is usually the result of the attacker using an unexpected access procedure that does not go through the proper checkpoints where authentication should occur. For example, a web site might assume that all users will click through a given link in order to get to secure material and simply authenticate everyone that clicks the link. However, an attacker might be able to reach secured web content by explicitly entering the path to the content rather than clicking through the authentication link, thereby avoiding the check entirely. This attack pattern differs from other authentication attacks in that attacks of this pattern avoid authentication entirely, rather than faking authentication by exploiting flaws or by stealing credentials from legitimate users.

## Prerequisites
- An authentication mechanism or subsystem implementing some form of authentication such as passwords, digest authentication, security certificates, etc.

## Resources required
- A client application, such as a web browser, or a scripting language capable of interacting with the target.

## Related weaknesses (CWE)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)

## Related ATT&CK techniques
- T1548

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/115.html
