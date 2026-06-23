---
cwe_id: CWE-645
name: Overly Restrictive Account Lockout Mechanism
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-2]
url: https://cwe.mitre.org/data/definitions/645.html
tags: [mitre-cwe, weakness, CWE-645]
---

# CWE-645 - Overly Restrictive Account Lockout Mechanism

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-645](https://cwe.mitre.org/data/definitions/645.html)

## Description
The product contains an account lockout protection mechanism, but the mechanism is too restrictive and can be triggered too easily, which allows attackers to deny service to legitimate users by causing their accounts to be locked out.

## Extended description
Account lockout is a security feature often present in applications as a countermeasure to the brute force attack on the password based authentication mechanism of the system. After a certain number of failed login attempts, the users' account may be disabled for a certain period of time or until it is unlocked by an administrator. Other security events may also possibly trigger account lockout. However, an attacker may use this very security feature to deny service to legitimate system users. It is therefore important to ensure that the account lockout security mechanism is not overly restrictive.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design**: Implement more intelligent password throttling mechanisms such as those which take IP address into account, in addition to the login name.
- **Architecture and Design**: Implement a lockout timeout that grows as the number of incorrect login attempts goes up, eventually resulting in a complete lockout.
- **Architecture and Design**: Consider alternatives to account lockout that would still be effective against password brute force attacks, such as presenting the user machine with a puzzle to solve (makes it do some computation).

## Related attack patterns (CAPEC)
- [CAPEC-2](https://capec.mitre.org/data/definitions/2.html)

## Related weaknesses
- CWE-287 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/645.html
