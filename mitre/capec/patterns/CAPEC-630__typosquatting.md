---
capec_id: CAPEC-630
name: TypoSquatting
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Medium
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/630.html
tags: [mitre-capec, attack-pattern, CAPEC-630]
---

# CAPEC-630 - TypoSquatting

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-630](https://capec.mitre.org/data/definitions/630.html)

## Description
An adversary registers a domain name with at least one character different than a trusted domain. A TypoSquatting attack takes advantage of instances where a user mistypes a URL (e.g. www.goggle.com) or not does visually verify a URL before clicking on it (e.g. phishing attack). As a result, the user is directed to an adversary-controlled destination. TypoSquatting does not require an attack against the trusted domain or complicated reverse engineering.

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills required
- **Low**: Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- **Other**: Other (Depending on the intention of the adversary, a successful TypoSquatting attack can be leveraged to execute more complex attacks such as cross-site scripting or stealing account credentials.)

## Execution flow
Execution Flow Explore Determine target website: The adversary first determines which website to impersonate, generally one that is trusted and receives a consistent amount of traffic. Techniques Research popular or high traffic websites. Experiment Impersonate trusted domain: In order to impersonate the trusted domain, the adversary needs to register the TypoSquatted URL. Techniques Register the TypoSquatted domain. Exploit Deceive user into visiting domain: Finally, the adversary needs to deceive a user into visiting the TypoSquatted domain. Techniques Execute a phishing attack and send a user an e-mail convincing the user to click on a link leading the user to the TypoSquatted domain. Assume that a user will incorrectly type the legitimate URL, leading the user to the TypoSquatted domain.

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Purchase potential TypoSquatted domains and forward to legitimate domain.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/630.html
