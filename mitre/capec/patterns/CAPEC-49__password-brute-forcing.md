---
capec_id: CAPEC-49
name: Password Brute Forcing
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-521, CWE-262, CWE-263, CWE-257, CWE-654, CWE-307, CWE-308, CWE-309]
related_attack: [T1110.001]
url: https://capec.mitre.org/data/definitions/49.html
tags: [mitre-capec, attack-pattern, CAPEC-49]
---

# CAPEC-49 - Password Brute Forcing

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-49](https://capec.mitre.org/data/definitions/49.html)

## Description
An adversary tries every possible value for a password until they succeed. A brute force attack, if feasible computationally, will always be successful because it will essentially go through all possible passwords given the alphabet used (lower case letters, upper case letters, numbers, symbols, etc.) and the maximum length of the password.

## Extended description
A system will be particularly vulnerable to this type of an attack if it does not have a proper enforcement mechanism in place to ensure that passwords selected by users are strong passwords that comply with an adequate password policy. In practice a pure brute force attack on passwords is rarely used, unless the password is suspected to be weak. Other password cracking methods exist that are far more effective (e.g. dictionary attacks, rainbow tables, etc.). Knowing the password policy on the system can make a brute force attack more efficient. For instance, if the policy states that all passwords must be of a certain level, there is no need to check smaller candidates.

## Prerequisites
- An adversary needs to know a username to target.
- The system uses password based authentication as the one factor authentication mechanism.
- An application does not have a password throttling mechanism in place. A good password throttling mechanism will make it almost impossible computationally to brute force a password as it may either lock out the user after a certain number of incorrect attempts or introduce time out periods. Both of these would make a brute force attack impractical.

## Skills required
- **Low**: A brute force attack is very straightforward. A variety of password cracking tools are widely available.

## Resources required
- A powerful enough computer for the job with sufficient CPU, RAM and HD. Exact requirements will depend on the size of the brute force job and the time requirement for completion. Some brute forcing jobs may require grid or distributed computing (e.g. DES Challenge).

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Determine application's/system's password policy: Determine the password policies of the target application/system. Techniques Determine minimum and maximum allowed password lengths. Determine format of allowed passwords (whether they are required or allowed to contain numbers, special characters, etc.). Determine account lockout policy (a strict account lockout policy will prevent brute force attacks). Exploit Brute force password: Given the finite space of possible passwords dictated by the password policy determined in the previous step, try all possible passwords for a known user ID until application/system grants access. Techniques Manually or automatically enter all possible passwords through the application/system's interface. In most systems, start with the shortest and simplest possible passwords, because most users tend to select such passwords if allowed to do so. Perform an offline dictionary attack or a rainbow table attack against a known password hash.

## Mitigations
- Implement a password throttling mechanism. This mechanism should take into account both the IP address and the log in name of the user.
- Put together a strong password policy and make sure that all user created passwords comply with it. Alternatively automatically generate strong passwords for users.
- Passwords need to be recycled to prevent aging, that is every once in a while a new password must be chosen.

## Related weaknesses (CWE)
- [CWE-521](https://cwe.mitre.org/data/definitions/521.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-257](https://cwe.mitre.org/data/definitions/257.html)
- [CWE-654](https://cwe.mitre.org/data/definitions/654.html)
- [CWE-307](https://cwe.mitre.org/data/definitions/307.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)

## Related ATT&CK techniques
- T1110.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/49.html
