---
capec_id: CAPEC-662
name: Adversary in the Browser (AiTB)
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-300, CWE-494]
related_attack: [T1185]
url: https://capec.mitre.org/data/definitions/662.html
tags: [mitre-capec, attack-pattern, CAPEC-662]
---

# CAPEC-662 - Adversary in the Browser (AiTB)

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-662](https://capec.mitre.org/data/definitions/662.html)

## Description
<xhtml:p>An adversary exploits security vulnerabilities or inherent functionalities of a web browser, in order to manipulate traffic between two endpoints.</xhtml:p>

## Extended description
This attack first requires the adversary to trick the victim into installing a Trojan Horse application on their system, such as a malicious web browser plugin, which the adversary then leverages to mount the attack. The victim interacts with a web application, such as a banking website, in a normal manner and under the assumption that the connection is secure. However, the adversary can now alter and/or reroute traffic between the client application (e.g., web browser) and the coinciding endpoint, while simultaneously displaying intended transactions and data back to the user. The adversary may also be able to glean cookies, HTTP sessions, and SSL client certificates, which can be used to pivot into an authenticated intranet. Identifying AITB is often difficult because these attacks are successful even when security mechanisms such as SSL/PKI and multifactor authentication are present, since they still function as intended during the attack.

## Prerequisites
- The adversary must install or convince a user to install a Trojan.
- There are two components communicating with each other.
- An attacker is able to identify the nature and mechanism of communication between the two target components.
- Strong mutual authentication is not used between the two target components yielding opportunity for adversarial interposition.
- For browser pivoting, the SeDebugPrivilege and a high-integrity process must both exist to execute this attack.

## Skills required
- **Medium**: Tricking the victim into installing the Trojan is often the most difficult aspect of this attack. Afterwards, the remainder of this attack is fairly trivial.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Experiment The adversary tricks the victim into installing the Trojan Horse malware onto their system. Techniques Conduct phishing attacks, drive-by malware installations, or masquerade malicious browser extensions as being legitimate. The adversary inserts themself into the communication channel initially acting as a routing proxy between the two targeted components. Exploit The adversary observes, filters, or alters passed data of their choosing to gain access to sensitive information or to manipulate the actions of the two target components for their own purposes.

## Mitigations
- Ensure software and applications are only downloaded from legitimate and reputable sources, in addition to conducting integrity checks on the downloaded component.
- Leverage anti-malware tools, which can detect Trojan Horse malware.
- Use strong, out-of-band mutual authentication to always fully authenticate both ends of any communications channel.
- Limit user permissions to prevent browser pivoting.
- Ensure browser sessions are regularly terminated and when their effective lifetime ends.

## Related weaknesses (CWE)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)

## Related ATT&CK techniques
- T1185

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/662.html
