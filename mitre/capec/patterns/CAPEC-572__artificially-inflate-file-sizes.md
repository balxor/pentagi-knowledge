---
capec_id: CAPEC-572
name: Artificially Inflate File Sizes
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Medium
related_cwe: []
related_attack: [T1027.001]
url: https://capec.mitre.org/data/definitions/572.html
tags: [mitre-capec, attack-pattern, CAPEC-572]
---

# CAPEC-572 - Artificially Inflate File Sizes

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-572](https://capec.mitre.org/data/definitions/572.html)

## Description
<xhtml:p>An adversary modifies file contents by adding data to files for several reasons. Many different attacks could “follow” this pattern resulting in numerous outcomes. Adding data to a file could also result in a Denial of Service condition for devices with limited storage capacity.</xhtml:p>

## Consequences
- **Availability**: Resource Consumption (Denial of Service)
- **Integrity**: Modify Data

## Related ATT&CK techniques
- T1027.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/572.html
