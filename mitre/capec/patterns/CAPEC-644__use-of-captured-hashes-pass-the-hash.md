---
capec_id: CAPEC-644
name: Use of Captured Hashes (Pass The Hash)
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-522, CWE-836, CWE-308, CWE-294, CWE-308]
related_attack: [T1550.002]
url: https://capec.mitre.org/data/definitions/644.html
tags: [mitre-capec, attack-pattern, CAPEC-644]
---

# CAPEC-644 - Use of Captured Hashes (Pass The Hash)

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-644](https://capec.mitre.org/data/definitions/644.html)

## Description
An adversary obtains (i.e. steals or purchases) legitimate Windows domain credential hash values to access systems within the domain that leverage the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols.

## Extended description
When authenticating via LM or NTLM, an authenticating account's plaintext credentials are not required by the protocols for successful authentication. Instead, the hashed credentials are used to determine if an authentication attempt is valid. If an adversary can obtain an account's hashed credentials, the hash values can then be passed to a system or service to authenticate, without needing to brute-force the hashes to obtain their cleartext values. Successful Pass The Hash attacks result in the adversary fully authenticating as the targeted account, which can further allow the adversary to laterally move within the network, impersonate a legitimate user, and/or download/install malware to systems within the domain. This technique can be performed against any operating system that leverages the LM or NTLM protocols even if the operating system is not Windows-based, since these systems/accounts may still authenticate to a Windows domain.

## Prerequisites
- The system/application is connected to the Windows domain.
- The system/application leverages the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols.
- The adversary possesses known Windows credential hash value pairs that exist on the target domain.

## Skills required
- **Low**: Once an adversary obtains a known Windows credential hash value pair, leveraging it is trivial.

## Resources required
- A list of known Window credential hash value pairs for the targeted domain.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Read Data
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Acquire known Windows credential hash value pairs: The adversary must obtain known Windows credential hash value pairs of accounts that exist on the domain. Techniques An adversary purchases breached Windows credential hash value pairs from the dark web. An adversary conducts a sniffing attack to steal Windows credential hash value pairs as they are transmitted. An adversary gains access to a Windows domain system/files and exfiltrates Windows credential hash value pairs. An adversary examines outward-facing configuration and properties files to discover hardcoded Windows credential hash value pairs. Experiment Attempt domain authentication: Try each Windows credential hash value pair until the target grants access. Techniques Manually or automatically enter each Windows credential hash value pair through the target's interface. Exploit Impersonate: An adversary can use successful experiments or authentications to impersonate an authorized user or system, or to laterally move within the domain Spoofing: Malicious data can be injected into the target system or into other systems on the domain. The adversary can also pose as a legitimate domain user to perform social engineering attacks. Data Exfiltration: The adversary can obtain sensitive data contained within domain systems or applications.

## Mitigations
- Prevent the use of Lan Man and NT Lan Man authentication on severs and apply patch KB2871997 to Windows 7 and higher systems.
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Monitor system and domain logs for abnormal credential access.
- Create a strong password policy and ensure that your system enforces this policy.
- Leverage system penetration testing and other defense in depth methods to determine vulnerable systems within a domain.

## Related weaknesses (CWE)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-836](https://cwe.mitre.org/data/definitions/836.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-308](https://cwe.mitre.org/data/definitions/308.html)

## Related ATT&CK techniques
- T1550.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/644.html
