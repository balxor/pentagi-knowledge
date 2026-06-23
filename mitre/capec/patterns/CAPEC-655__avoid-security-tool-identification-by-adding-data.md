---
capec_id: CAPEC-655
name: Avoid Security Tool Identification by Adding Data
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: []
related_attack: [T1027.001]
url: https://capec.mitre.org/data/definitions/655.html
tags: [mitre-capec, attack-pattern, CAPEC-655]
---

# CAPEC-655 - Avoid Security Tool Identification by Adding Data

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-655](https://capec.mitre.org/data/definitions/655.html)

## Description
<xhtml:p>An adversary adds data to a file to increase the file size beyond what security tools are capable of handling in an attempt to mask their actions.</xhtml:p>
            <xhtml:p>In addition to this, adding data to a file also changes the file's hash, frustrating security tools that look for known bad files by their hash.</xhtml:p>

## Consequences
- **Accountability**: Hide Activities, Bypass Protection Mechanism
- **Integrity**: Modify Data

## Related ATT&CK techniques
- T1027.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/655.html
