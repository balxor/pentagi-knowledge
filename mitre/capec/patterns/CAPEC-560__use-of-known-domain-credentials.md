---
capec_id: CAPEC-560
name: Use of Known Domain Credentials
type: attack-pattern
abstraction: Meta
likelihood: High
severity: High
related_cwe: [CWE-522, CWE-307, CWE-308, CWE-309, CWE-262, CWE-263, CWE-654, CWE-1273]
related_attack: [T1078]
url: https://capec.mitre.org/data/definitions/560.html
tags: [mitre-capec, attack-pattern, CAPEC-560]
---

# CAPEC-560 - Use of Known Domain Credentials

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-560](https://capec.mitre.org/data/definitions/560.html)

## Description
<xhtml:p>An adversary guesses or obtains (i.e. steals or purchases) legitimate credentials (e.g. userID/password) to achieve authentication and to perform authorized actions under the guise of an authenticated user or service.</xhtml:p>

## Extended description
Attacks leveraging trusted credentials typically result in the adversary laterally moving within the local network, since users are often allowed to login to systems/applications within the network using the same password. This further allows the adversary to obtain sensitive data, download/install malware on the system, pose as a legitimate user for social engineering purposes, and more. Attacks on known passwords generally rely on the primary fact that users often reuse the same username/password combination for a variety of systems, applications, and services, coupled with poor password policies on the target system or application. Adversaries can also utilize known passwords to target Single Sign On (SSO) or cloud-based applications and services, which often don't verify the authenticity of the user's input. Known credentials are usually obtained by an adversary via a system/application breach and/or by purchasing dumps of credentials on the dark web. These credentials may be further gleaned via exposed configuration and properties files that contain system passwords, database connection strings, and other sensitive data.

## Prerequisites
- The system/application uses one factor password based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills required
- **Low**: Once an adversary obtains a known credential, leveraging it is trivial.

## Resources required
- A list of known credentials.
- A custom script that leverages the credential list to launch an attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Read Data
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Acquire known credentials: The adversary must obtain known credentials in order to access the target system, application, or service. Techniques An adversary purchases breached username/password combinations or leaked hashed passwords from the dark web. An adversary leverages a key logger or phishing attack to steal user credentials as they are provided. An adversary conducts a sniffing attack to steal credentials as they are transmitted. An adversary gains access to a database and exfiltrates password hashes. An adversary examines outward-facing configuration and properties files to discover hardcoded credentials. Determine target's password policy: Determine the password policies of the target system/application to determine if the known credentials fit within the specified criteria. Techniques Determine minimum and maximum allowed password lengths. Determine format of allowed passwords (whether they are required or allowed to contain numbers, special characters, etc., or whether they are allowed to contain words from the dictionary). Determine account lockout policy (a strict account lockout policy will prevent brute force attacks if multiple passwords are known for a single user account). Experiment Attempt authentication: Try each credential until the target grants access. Techniques Manually or automatically enter each credential through the target's interface. Exploit Impersonate: An adversary can use successful experiments or authentications to impersonate an authorized user or system, or to laterally move within a system or application Spoofing: Malicious data can be injected into the target system or into a victim user's system by an adversary. The adversary can also pose as a legitimate user to perform social engineering attacks. Data Exfiltration: The adversary can obtain sensitive data contained within the system or application.

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
- [CWE-1273](https://cwe.mitre.org/data/definitions/1273.html)

## Related ATT&CK techniques
- T1078

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/560.html
