---
capec_id: CAPEC-143
name: Detect Unpublicized Web Pages
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-425]
related_attack: []
url: https://capec.mitre.org/data/definitions/143.html
tags: [mitre-capec, attack-pattern, CAPEC-143]
---

# CAPEC-143 - Detect Unpublicized Web Pages

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-143](https://capec.mitre.org/data/definitions/143.html)

## Description
An adversary searches a targeted web site for web pages that have not been publicized. In doing this, the adversary may be able to gain access to information that the targeted site did not intend to make public.

## Prerequisites
- The targeted web site must include pages within its published tree that are not connected to its tree of links. The sensitivity of the content of these pages determines the severity of this attack.

## Resources required
- Spidering tools to explore the target web site are extremely useful in this attack especially when attacking large sites. Some tools might also be able to automatically construct common page locations from known paths.

## Execution flow
Execution Flow Explore Find target web site: An adversary finds a target web site that they think may have unpublicized web pages Map the published web site: The adversary will map the published web site either by using an automated tool or by manually accessing well-known debugging or logging pages, or otherwise predictable pages within the site tree Techniques Use Dirbuster to brute force directories and file names to find unpublicized pages Find a pattern in the naming of documents and extrapolate this pattern to discover additional documents that have been created but are no longer externally linked Experiment Try to find weaknesses or information: The adversary will try to find weaknesses or information on the unpublicized pages that the targeted site did not intend to be public Techniques Manually analyze files or pages for information that could be useful in a further attack Use a static analysis tool to find weaknesses in unpublished web pages Exploit Follow-up attack: Use any information or weaknesses found to carry out a follow-up attack

## Related weaknesses (CWE)
- [CWE-425](https://cwe.mitre.org/data/definitions/425.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/143.html
