---
cwe_id: CWE-336
name: Same Seed in Pseudo-Random Number Generator (PRNG)
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/336.html
tags: [mitre-cwe, weakness, CWE-336]
---

# CWE-336 - Same Seed in Pseudo-Random Number Generator (PRNG)

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-336](https://cwe.mitre.org/data/definitions/336.html)

## Description
A Pseudo-Random Number Generator (PRNG) uses the same seed each time the product is initialized.

## Extended description
Given the deterministic nature of PRNGs, using the same seed for each initialization will lead to the same output in the same order. If an attacker can guess (or knows) the seed, then the attacker may be able to determine the random numbers that will be produced from the PRNG.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other, Access Control**: Other, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Do not reuse PRNG seeds. Consider a PRNG that periodically re-seeds itself as needed from a high quality pseudo-random output, such as hardware devices.
- **Architecture and Design, Requirements**: Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems, or use the more recent FIPS 140-3 [REF-1192] if possible.

## Related weaknesses
- CWE-335 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-39218**: SDK for JavaScript app builder for serverless code uses the same fixed seed for a PRNG, allowing cryptography bypass

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/336.html
