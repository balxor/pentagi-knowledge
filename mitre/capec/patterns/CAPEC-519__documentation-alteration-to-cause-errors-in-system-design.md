---
capec_id: CAPEC-519
name: Documentation Alteration to Cause Errors in System Design
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/519.html
tags: [mitre-capec, attack-pattern, CAPEC-519]
---

# CAPEC-519 - Documentation Alteration to Cause Errors in System Design

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-519](https://capec.mitre.org/data/definitions/519.html)

## Description
An attacker with access to a manufacturer's documentation containing requirements allocation and software design processes maliciously alters the documentation in order to cause errors in system design. This allows the attacker to take advantage of a weakness in a deployed system of the manufacturer for malicious purposes.

## Prerequisites
- Advanced knowledge of software capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills required
- **High**: Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations
- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain multiple instances of the document across different privileged users for recovery and verification.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/519.html
