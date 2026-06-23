---
capec_id: CAPEC-16
name: Dictionary-based Password Attack
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-521, CWE-262, CWE-263, CWE-654, CWE-307, CWE-308, CWE-309]
related_attack: []
url: https://capec.mitre.org/data/definitions/16.html
tags: [mitre-capec, attack-pattern, CAPEC-16]
---

# CAPEC-16 - Dictionary-based Password Attack

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-16](https://capec.mitre.org/data/definitions/16.html)

## Description
<xhtml:p>An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern.</xhtml:p>
            <xhtml:p>Dictionary Attacks differ from similar attacks such as Password Spraying (CAPEC-565) and Credential Stuffing (CAPEC-600), since they leverage unknown username/password combinations and don't care about inducing account lockouts.</xhtml:p>

## Prerequisites
- The system uses one factor password based authentication.
- The system does not have a sound password policy that is being enforced.
- The system does not implement an effective password throttling mechanism.

## Skills required
- **Low**: A variety of password cracking tools and dictionaries are available to launch this type of an attack.

## Resources required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD). Applicable dictionaries are required. Also a password cracking tool or a custom script that leverages the dictionary database to launch the attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Determine application's/system's password policy: Determine the password policies of the target application/system. Techniques Determine minimum and maximum allowed password lengths. Determine format of allowed passwords (whether they are required or allowed to contain numbers, special characters, etc., or whether they are allowed to contain words from the dictionary). Determine account lockout policy (a strict account lockout policy will prevent brute force attacks). Select dictionaries: Pick the dictionaries to be used in the attack (e.g. different languages, specific terminology, etc.) Techniques Select dictionary based on particular users' preferred languages. Select dictionary based on the application/system's supported languages. Determine username(s) to target: Determine username(s) whose passwords to crack. Techniques Obtain username(s) by sniffing network packets. Obtain username(s) by querying application/system (e.g. if upon a failed login attempt, the system indicates whether the entered username was valid or not) Obtain usernames from filesystem (e.g. list of directories in C:\Documents and Settings\ in Windows, and list in /etc/passwd in UNIX-like systems) Exploit Use dictionary to crack passwords.: Use a password cracking tool that will leverage the dictionary to feed passwords to the system and see if they work. Techniques Try all words in the dictionary, as well as common misspellings of the words as passwords for the chosen username(s). Try common combinations of words in the dictionary, as well as common misspellings of the combinations as passwords for the chosen username(s).

## Mitigations
- Create a strong password policy and ensure that your system enforces this policy.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Leverage multi-factor authentication for all authentication services.

## Related weaknesses (CWE)
- [CWE-521](https://cwe.mitre.org/data/definitions/521.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-654](https://cwe.mitre.org/data/definitions/654.html)
- [CWE-307](https://cwe.mitre.org/data/definitions/307.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/16.html
