---
capec_id: CAPEC-600
name: Credential Stuffing
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-522, CWE-307, CWE-308, CWE-309, CWE-262, CWE-263, CWE-654]
related_attack: [T1110.004]
url: https://capec.mitre.org/data/definitions/600.html
tags: [mitre-capec, attack-pattern, CAPEC-600]
---

# CAPEC-600 - Credential Stuffing

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-600](https://capec.mitre.org/data/definitions/600.html)

## Description
<xhtml:p>An adversary tries known username/password combinations against different systems, applications, or services to gain additional authenticated access. Credential Stuffing attacks rely upon the fact that many users leverage the same username/password combination for multiple systems, applications, and services.</xhtml:p>

## Extended description
Attacks of this kind often target management services over commonly used ports such as SSH, FTP, Telnet, LDAP, Kerberos, MySQL, and more. Additional targets include Single Sign-On (SSO) or cloud-based applications/services that utilize federated authentication protocols, and externally facing applications. The primary goal of Credential Stuffing is to achieve lateral movement and gain authenticated access to additional systems, applications, and/or services. A successfully executed Credential Stuffing attack could result in the adversary impersonating the victim or executing any action that the victim is authorized to perform. Although not technically a brute force attack, Credential Stuffing attacks can function as such if an adversary possess multiple known passwords for the same user account. This may occur in the event where an adversary obtains user credentials from multiple sources or if the adversary obtains a user's password history for an account. Credential Stuffing attacks are similar to Password Spraying attacks (CAPEC-565) regarding their targets and their overall goals. However, Password Spraying attacks do not have any insight into known username/password combinations and instead leverage common or expected passwords. This also means that Password Spraying attacks must avoid inducing account lockouts, which is generally not a worry of Credential Stuffing attacks. Password Spraying attacks may additionally lead to Credential Stuffing attacks, once a successful username/password combination is discovered.

## Prerequisites
- The system/application uses one factor password based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills required
- **Low**: A Credential Stuffing attack is very straightforward.

## Resources required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD).
- A known list of username/password combinations.
- A custom script that leverages the credential list to launch the attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Read Data
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Acquire known credentials: The adversary must obtain known credentials in order to access the target system, application, or service. Techniques An adversary purchases breached username/password combinations or leaked hashed passwords from the dark web. An adversary leverages a key logger or phishing attack to steal user credentials as they are provided. An adversary conducts a sniffing attack to steal credentials as they are transmitted. An adversary gains access to a database and exfiltrates password hashes. An adversary examines outward-facing configuration and properties files to discover hardcoded credentials. Determine target's password policy: Determine the password policies of the target system/application to determine if the known credentials fit within the specified criteria. Techniques Determine minimum and maximum allowed password lengths. Determine format of allowed passwords (whether they are required or allowed to contain numbers, special characters, etc., or whether they are allowed to contain words from the dictionary). Determine account lockout policy (a strict account lockout policy will prevent brute force attacks if multiple passwords are known for a single user account). Experiment Attempt authentication: Try each username/password combination until the target grants access. Techniques Manually or automatically enter each username/password combination through the target's interface. Exploit Impersonate: An adversary can use successful experiments or authentications to impersonate an authorized user or system or to laterally move within a system or application Spoofing: Malicious data can be injected into the target system or into a victim user's system by an adversary. The adversary can also pose as a legitimate user to perform social engineering attacks. Data Exfiltration: The adversary can obtain sensitive data contained within the system or application.

## Mitigations
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Create a strong password policy and ensure that your system enforces this policy.
- Ensure users are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Monitor system and domain logs for abnormal credential access.

## Related weaknesses (CWE)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-307](https://cwe.mitre.org/data/definitions/307.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-654](https://cwe.mitre.org/data/definitions/654.html)

## Related ATT&CK techniques
- T1110.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/600.html
