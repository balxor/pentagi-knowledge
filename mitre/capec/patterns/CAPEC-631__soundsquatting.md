---
capec_id: CAPEC-631
name: SoundSquatting
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Medium
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/631.html
tags: [mitre-capec, attack-pattern, CAPEC-631]
---

# CAPEC-631 - SoundSquatting

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-631](https://capec.mitre.org/data/definitions/631.html)

## Description
An adversary registers a domain name that sounds the same as a trusted domain, but has a different spelling. A SoundSquatting attack takes advantage of a user's confusion of the two words to direct Internet traffic to adversary-controlled destinations. SoundSquatting does not require an attack against the trusted domain or complicated reverse engineering.

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills required
- **Low**: Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- **Other**: Other (Depending on the intention of the adversary, a successful SoundSquatting attack can be leveraged to execute more complex attacks such as cross-site scripting or stealing account credentials.)

## Execution flow
Execution Flow Explore Determine target website: The adversary first determines which website to impersonate, generally one that is trusted, receives a consistent amount of traffic, and is a homophone. Techniques Research popular or high traffic websites which are also homophones. Experiment Impersonate trusted domain: In order to impersonate the trusted domain, the adversary needs to register the SoundSquatted URL. Techniques Register the SoundSquatted domain. Exploit Deceive user into visiting domain: Finally, the adversary needs to deceive a user into visiting the SoundSquatted domain. Techniques Execute a phishing attack and send a user an e-mail convincing the user to click on a link leading the user to the SoundSquatted domain. Assume that a user will unintentionally use the homophone in the URL, leading the user to the SoundSquatted domain.

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Purchase potential SoundSquatted domains and forward to legitimate domain.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/631.html
