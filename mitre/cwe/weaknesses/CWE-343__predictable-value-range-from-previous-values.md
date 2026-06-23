---
cwe_id: CWE-343
name: Predictable Value Range from Previous Values
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/343.html
tags: [mitre-cwe, weakness, CWE-343]
---

# CWE-343 - Predictable Value Range from Previous Values

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-343](https://cwe.mitre.org/data/definitions/343.html)

## Description
The product's random number generator produces a series of values which, when observed, can be used to infer a relatively small range of possibilities for the next value that could be generated.

## Extended description
The output of a random number generator should not be predictable based on observations of previous values. In some cases, an attacker cannot predict the exact value that will be produced next, but can narrow down the possibilities significantly. This reduces the amount of effort to perform a brute force attack. For example, suppose the product generates random numbers between 1 and 100, but it always produces a larger value until it reaches 100. If the generator produces an 80, then the attacker knows that the next value will be somewhere between 81 and 100. Instead of 100 possibilities, the attacker only needs to consider 20.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **general**: Increase the entropy used to seed a PRNG.
- **Architecture and Design, Requirements**: Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C ("Approved Random Number Generators").
- **Implementation**: Use a PRNG that periodically re-seeds itself using input from high-quality sources, such as hardware devices with high entropy. However, do not re-seed too frequently, or else the entropy source might block.

## Related weaknesses
- CWE-340 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/343.html
