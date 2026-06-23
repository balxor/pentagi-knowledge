---
capec_id: CAPEC-561
name: Windows Admin Shares with Stolen Credentials
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-522, CWE-308, CWE-309, CWE-294, CWE-263, CWE-262, CWE-521]
related_attack: [T1021.002]
url: https://capec.mitre.org/data/definitions/561.html
tags: [mitre-capec, attack-pattern, CAPEC-561]
---

# CAPEC-561 - Windows Admin Shares with Stolen Credentials

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-561](https://capec.mitre.org/data/definitions/561.html)

## Description
An adversary guesses or obtains (i.e. steals or purchases) legitimate Windows administrator credentials (e.g. userID/password) to access Windows Admin Shares on a local machine or within a Windows domain.

## Extended description
Windows systems within the Windows NT family contain hidden network shares that are only accessible to system administrators. These shares allow administrators to remotely access all disk volumes on a network-connected system and further allow for files to be copied, written, and executed, along with other administrative actions. Example network shares include: C$, ADMIN$ and IPC$. If an adversary is able to obtain legitimate Windows credentials, the hidden shares can be accessed remotely, via server message block (SMB) or the Net utility, to transfer files and execute code. It is also possible for adversaries to utilize NTLM hashes to access administrator shares on systems with certain configuration and patch levels.

## Prerequisites
- The system/application is connected to the Windows domain.
- The target administrative share allows remote use of local admin credentials to log into domain systems.
- The adversary possesses a list of known Windows administrator credentials that exist on the target domain.

## Skills required
- **Low**: Once an adversary obtains a known Windows credential, leveraging it is trivial.

## Resources required
- A list of known Windows administrator credentials for the targeted domain.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Read Data
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Acquire known Windows administrator credentials: The adversary must obtain known Windows administrator credentials in order to access the administrative network shares. Techniques An adversary purchases breached Windows administrator credentials from the dark web. An adversary leverages a key logger or phishing attack to steal administrator credentials as they are provided. An adversary conducts a sniffing attack to steal Windows administrator credentials as they are transmitted. An adversary gains access to a Windows domain system/files and exfiltrates Windows administrator password hashes. An adversary examines outward-facing configuration and properties files to discover hardcoded Windows administrator credentials. Experiment Attempt domain authentication: Try each Windows administrator credential against the hidden network shares until the target grants access. Techniques Manually or automatically enter each administrator credential through the target's interface. Exploit Malware Execution: An adversary can remotely execute malware within the administrative network shares to infect other systems within the domain. Data Exfiltration: The adversary can remotely obtain sensitive data contained within the administrative network shares.

## Mitigations
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.

## Related weaknesses (CWE)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-309](https://cwe.mitre.org/data/definitions/309.html)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-263](https://cwe.mitre.org/data/definitions/263.html)
- [CWE-262](https://cwe.mitre.org/data/definitions/262.html)
- [CWE-521](https://cwe.mitre.org/data/definitions/521.html)

## Related ATT&CK techniques
- T1021.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/561.html
