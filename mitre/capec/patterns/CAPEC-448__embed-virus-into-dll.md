---
capec_id: CAPEC-448
name: Embed Virus into DLL
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-506]
related_attack: [T1027.009]
url: https://capec.mitre.org/data/definitions/448.html
tags: [mitre-capec, attack-pattern, CAPEC-448]
---

# CAPEC-448 - Embed Virus into DLL

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-448](https://capec.mitre.org/data/definitions/448.html)

## Description
An adversary tampers with a DLL and embeds a computer virus into gaps between legitimate machine instructions. These gaps may be the result of compiler optimizations that pad memory blocks for performance gains. The embedded virus then attempts to infect any machine which interfaces with the product, and possibly steal private data or eavesdrop.

## Prerequisites
- Access to the software currently deployed at a victim location. This access is often obtained by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- **Authorization**: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect and quarantine software with known virus.

## Related weaknesses (CWE)
- [CWE-506](https://cwe.mitre.org/data/definitions/506.html)

## Related ATT&CK techniques
- T1027.009

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/448.html
