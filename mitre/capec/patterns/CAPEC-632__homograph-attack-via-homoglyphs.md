---
capec_id: CAPEC-632
name: Homograph Attack via Homoglyphs
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Medium
related_cwe: [CWE-1007]
related_attack: []
url: https://capec.mitre.org/data/definitions/632.html
tags: [mitre-capec, attack-pattern, CAPEC-632]
---

# CAPEC-632 - Homograph Attack via Homoglyphs

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-632](https://capec.mitre.org/data/definitions/632.html)

## Description
An adversary registers a domain name containing a homoglyph, leading the registered domain to appear the same as a trusted domain. A homograph attack leverages the fact that different characters among various character sets look the same to the user. Homograph attacks must generally be combined with other attacks, such as phishing attacks, in order to direct Internet traffic to the adversary-controlled destinations.

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills required
- **Low**: Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- **Other**: Other (Depending on the intention of the adversary, a successful Homograph attack can be leveraged to execute more complex attacks such as cross-site scripting or stealing account credentials.)

## Execution flow
Execution Flow Explore Determine target website: The adversary first determines which website to impersonate, generally one that is trusted and receives a consistent amount of traffic. Techniques Research popular or high traffic websites. Experiment Impersonate trusted domain: In order to impersonate the trusted domain, the adversary needs to register the URL containing the homoglpyh character(s). Techniques Register the Homograph domain. Exploit Deceive user into visiting domain: Finally, the adversary needs to deceive a user into visiting the Homograph domain. Techniques Execute a phishing attack and send a user an e-mail convincing the to click on a link leading the user to the malicious domain.

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Utilize browsers that can warn users if URLs contain characters from different character sets.

## Related weaknesses (CWE)
- [CWE-1007](https://cwe.mitre.org/data/definitions/1007.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/632.html
