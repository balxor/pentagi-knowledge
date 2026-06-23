---
capec_id: CAPEC-443
name: Malicious Logic Inserted Into Product by Authorized Developer
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: []
related_attack: [T1195.002, T1195.003]
url: https://capec.mitre.org/data/definitions/443.html
tags: [mitre-capec, attack-pattern, CAPEC-443]
---

# CAPEC-443 - Malicious Logic Inserted Into Product by Authorized Developer

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-443](https://capec.mitre.org/data/definitions/443.html)

## Description
An adversary uses their privileged position within an authorized development organization to inject malicious logic into a codebase or product.

## Extended description
Supply chain attacks from approved or trusted developers are extremely difficult to detect as it is generally assumed the quality control and internal security measures of these organizations conform to best practices. In some cases the malicious logic is intentional, embedded by a disgruntled employee, programmer, or individual with an otherwise hidden agenda. In other cases, the integrity of the product is compromised by accident (e.g. by lapse in the internal security of the organization that results in a product becoming contaminated). In further cases, the developer embeds a backdoor into a product to serve some purpose, such as product support, but discovery of the backdoor results in its malicious use by adversaries. It is also worth noting that this attack can occur during initial product development or throughout a product's sustainment.

## Prerequisites
- Access to the product during the initial or continuous development.

## Consequences
- **Authorization**: Execute Unauthorized Commands

## Mitigations
- Assess software and hardware during development and prior to deployment to ensure that it functions as intended and without any malicious functionality. This includes both initial development, as well as updates propagated to the product after deployment.

## Related ATT&CK techniques
- T1195.002
- T1195.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/443.html
