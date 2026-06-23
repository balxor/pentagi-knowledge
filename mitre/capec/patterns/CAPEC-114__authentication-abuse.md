---
capec_id: CAPEC-114
name: Authentication Abuse
type: attack-pattern
abstraction: Meta
likelihood: n/a
severity: Medium
related_cwe: [CWE-287, CWE-1244]
related_attack: [T1548]
url: https://capec.mitre.org/data/definitions/114.html
tags: [mitre-capec, attack-pattern, CAPEC-114]
---

# CAPEC-114 - Authentication Abuse

**Abstraction:** Meta  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-114](https://capec.mitre.org/data/definitions/114.html)

## Description
An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is functioning but a carefully controlled sequence of events causes the mechanism to grant access to the attacker.

## Extended description
This attack may exploit assumptions made by the target's authentication procedures, such as assumptions regarding trust relationships or assumptions regarding the generation of secret values. This attack differs from Authentication Bypass attacks in that Authentication Abuse allows the attacker to be certified as a valid user through illegitimate means, while Authentication Bypass allows the user to access protected material without ever being certified as an authenticated user. This attack does not rely on prior sessions established by successfully authenticating users, as relied upon for the "Exploitation of Session Variables, Resource IDs and other Trusted Credentials" attack patterns.

## Prerequisites
- An authentication mechanism or subsystem implementing some form of authentication such as passwords, digest authentication, security certificates, etc. which is flawed in some way.

## Resources required
- A client application, command-line access to a binary, or scripting language capable of interacting with the authentication mechanism.

## Related weaknesses (CWE)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)
- [CWE-1244](https://cwe.mitre.org/data/definitions/1244.html)

## Related ATT&CK techniques
- T1548

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/114.html
