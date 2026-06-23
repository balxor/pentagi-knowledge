---
capec_id: CAPEC-652
name: Use of Known Kerberos Credentials
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-522, CWE-307, CWE-308, CWE-309, CWE-262, CWE-263, CWE-654, CWE-294, CWE-836]
related_attack: [T1558]
url: https://capec.mitre.org/data/definitions/652.html
tags: [mitre-capec, attack-pattern, CAPEC-652]
---

# CAPEC-652 - Use of Known Kerberos Credentials

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-652](https://capec.mitre.org/data/definitions/652.html)

## Description
An adversary obtains (i.e. steals or purchases) legitimate Kerberos credentials (e.g. Kerberos service account userID/password or Kerberos Tickets) with the goal of achieving authenticated access to additional systems, applications, or services within the domain.

## Extended description
Kerberos is the default authentication method for Windows domains and is also used across many operating systems. Attacks leveraging trusted Kerberos credentials can result in numerous consequences, depending on what Kerberos credential is stolen. For example, Kerberos service accounts are typically used to run services or scheduled tasks pertaining to authentication. However, these credentials are often weak and never expire, in addition to possessing local or domain administrator privileges. If an adversary is able to acquire these credentials, it could result in lateral movement within the domain or access to any resources the service account is privileged to access, among other things. Ultimately, successful spoofing and impersonation of trusted Kerberos credentials can lead to an adversary breaking authentication, authorization, and audit controls with the target system or application.

## Prerequisites
- The system/application leverages Kerberos authentication.
- The system/application uses one factor password-based authentication, SSO, and/or cloud-based authentication for Kerberos service accounts.
- The system/application does not have a sound password policy that is being enforced for Kerberos service accounts.
- The system/application does not implement an effective password throttling mechanism for authenticating to Kerberos service accounts.
- The targeted network allows for network sniffing attacks to succeed.

## Skills required
- **Low**: Once an adversary obtains a known Kerberos credential, leveraging it is trivial.

## Resources required
- A valid Kerberos ticket or a known Kerberos service account credential.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Read Data
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Acquire known Kerberos credentials: The adversary must obtain known Kerberos credentials in order to access the target system, application, or service within the domain. Techniques An adversary purchases breached Kerberos service account username/password combinations or leaked hashed passwords from the dark web. An adversary guesses the credentials to a weak Kerberos service account. An adversary conducts a sniffing attack to steal Kerberos tickets as they are transmitted. An adversary conducts a Kerberoasting attack. Experiment Attempt Kerberos authentication: Try each Kerberos credential against various resources within the domain until the target grants access. Techniques Manually or automatically enter each Kerberos service account credential through the target's interface. Attempt a Pass the Ticket attack. Exploit Impersonate: An adversary can use successful experiments or authentications to impersonate an authorized user or system, or to laterally move within the domain Spoofing: Malicious data can be injected into the target system or into other systems on the domain. The adversary can also pose as a legitimate domain user to perform social engineering attacks. Data Exfiltration: The adversary can obtain sensitive data contained within domain systems or applications.

## Mitigations
- Create a strong password policy and ensure that your system enforces this policy for Kerberos service accounts.
- Ensure Kerberos service accounts are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse Kerberos service account credentials across systems.
- Deny remote use of Kerberos service account credentials to log into domain systems.
- Do not allow Kerberos service accounts to be a local administrator on more than one system.
- Enable at least AES Kerberos encryption for tickets.
- Monitor system and domain logs for abnormal credential access.

## Related weaknesses (CWE)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-307](https://cwe.mitre.org/data/definitions/307.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-654](https://cwe.mitre.org/data/definitions/654.html)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-836](https://cwe.mitre.org/data/definitions/836.html)

## Related ATT&CK techniques
- T1558

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/652.html
