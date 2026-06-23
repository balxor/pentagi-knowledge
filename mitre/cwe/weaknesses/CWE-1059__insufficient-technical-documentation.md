---
cwe_id: CWE-1059
name: Insufficient Technical Documentation
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1059.html
tags: [mitre-cwe, weakness, CWE-1059]
---

# CWE-1059 - Insufficient Technical Documentation

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1059](https://cwe.mitre.org/data/definitions/1059.html)

## Description
The product does not contain sufficient technical or engineering documentation (whether on paper or in electronic form) that contains descriptions of all the relevant software/hardware elements of the product, such as its usage, structure, architectural components, interfaces, design, implementation, configuration, operation, etc.

## Extended description
When technical documentation is limited or lacking, products are more difficult to maintain. This indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. When using time-limited or labor-limited third-party/in-house security consulting services (such as threat modeling, vulnerability discovery, or pentesting), insufficient documentation can force those consultants to invest unnecessary time in learning how the product is organized, instead of focusing their expertise on finding the flaws or suggesting effective mitigations. With respect to hardware design, the lack of a formal, final manufacturer reference can make it difficult or impossible to evaluate the final product, including post-manufacture verification. One cannot ensure that design functionality or operation is within acceptable tolerances, conforms to specifications, and is free from unexpected behavior. Hardware-related documentation may include engineering artifacts such as hardware description language (HDLs), netlists, Gerber files, Bills of Materials, EDA (Electronic Design Automation) tool files, etc.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Other**: Varies by Context, Hide Activities, Reduce Reliability, Quality Degradation, Reduce Maintainability

## Potential mitigations
- **Documentation, Architecture and Design**: Ensure that design documentation is detailed enough to allow for post-manufacturing verification.

## Related weaknesses
- CWE-710 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-3203**: A wireless access point manual specifies that the only method of configuration is via web interface (CWE-1059), but there is an undisclosed telnet server that was activated by default (CWE-912).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1059.html
