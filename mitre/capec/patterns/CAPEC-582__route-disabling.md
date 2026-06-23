---
capec_id: CAPEC-582
name: Route Disabling
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/582.html
tags: [mitre-capec, attack-pattern, CAPEC-582]
---

# CAPEC-582 - Route Disabling

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-582](https://capec.mitre.org/data/definitions/582.html)

## Description
An adversary disables the network route between two targets. The goal is to completely sever the communications channel between two entities. This is often the result of a major error or the use of an "Internet kill switch" by those in control of critical infrastructure. This attack pattern differs from most other obstruction patterns by targeting the route itself, as opposed to the data passed over the route.

## Prerequisites
- The adversary requires knowledge of and access to network route.

## Consequences
- **Availability**: Other (Disabling a network route denies the availability of a service.)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/582.html
