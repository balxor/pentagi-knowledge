---
capec_id: CAPEC-633
name: Token Impersonation
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-287, CWE-1270]
related_attack: [T1134]
url: https://capec.mitre.org/data/definitions/633.html
tags: [mitre-capec, attack-pattern, CAPEC-633]
---

# CAPEC-633 - Token Impersonation

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-633](https://capec.mitre.org/data/definitions/633.html)

## Description
An adversary exploits a weakness in authentication to create an access token (or equivalent) that impersonates a different entity, and then associates a process/thread to that that impersonated token. This action causes a downstream user to make a decision or take action that is based on the assumed identity, and not the response that blocks the adversary.

## Prerequisites
- This pattern of attack is only applicable when a downstream user leverages tokens to verify identity, and then takes action based on that identity.

## Consequences
- **Integrity**: Alter Execution Logic (By faking the source of data or services, an adversary can cause a target to make incorrect decisions about how to proceed.), Gain Privileges (By impersonating identities that have an increased level of access, an adversary gain privilege that they many not have otherwise had.), Hide Activities (Faking the source of data or services can be used to create a false trail in logs as the target will associated any actions with the impersonated identity instead of the adversary.)

## Related weaknesses (CWE)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)
- [CWE-1270](https://cwe.mitre.org/data/definitions/1270.html)

## Related ATT&CK techniques
- T1134

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/633.html
