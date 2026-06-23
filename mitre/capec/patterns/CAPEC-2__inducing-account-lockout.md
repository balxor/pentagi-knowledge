---
capec_id: CAPEC-2
name: Inducing Account Lockout
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Medium
related_cwe: [CWE-645]
related_attack: [T1531]
url: https://capec.mitre.org/data/definitions/2.html
tags: [mitre-capec, attack-pattern, CAPEC-2]
---

# CAPEC-2 - Inducing Account Lockout

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-2](https://capec.mitre.org/data/definitions/2.html)

## Description
An attacker leverages the security functionality of the system aimed at thwarting potential attacks to launch a denial of service attack against a legitimate system user. Many systems, for instance, implement a password throttling mechanism that locks an account after a certain number of incorrect log in attempts. An attacker can leverage this throttling mechanism to lock a legitimate user out of their own account. The weakness that is being leveraged by an attacker is the very security feature that has been put in place to counteract attacks.

## Prerequisites
- The system has a lockout mechanism.
- An attacker must be able to reproduce behavior that would result in an account being locked.

## Skills required
- **Low**: No programming skills or computer knowledge is needed. An attacker can easily use this attack pattern following the Execution Flow above.

## Resources required
- Computer with access to the login portion of the target system

## Consequences
- **Availability**: Resource Consumption (Denial of Service)

## Execution flow
Execution Flow Experiment Investigate account lockout behavior of system: Investigate the security features present in the system that may trigger an account lockout Techniques Analyze system documentation to find list of events that could potentially cause account lockout Obtain user account in system and attempt to lock it out by sending malformed or incorrect data repeatedly Determine another user's login ID, and attempt to brute force the password (or other credentials) for it a predetermined number of times, or until the system provides an indication that the account is locked out. Obtain list of user accounts to lock out: Generate a list of valid user accounts to lock out Techniques Obtain list of authorized users using another attack pattern, such as SQL Injection. Attempt to create accounts if possible; system should indicate if a user ID is already taken. Attempt to brute force user IDs if system reveals whether a given user ID is valid or not upon failed login attempts. Exploit Lock Out Accounts: Perform lockout procedure for all accounts that the attacker wants to lock out. Techniques For each user ID to be locked out, perform the lockout procedure discovered in the first step.

## Mitigations
- Implement intelligent password throttling mechanisms such as those which take IP address into account, in addition to the login name.
- When implementing security features, consider how they can be misused and made to turn on themselves.

## Related weaknesses (CWE)
- [CWE-645](https://cwe.mitre.org/data/definitions/645.html)

## Related ATT&CK techniques
- T1531

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/2.html
