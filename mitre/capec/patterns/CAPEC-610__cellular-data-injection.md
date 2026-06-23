---
capec_id: CAPEC-610
name: Cellular Data Injection
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/610.html
tags: [mitre-capec, attack-pattern, CAPEC-610]
---

# CAPEC-610 - Cellular Data Injection

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-610](https://capec.mitre.org/data/definitions/610.html)

## Description
Adversaries inject data into mobile technology traffic (data flows or signaling data) to disrupt communications or conduct additional surveillance operations.

## Prerequisites
- None

## Skills required
- **High**: Often achieved by nation states in conjunction with commercial cellular providers to conduct cellular traffic intercept and possible traffic injection.

## Consequences
- **Availability**: Resource Consumption (Attackers can disrupt or deny mobile technology communications and operations.), Modify Data (Attackers can inject false data into data or signaling system data flows of communications and operations, or re-route data flows or signaling data for the purpose of further data intercept and capture.)

## Mitigations
- Commercial defensive technology to detect and alert to any attempts to modify mobile technology data flows or to inject new data into existing data flows and signaling data.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/610.html
