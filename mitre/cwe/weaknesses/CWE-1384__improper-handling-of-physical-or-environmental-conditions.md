---
cwe_id: CWE-1384
name: Improper Handling of Physical or Environmental Conditions
type: weakness
abstraction: Class
status: Incomplete
languages: [System on Chip, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1384.html
tags: [mitre-cwe, weakness, CWE-1384]
---

# CWE-1384 - Improper Handling of Physical or Environmental Conditions

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1384](https://cwe.mitre.org/data/definitions/1384.html)

## Description
The product does not properly handle unexpected physical or environmental conditions that occur naturally or are artificially induced.

## Extended description
Hardware products are typically only guaranteed to behave correctly within certain physical limits or environmental conditions. Such products cannot necessarily control the physical or external conditions to which they are subjected. However, the inability to handle such conditions can undermine a product's security. For example, an unexpected physical or environmental condition may cause the flipping of a bit that is used for an authentication decision. This unexpected condition could occur naturally or be induced artificially by an adversary. Physical or environmental conditions of concern are: Atmospheric characteristics: extreme temperature ranges, etc. Interference: electromagnetic interference (EMI), radio frequency interference (RFI), etc. Assorted light sources: white light, ultra-violet light (UV), lasers, infrared (IR), etc. Power variances: under-voltages, over-voltages, under-current, over-current, etc. Clock variances: glitching, overclocking, clock stretching, etc. Component aging and degradation Materials manipulation: focused ion beams (FIB), etc. Exposure to radiation: x-rays, cosmic radiation, etc.

## Applicable platforms / languages
System on Chip, ICS/OT

## Common consequences
- **Confidentiality, Integrity, Availability**: Varies by Context, Unexpected State

## Potential mitigations
- **Requirements**: In requirements, be specific about expectations for how the product will perform when it exceeds physical and environmental boundary conditions, e.g., by shutting down.
- **Architecture and Design, Implementation**: Where possible, include independent components that can detect excess environmental conditions and have the capability to shut down the product.
- **Architecture and Design, Implementation**: Where possible, use shielding or other materials that can increase the adversary's workload and reduce the likelihood of being able to successfully trigger a security-related failure.

## Related weaknesses
- CWE-703 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-17391**: Lack of anti-glitch protections allows an attacker to launch a physical attack to bypass the secure boot and read protected eFuses.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1384.html
