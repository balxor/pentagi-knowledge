---
capec_id: CAPEC-653
name: Use of Known Operating System Credentials
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-522, CWE-307, CWE-308, CWE-309, CWE-262, CWE-263, CWE-654]
related_attack: []
url: https://capec.mitre.org/data/definitions/653.html
tags: [mitre-capec, attack-pattern, CAPEC-653]
---

# CAPEC-653 - Use of Known Operating System Credentials

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-653](https://capec.mitre.org/data/definitions/653.html)

## Description
An adversary guesses or obtains (i.e. steals or purchases) legitimate operating system credentials (e.g. userID/password) to achieve authentication and to perform authorized actions on the system, under the guise of an authenticated user or service. This applies to any Operating System.

## Extended description
This attack can be extremely harmful when the operating system credentials used are for a root or admin user. Once an adversary gains access using credentials with elevated privileges, they are free to alter important system files which can effect other users who may use the system or other users on the system's network.

## Prerequisites
- The system/application uses one factor password-based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills required
- **Low**: Once an adversary obtains a known credential, leveraging it is trivial.

## Resources required
- A list of known credentials for the targeted domain.
- A custom script that leverages a credential list to launch an attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Read Data
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Acquire known operating system credentials: The adversary must obtain known operating system credentials in order to access the target system, application, or service within the domain. Techniques An adversary purchases breached operating system username/password combinations or leaked hashed passwords from the dark web. An adversary leverages a key logger or phishing attack to steal user credentials as they are provided. An adversary conducts a sniffing attack to steal operating system credentials as they are transmitted. An adversary gains access to a system/files and exfiltrates password hashes. An adversary examines outward-facing configuration and properties files to discover hardcoded credentials. Experiment Attempt authentication: Try each operating system credential against various systems, applications, and services within the domain until the target grants access. Techniques Manually or automatically enter each credential through the target's interface. Exploit Impersonate: An adversary can use successful experiments or authentications to impersonate an authorized user or system, or to laterally move within the network Spoofing: Malicious data can be injected into the target system or into other systems on the network. The adversary can also pose as a legitimate user to perform social engineering attacks. Data Exfiltration: The adversary can obtain sensitive data contained within system files or application configuration.

## Mitigations
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the network.
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

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/653.html
