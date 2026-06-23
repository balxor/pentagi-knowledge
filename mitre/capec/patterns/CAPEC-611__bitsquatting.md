---
capec_id: CAPEC-611
name: BitSquatting
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Medium
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/611.html
tags: [mitre-capec, attack-pattern, CAPEC-611]
---

# CAPEC-611 - BitSquatting

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-611](https://capec.mitre.org/data/definitions/611.html)

## Description
An adversary registers a domain name one bit different than a trusted domain. A BitSquatting attack leverages random errors in memory to direct Internet traffic to adversary-controlled destinations. BitSquatting requires no exploitation or complicated reverse engineering, and is operating system and architecture agnostic. Experimental observations show that BitSquatting popular websites could redirect non-trivial amounts of Internet traffic to a malicious entity.

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills required
- **Low**: Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- **Other**: Other (Depending on the intention of the adversary, a successful BitSquatting attack can be leveraged to execute more complex attacks such as cross-site scripting or stealing account credentials.)

## Execution flow
Execution Flow Explore Determine target website: The adversary first determines which website to impersonate, generally one that is trusted and receives a consistent amount of traffic. Techniques Research popular or high traffic websites. Experiment Impersonate trusted domain: In order to impersonate the trusted domain, the adversary needs to register the BitSquatted URL. Techniques Register the BitSquatted domain. Exploit Wait for a user to visit the domain: Finally, the adversary simply waits for a user to be unintentionally directed to the BitSquatted domain. Techniques Simply wait for an error in memory to occur, redirecting the user to the malicious domain.

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- When possible, use error-correcting (ECC) memory in local devices as non-ECC memory is significantly more vulnerable to faults.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/611.html
