---
capec_id: CAPEC-522
name: Malicious Hardware Component Replacement
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.003]
url: https://capec.mitre.org/data/definitions/522.html
tags: [mitre-capec, attack-pattern, CAPEC-522]
---

# CAPEC-522 - Malicious Hardware Component Replacement

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-522](https://capec.mitre.org/data/definitions/522.html)

## Description
An adversary replaces legitimate hardware in the system with faulty counterfeit or tampered hardware in the supply chain distribution channel, with purpose of causing malicious disruption or allowing for additional compromise when the system is deployed.

## Prerequisites
- Physical access to the system after it has left the manufacturer but before it is deployed at the victim location.

## Skills required
- **High**: Hardware creation and manufacture of replacement components.

## Execution flow
Execution Flow Explore Determine Target Hardware: The adversary must first identify a system that they wish to target, and a specific hardware component that they can swap out with a malicious replacement. Techniques Look for datasheets containing the system schematics that can help identify possible target hardware. Procure a system and inspect it manually, looking for possible hardware component targets. Search for manufacturer IDs on hardware chips or FCC IDs on wireless chips to determine their functionality. Discover Vulnerability in Supply Chain: The adversary maps out the supply chain for the targeted system. They look for ooportunities to gain physical access to the system after it has left the manufacturer, but before it is deployed to the victim. Techniques Procure a system and observe the steps it takes in the shipment process. Identify possible warehouses that systems are stored after manufacturing. Experiment Test a Malicious Component Replacement: Before performing the attack in the wild, an adversary will test the attack on a system they have procured to ensure that the desired outcome will be achieved. Techniques Design a malicious hardware component that will perform the same functionality as the target component, but also contains additional functionality. Obtain already designed malicious components that just need to be placed into the system. Exploit Substitute Components in the Supply Chain: Using the vulnerability in the supply chain of the system discovered in the explore phase, the adversary substitutes the malicious component for the targeted component. This results in the adversary gaining unintended access to systems once they reach the victim and can lead to a variety of follow up attacks.

## Mitigations
- Ensure that all contractors and sub-suppliers use trusted means of shipping (e.g., bonded/cleared/vetted and insured couriers) to ensure that components, once purchased, are not subject to compromise during their delivery.
- Prevent or detect tampering with critical hardware or firmware components while in transit through use of state-of-the-art anti-tamper devices.
- Use tamper-resistant and tamper-evident packaging when shipping critical components (e.g., plastic coating for circuit boards, tamper tape, paint, sensors, and/or seals for cases and containers) and inspect received system components for evidence of tampering.

## Related ATT&CK techniques
- T1195.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/522.html
