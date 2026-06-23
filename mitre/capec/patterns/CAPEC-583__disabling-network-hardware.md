---
capec_id: CAPEC-583
name: Disabling Network Hardware
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/583.html
tags: [mitre-capec, attack-pattern, CAPEC-583]
---

# CAPEC-583 - Disabling Network Hardware

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-583](https://capec.mitre.org/data/definitions/583.html)

## Description
In this attack pattern, an adversary physically disables networking hardware by powering it down or disconnecting critical equipment. Disabling or shutting off critical system resources prevents them from performing their service as intended, which can have direct and indirect consequences on other systems. This attack pattern is considerably less technical than the selective blocking used in most obstruction attacks.

## Prerequisites
- The adversary requires physical access to the targeted communications equipment (networking devices, cables, etc.), which may be spread over a wide area.

## Consequences
- **Availability**: Other (Denial of Service)

## Mitigations
- Ensure rigorous physical defensive measures to keep the adversary from accessing critical systems..

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/583.html
