---
capec_id: CAPEC-446
name: Malicious Logic Insertion into Product via Inclusion of Third-Party Component
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: []
related_attack: [T1195]
url: https://capec.mitre.org/data/definitions/446.html
tags: [mitre-capec, attack-pattern, CAPEC-446]
---

# CAPEC-446 - Malicious Logic Insertion into Product via Inclusion of Third-Party Component

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-446](https://capec.mitre.org/data/definitions/446.html)

## Description
<xhtml:p>An adversary conducts supply chain attacks by the inclusion of insecure third-party components into a technology, product, or code-base, possibly packaging a malicious driver or component along with the product before shipping it to the consumer or acquirer.</xhtml:p>

## Extended description
The result is a window of opportunity for exploiting the product until the insecure component is discovered. This supply chain threat can result in the installation of malicious software or hardware that introduces widespread security vulnerabilities within an organization. Additionally, because software often depends upon a large number of interdependent libraries and components to be present, security holes can be introduced merely by installing Commercial off the Shelf (COTS) or Open Source Software (OSS) software that comes pre-packaged with the components required for it to operate. It is also worth noting that this attack can occur during initial product development or throughout a product's sustainment.

## Prerequisites
- Access to the product during the initial or continuous development. This access is often obtained via insider access to include the third-party component after deployment.

## Consequences
- **Authorization**: Execute Unauthorized Commands

## Mitigations
- Assess software and hardware during development and prior to deployment to ensure that it functions as intended and without any malicious functionality. This includes both initial development, as well as updates propagated to the product after deployment.
- Don't assume popular third-party components are free from malware or vulnerabilities. For software, assess for malicious functionality via update/commit reviews or automated static/dynamic analysis prior to including the component within the application and deploying in a production environment.

## Related ATT&CK techniques
- T1195

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/446.html
