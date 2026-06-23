---
capec_id: CAPEC-194
name: Fake the Source of Data
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-287]
related_attack: []
url: https://capec.mitre.org/data/definitions/194.html
tags: [mitre-capec, attack-pattern, CAPEC-194]
---

# CAPEC-194 - Fake the Source of Data

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-194](https://capec.mitre.org/data/definitions/194.html)

## Description
An adversary takes advantage of improper authentication to provide data or services under a falsified identity. The purpose of using the falsified identity may be to prevent traceability of the provided data or to assume the rights granted to another individual. One of the simplest forms of this attack would be the creation of an email message with a modified "From" field in order to appear that the message was sent from someone other than the actual sender. The root of the attack (in this case the email system) fails to properly authenticate the source and this results in the reader incorrectly performing the instructed action. Results of the attack vary depending on the details of the attack, but common results include privilege escalation, obfuscation of other attacks, and data corruption/manipulation.

## Prerequisites
- This attack is only applicable when a vulnerable entity associates data or services with an identity. Without such an association, there would be no reason to fake the source.

## Resources required
- Resources required vary depending on the nature of the attack. Possible tools needed by an attacker could include tools to create custom network packets, specific client software, and tools to capture network traffic. Many variants of this attack require no attacker resources, however.

## Consequences
- **Integrity**: Alter Execution Logic (By faking the source of data or services, an adversary can cause a target to make incorrect decisions about how to proceed.), Gain Privileges (By impersonating identities that have an increased level of access, an adversary gain privilege that they many not have otherwise had.), Hide Activities (Faking the source of data or services can be used to create a false trail in logs as the target will associate any actions with the impersonated identity instead of the adversary.)

## Related weaknesses (CWE)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/194.html
