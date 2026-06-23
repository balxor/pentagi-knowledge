---
capec_id: CAPEC-548
name: Contaminate Resource
type: attack-pattern
abstraction: Meta
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/548.html
tags: [mitre-capec, attack-pattern, CAPEC-548]
---

# CAPEC-548 - Contaminate Resource

**Abstraction:** Meta  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-548](https://capec.mitre.org/data/definitions/548.html)

## Description
An adversary contaminates organizational information systems (including devices and networks) by causing them to handle information of a classification/sensitivity for which they have not been authorized. When this happens, the contaminated information system, device, or network must be brought offline to investigate and mitigate the data spill, which denies availability of the system until the investigation is complete.

## Extended description
Contamination through email is a very common attack vector. Systems with email servers or personal work systems using email are susceptible to this attack simply by receiving an email that contains a classified document or information. A fake classified document could even be used that is mistaken as true classified material. This would still cause the system to be taken offline until the validity of the classified material is confirmed.

## Prerequisites
- The adversary needs to have real or fake classified/sensitive information to place on a system

## Skills required
- **High**: The ability to obtain a classified document or information
- **Low**: The ability to fake a classified document

## Consequences
- **Availability**: Resource Consumption (Denial of Service)
- **Confidentiality**: Read Data (Victims of the attack can be exposed to classified materials)

## Mitigations
- Properly safeguard classified/sensitive data. This includes training cleared individuals to ensure they are handling and disposing of this data properly, as well as ensuring systems only handle information of the classification level they are designed for.
- Design systems with redundancy in mind. This could mean creating backing servers that could be switched over to in the event that a server has to be taken down for investigation.
- Have a planned and efficient response plan to limit the amount of time a system is offline while the contamination is investigated.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/548.html
