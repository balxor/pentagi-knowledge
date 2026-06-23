---
capec_id: CAPEC-144
name: Detect Unpublicized Web Services
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-425]
related_attack: []
url: https://capec.mitre.org/data/definitions/144.html
tags: [mitre-capec, attack-pattern, CAPEC-144]
---

# CAPEC-144 - Detect Unpublicized Web Services

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-144](https://capec.mitre.org/data/definitions/144.html)

## Description
An adversary searches a targeted web site for web services that have not been publicized. This attack can be especially dangerous since unpublished but available services may not have adequate security controls placed upon them given that an administrator may believe they are unreachable.

## Prerequisites
- The targeted web site must include unpublished services within its web tree. The nature of these services determines the severity of this attack.

## Resources required
- Spidering tools to explore the target web site are extremely useful in this attack especially when attacking large sites. Some tools might also be able to automatically construct common service queries from known paths.

## Execution flow
Execution Flow Explore Find target web site: An adversary finds a target web site that they think may have unpublicized web services Map the published web site: The adversary will map the published web site either by using an automated tool or by manually accessing well-known debugging or logging pages, or otherwise predictable pages within the site tree Techniques Use Dirbuster to brute force directories and file names to find unpublicized web services Find a pattern in the naming of documents and extrapolate this pattern to discover additional documents that have been created but are no longer externally linked Experiment Try to find weaknesses or information: The adversary will try to find weaknesses in the unpublicized services that the targeted site did not intend to be public Techniques Use Nikto to look for web service vulnerabilities Exploit Follow-up attack: Use any information or weaknesses found to carry out a follow-up attack

## Related weaknesses (CWE)
- [CWE-425](https://cwe.mitre.org/data/definitions/425.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/144.html
