---
capec_id: CAPEC-701
name: Browser in the Middle (BiTM)
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-294, CWE-345]
related_attack: []
url: https://capec.mitre.org/data/definitions/701.html
tags: [mitre-capec, attack-pattern, CAPEC-701]
---

# CAPEC-701 - Browser in the Middle (BiTM)

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-701](https://capec.mitre.org/data/definitions/701.html)

## Description
An adversary exploits the inherent functionalities of a web browser, in order to establish an unnoticed remote desktop connection in the victim's browser to the adversary's system. The adversary must deploy a web client with a remote desktop session that the victim can access.

## Extended description
Unlike Adversary in the Browser, the victim does not need to install a malicious application. Browser in the Middle uses the inherent functionalities of a web browser to convince the victim they are browsing normally under the assumption that the connection is secure. All the actions performed by the victim in the open window are actually performed on the machine of the adversary. These victim-authenticated sessions are available to the adversary to use. All entered data such as passwords and usernames can be logged by the adversary and the content displayed to the victim can be altered arbitrarily. Varieties of multifactor authentication which rely solely on user input and do not use a form of hardware-based secret exchange are vulnerable to browser in the middle.

## Prerequisites
- The adversary must create a convincing web client to establish the connection. The victim then needs to be lured onto the adversary's webpage. In addition, the victim's machine must not use local authentication APIs, a hardware token, or a Trusted Platform Module (TPM) to authenticate.

## Skills required
- **Medium**: 

## Resources required
- A web application with a client is needed to enable the victim's browser to establish a remote desktop connection to the system of the adversary.

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Read Data
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Identify potential targets: The adversary identifies an application or service that the target is likely to use. Techniques The adversary stands up a server to host the transparent browser and entices victims to use it by using a domain name similar to the legitimate application. In addition to the transparent browser, the adversary could also install a web proxy, sniffer, keylogger, and other tools to assist in their goals. Experiment Lure victims: The adversary crafts a phishing campaign to lure unsuspecting victims into using the transparent browser. Techniques An adversary can create a convincing email with a link to download the web client and interact with the transparent browser. Exploit Monitor and Manipulate Data: When the victim establishes the connection to the transparent browser, the adversary can view victim activity and make alterations to what the victim sees when browsing the web. Techniques Once a victim has established a connection to the transparent browser, the adversary can use installed tools such as a web proxy, keylogger, or additional malicious browser extensions to gather and manipulate data or impersonate the victim.

## Mitigations
- Implementation: Use strong, mutual authentication to fully authenticate with both ends of any communications channel

## Related weaknesses (CWE)
- [CWE-294](https://cwe.mitre.org/data/definitions/294.html)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/701.html
