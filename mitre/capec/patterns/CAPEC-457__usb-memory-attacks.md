---
capec_id: CAPEC-457
name: USB Memory Attacks
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-1299]
related_attack: [T1091, T1092]
url: https://capec.mitre.org/data/definitions/457.html
tags: [mitre-capec, attack-pattern, CAPEC-457]
---

# CAPEC-457 - USB Memory Attacks

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-457](https://capec.mitre.org/data/definitions/457.html)

## Description
An adversary loads malicious code onto a USB memory stick in order to infect any system which the device is plugged in to. USB drives present a significant security risk for business and government agencies. Given the ability to integrate wireless functionality into a USB stick, it is possible to design malware that not only steals confidential data, but sniffs the network, or monitor keystrokes, and then exfiltrates the stolen data off-site via a Wireless connection. Also, viruses can be transmitted via the USB interface without the specific use of a memory stick. The attacks from USB devices are often of such sophistication that experts conclude they are not the work of single individuals, but suggest state sponsorship. These attacks can be performed by an adversary with direct access to a target system or can be executed via means such as USB Drop Attacks.

## Prerequisites
- Some level of physical access to the device being attacked.
- Information pertaining to the target organization on how to best execute a USB Drop Attack.

## Execution flow
Execution Flow Explore Determine Target System: In certain cases, the adversary will explore an organization's network to determine a specific target machine to exploit based on the information it contains or privileges the main user may possess. Techniques If needed, the adversary explores an organization's network to determine if any specific systems of interest exist. Experiment Develop or Obtain malware and install on a USB device: The adversary develops or obtains the malicious software necessary to exploit the target system, which they then install on an external USB device such as a USB flash drive. Techniques The adversary can develop or obtain malware for to perform a variety of tasks such as sniffing network traffic or monitoring keystrokes. Exploit Connect or deceive a user into connecting the infected USB device: Once the malware has been placed on an external USB device, the adversary connects the device to the target system or deceives a user into connecting the device to the target system such as in a USB Drop Attack. Techniques The adversary connects the USB device to a specified target system or performs a USB Drop Attack, hoping a user will find and connect the USB device on their own. Once the device is connected, the malware executes giving the adversary access to network traffic, credentials, etc.

## Mitigations
- Ensure that proper, physical system access is regulated to prevent an adversary from physically connecting a malicious USB device themself.
- Use anti-virus and anti-malware tools which can prevent malware from executing if it finds its way onto a target system. Additionally, make sure these tools are regularly updated to contain up-to-date virus and malware signatures.
- Do not connect untrusted USB devices to systems connected on an organizational network. Additionally, use an isolated testing machine to validate untrusted devices and confirm malware does not exist.

## Related weaknesses (CWE)
- [CWE-1299](https://cwe.mitre.org/data/definitions/1299.html)

## Related ATT&CK techniques
- T1091
- T1092

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/457.html
