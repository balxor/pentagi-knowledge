---
capec_id: CAPEC-565
name: Password Spraying
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-521, CWE-262, CWE-263, CWE-654, CWE-307, CWE-308, CWE-309]
related_attack: [T1110.003]
url: https://capec.mitre.org/data/definitions/565.html
tags: [mitre-capec, attack-pattern, CAPEC-565]
---

# CAPEC-565 - Password Spraying

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-565](https://capec.mitre.org/data/definitions/565.html)

## Description
<xhtml:p>In a Password Spraying attack, an adversary tries a small list (e.g. 3-5) of common or expected passwords, often matching the target's complexity policy, against a known list of user accounts to gain valid credentials. The adversary tries a particular password for each user account, before moving onto the next password in the list. This approach assists the adversary in remaining undetected by avoiding rapid or frequent account lockouts. The adversary may then reattempt the process with additional passwords, once enough time has passed to prevent inducing a lockout.</xhtml:p>

## Extended description
Password Spraying attacks often target management services over commonly used ports such as SSH, FTP, Telnet, LDAP, Kerberos, MySQL, and more. Additional targets include Single Sign-On (SSO) or cloud-based applications/services that utilize federated authentication protocols, and externally facing applications. Successful execution of Password Spraying attacks usually lead to lateral movement within the target, which allows the adversary to impersonate the victim or execute any action that the victim is authorized to perform. If the password chosen by the user is commonly used or easily guessed, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern. Password Spraying Attacks are similar to Dictionary-based Password Attacks (CAPEC-16) in that they both leverage precompiled lists (i.e. dictionaries) of username/password combinations to try against a system/application. The primary difference is that Password Spraying Attacks leverage a known list of user accounts and only try one password for each account before moving onto the next password. In contrast, Dictionary-based Password Attacks leverage unknown username/password combinations and are often executed offline against files containing hashed credentials, where inducing an account lockout is not a concern. Password Spraying Attacks are also similar to Credential Stuffing attacks (CAPEC-600), since both utilize known user accounts and often attack the same targets. Credential Stuffing attacks, however, leverage known username/password combinations, whereas Password Spraying attacks have no insight into known username/password pairs. If a Password Spraying attack succeeds, it may additionally lead to Credential Stuffing attacks on different targets.

## Prerequisites
- The system/application uses one factor password based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts on the target system/application.

## Skills required
- **Low**: A Password Spraying attack is very straightforward. A variety of password cracking tools are widely available.

## Resources required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD).
- Applicable password lists.
- A password cracking tool or a custom script that leverages the password list to launch the attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Read Data
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Determine target's password policy: Determine the password policies of the target system/application. Techniques Determine minimum and maximum allowed password lengths. Determine format of allowed passwords (whether they are required or allowed to contain numbers, special characters, etc., or whether they are allowed to contain words from the dictionary). Determine account lockout policy (a strict account lockout policy will prevent brute force attacks). Select passwords: Pick the passwords to be used in the attack (e.g. commonly used passwords, passwords tailored to individual users, etc.) Techniques Select passwords based on common use or a particular user's additional details. Select passwords based on the target's password complexity policies. Exploit Brute force password: Given the finite space of possible passwords dictated by information determined in the previous steps, try each password for all known user accounts until the target grants access. Techniques Manually or automatically enter the first password for each known user account through the target's interface. In most systems, start with the shortest and simplest possible passwords, because most users tend to select such passwords if allowed to do so. Iterate through the remaining passwords for each known user account.

## Mitigations
- Create a strong password policy and ensure that your system enforces this policy.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.

## Related weaknesses (CWE)
- [CWE-521](https://cwe.mitre.org/data/definitions/521.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-654](https://cwe.mitre.org/data/definitions/654.html)
- [CWE-307](https://cwe.mitre.org/data/definitions/307.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)

## Related ATT&CK techniques
- T1110.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/565.html
