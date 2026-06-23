---
capec_id: CAPEC-523
name: Malicious Software Implanted
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.002]
url: https://capec.mitre.org/data/definitions/523.html
tags: [mitre-capec, attack-pattern, CAPEC-523]
---

# CAPEC-523 - Malicious Software Implanted

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-523](https://capec.mitre.org/data/definitions/523.html)

## Description
An attacker implants malicious software into the system in the supply chain distribution channel, with purpose of causing malicious disruption or allowing for additional compromise when the system is deployed.

## Prerequisites
- Physical access to the system after it has left the manufacturer but before it is deployed at the victim location.

## Skills required
- **High**: Malicious software creation.

## Execution flow
Execution Flow Explore Determine Entry Point: The adversary must first identify a system that they wish to target and search for an entry point they can use to install the malicious software. This could be a system which they have prior knowledge of, giving them insight into the software and environment. Techniques Use a JTAGulator to identify exposed JTAG and UART interfaces in smaller embedded systems. Identify exposed USB connectors that could be used to load software. Discover Vulnerability in Supply Chain: The adversary maps out the supply chain for the targeted system. They look for ooportunities to gain physical access to the system after it has left the manufacturer, but before it is deployed to the victim. Techniques Procure a system and observe the steps it takes in the shipment process. Identify possible warehouses that systems are stored after manufacturing. Experiment Test Malicious Software: Before performing the attack in the wild, an adversary will test the attack on a system they have procured to ensure that the desired outcome will be achieved. Techniques Design malicious software that will give an adversary a backdoor into the system once it is deployed to the victim. Obtain already designed malicious software that just need to be placed into the system. Exploit Implant Software in the Supply Chain: Using the vulnerability in the supply chain of the system discovered in the explore phase, the adversary implants the malicious software into the system. This results in the adversary gaining unintended access to systems once they reach the victim and can lead to a variety of follow up attacks.

## Mitigations
- Deploy strong code integrity policies to allow only authorized apps to run.
- Use endpoint detection and response solutions that can automaticalkly detect and remediate suspicious activities.
- Maintain a highly secure build and update infrastructure by immediately applying security patches for OS and software, implementing mandatory integrity controls to ensure only trusted tools run, and requiring multi-factor authentication for admins.
- Require SSL for update channels and implement certificate transparency based verification.
- Sign everything, including configuration files, XML files and packages.
- Develop an incident response process, disclose supply chain incidents and notify customers with accurate and timely information.

## Related ATT&CK techniques
- T1195.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/523.html
