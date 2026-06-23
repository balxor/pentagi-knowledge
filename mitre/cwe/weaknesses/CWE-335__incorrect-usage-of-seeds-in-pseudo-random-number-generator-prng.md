---
cwe_id: CWE-335
name: Incorrect Usage of Seeds in Pseudo-Random Number Generator (PRNG)
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/335.html
tags: [mitre-cwe, weakness, CWE-335]
---

# CWE-335 - Incorrect Usage of Seeds in Pseudo-Random Number Generator (PRNG)

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-335](https://cwe.mitre.org/data/definitions/335.html)

## Description
The product uses a Pseudo-Random Number Generator (PRNG) but does not correctly manage seeds.

## Extended description
PRNGs are deterministic and, while their output appears random, they cannot actually create entropy. They rely on cryptographically secure and unique seeds for entropy so proper seeding is critical to the secure operation of the PRNG. Management of seeds could be broken down into two main areas: (1) protecting seeds as cryptographic material (such as a cryptographic key); (2) whenever possible, using a uniquely generated seed from a cryptographically secure source PRNGs require a seed as input to generate a stream of numbers that are functionally indistinguishable from random numbers. While the output is, in many cases, sufficient for cryptographic uses, the output of any PRNG is directly determined by the seed provided as input. If the seed can be ascertained by a third party, the entire output of the PRNG can be made known to them. As such, the seed should be kept secret and should ideally not be able to be guessed. For example, the current time may be a poor seed. Knowing the approximate time the PRNG was seeded greatly reduces the possible key space. Seeds do not necessarily need to be unique, but reusing seeds may open up attacks if the seed is discovered.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Other**: Bypass Protection Mechanism, Other

## Related weaknesses
- CWE-330 (ChildOf)
- CWE-330 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-7010**: Cloud application on Kubernetes generates passwords using a weak random number generator based on deployment time.
- **CVE-2019-11495**: server uses erlang:now() to seed the PRNG, which results in a small search space for potential random seeds
- **CVE-2018-12520**: Product's PRNG is not seeded for the generation of session IDs
- **CVE-2016-10180**: Router's PIN generation is based on rand(time(0)) seeding.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/335.html
