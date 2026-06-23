---
capec_id: CAPEC-599
name: Terrestrial Jamming
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/599.html
tags: [mitre-capec, attack-pattern, CAPEC-599]
---

# CAPEC-599 - Terrestrial Jamming

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-599](https://capec.mitre.org/data/definitions/599.html)

## Description
In this attack pattern, the adversary transmits disruptive signals in the direction of the target's consumer-level satellite dish (as opposed to the satellite itself). The transmission disruption occurs in a more targeted range. Portable terrestrial jammers have a range of 3-5 kilometers in urban areas and 20 kilometers in rural areas. This technique requires a terrestrial jammer that is more powerful than the frequencies sent from the satellite.

## Resources required
- A terrestrial satellite jammer with a signal more powerful than that of the satellite attempting to communicate with the target. The adversary must know the location of the target satellite dish.

## Consequences
- **Availability**: Other (A successful attack will deny, degrade, or disrupt availability of satellite communications for the target by overwhelming its resources to accurately receive authorized transmissions.)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/599.html
