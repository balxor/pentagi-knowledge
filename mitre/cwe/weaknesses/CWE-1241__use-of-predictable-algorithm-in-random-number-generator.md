---
cwe_id: CWE-1241
name: Use of Predictable Algorithm in Random Number Generator
type: weakness
abstraction: Base
status: Draft
languages: [System on Chip]
related_capec: [CAPEC-97]
url: https://cwe.mitre.org/data/definitions/1241.html
tags: [mitre-cwe, weakness, CWE-1241]
---

# CWE-1241 - Use of Predictable Algorithm in Random Number Generator

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1241](https://cwe.mitre.org/data/definitions/1241.html)

## Description
The device uses an algorithm that is predictable and generates a pseudo-random number.

## Extended description
Pseudo-random number generator algorithms are predictable because their registers have a finite number of possible states, which eventually lead to repeating patterns. As a result, pseudo-random number generators (PRNGs) can compromise their randomness or expose their internal state to various attacks, such as reverse engineering or tampering.

## Applicable platforms / languages
System on Chip

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: It is highly recommended to use a true random number generator (TRNG) to ensure the security of encryption schemes. Hardware-based TRNGs generate unpredictable, unbiased, and independent random numbers because they employ physical phenomena, e.g., electrical noise, as sources to generate random numbers.
- **Implementation**: It is highly recommended to use a true random number generator (TRNG) to ensure the security of encryption schemes. Hardware-based TRNGs generate unpredictable, unbiased, and independent random numbers because they employ physical phenomena, e.g., electrical noise, as sources to generate random numbers.

## Related attack patterns (CAPEC)
- [CAPEC-97](https://capec.mitre.org/data/definitions/97.html)

## Related weaknesses
- CWE-330 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-3692**: PHP framework uses mt_rand() function (Marsenne Twister) when generating tokens

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1241.html
