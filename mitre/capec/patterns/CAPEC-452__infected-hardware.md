---
capec_id: CAPEC-452
name: Infected Hardware
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/452.html
tags: [mitre-capec, attack-pattern, CAPEC-452]
---

# CAPEC-452 - Infected Hardware

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-452](https://capec.mitre.org/data/definitions/452.html)

## Description
An adversary inserts malicious logic into hardware, typically in the form of a computer virus or rootkit. This logic is often hidden from the user of the hardware and works behind the scenes to achieve negative impacts. This pattern of attack focuses on hardware already fielded and used in operation as opposed to hardware that is still under development and part of the supply chain.

## Prerequisites
- Access to the hardware currently deployed at a victim location.

## Consequences
- **Authorization**: Execute Unauthorized Commands

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/452.html
