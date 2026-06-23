---
capec_id: CAPEC-55
name: Rainbow Table Password Cracking
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Medium
related_cwe: [CWE-261, CWE-521, CWE-262, CWE-263, CWE-654, CWE-916, CWE-308, CWE-309]
related_attack: [T1110.002]
url: https://capec.mitre.org/data/definitions/55.html
tags: [mitre-capec, attack-pattern, CAPEC-55]
---

# CAPEC-55 - Rainbow Table Password Cracking

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-55](https://capec.mitre.org/data/definitions/55.html)

## Description
An attacker gets access to the database table where hashes of passwords are stored. They then use a rainbow table of pre-computed hash chains to attempt to look up the original password. Once the original password corresponding to the hash is obtained, the attacker uses the original password to gain access to the system.

## Extended description
A password rainbow table stores hash chains for various passwords. A password chain is computed, starting from the original password, P, via a reduce(compression) function R and a hash function H. A recurrence relation exists where Xi+1 = R(H(Xi)), X0 = P. Then the hash chain of length n for the original password P can be formed: X1, X2, X3, ... , Xn-2, Xn-1, Xn, H(Xn). P and H(Xn) are then stored together in the rainbow table. Constructing the rainbow tables takes a very long time and is computationally expensive. A separate table needs to be constructed for the various hash algorithms (e.g. SHA1, MD5, etc.). However, once a rainbow table is computed, it can be very effective in cracking the passwords that have been hashed without the use of salt.

## Prerequisites
- Hash of the original password is available to the attacker. For a better chance of success, an attacker should have more than one hash of the original password, and ideally the whole table.
- Salt was not used to create the hash of the original password. Otherwise the rainbow tables have to be re-computed, which is very expensive and will make the attack effectively infeasible (especially if salt was added in iterations).
- The system uses one factor password based authentication.

## Skills required
- **Low**: A variety of password cracking tools are available that can leverage a rainbow table. The more difficult part is to obtain the password hash(es) in the first place.

## Resources required
- Rainbow table of password hash chains with the right algorithm used. A password cracking tool that leverages this rainbow table will also be required. Hash(es) of the password is required.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Execution flow
Execution Flow Explore Determine application's/system's password policy: Determine the password policies of the target application/system. Techniques Determine minimum and maximum allowed password lengths. Determine format of allowed passwords (whether they are required or allowed to contain numbers, special characters, etc.). Determine account lockout policy (a strict account lockout policy will prevent brute force attacks). Obtain password hashes: An attacker gets access to the database table storing hashes of passwords or potentially just discovers a hash of an individual password. Techniques Obtain copy of database table or flat file containing password hashes (by breaking access controls, using SQL Injection, etc.) Obtain password hashes from platform-specific storage locations (e.g. Windows registry) Sniff network packets containing password hashes. Exploit Run rainbow table-based password cracking tool: An attacker finds or writes a password cracking tool that uses a previously computed rainbow table for the right hashing algorithm. It helps if the attacker knows what hashing algorithm was used by the password system. Techniques Run rainbow table-based password cracking tool such as Ophcrack or RainbowCrack. Reduction function must depend on application's/system's password policy.

## Mitigations
- Use salt when computing password hashes. That is, concatenate the salt (random bits) with the original password prior to hashing it.

## Related weaknesses (CWE)
- [CWE-261](https://cwe.mitre.org/data/definitions/261.html)
- [CWE-521](https://cwe.mitre.org/data/definitions/521.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-654](https://cwe.mitre.org/data/definitions/654.html)
- [CWE-916](https://cwe.mitre.org/data/definitions/916.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)

## Related ATT&CK techniques
- T1110.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/55.html
