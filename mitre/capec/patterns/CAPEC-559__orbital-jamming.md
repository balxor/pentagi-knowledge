---
capec_id: CAPEC-559
name: Orbital Jamming
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/559.html
tags: [mitre-capec, attack-pattern, CAPEC-559]
---

# CAPEC-559 - Orbital Jamming

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-559](https://capec.mitre.org/data/definitions/559.html)

## Description
In this attack pattern, the adversary sends disruptive signals at a target satellite using a rogue uplink station to disrupt the intended transmission. Those within the satellite's footprint are prevented from reaching the satellite's targeted or neighboring channels. The satellite's footprint size depends upon its position in the sky; higher orbital satellites cover multiple continents.

## Prerequisites
- This attack requires the knowledge of the satellite's coordinates for targeting.

## Resources required
- A satellite uplink station.

## Consequences
- **Availability**: Other (A successful attack will deny the availability of the satellite communications for authorized users.)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/559.html
