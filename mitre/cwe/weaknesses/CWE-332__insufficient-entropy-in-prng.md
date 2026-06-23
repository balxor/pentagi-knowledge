---
cwe_id: CWE-332
name: Insufficient Entropy in PRNG
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/332.html
tags: [mitre-cwe, weakness, CWE-332]
---

# CWE-332 - Insufficient Entropy in PRNG

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-332](https://cwe.mitre.org/data/definitions/332.html)

## Description
The lack of entropy available for, or used by, a Pseudo-Random Number Generator (PRNG) can be a stability and security threat.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart
- **Access Control, Other**: Bypass Protection Mechanism, Other

## Potential mitigations
- **Architecture and Design, Requirements**: Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C ("Approved Random Number Generators").
- **Implementation**: Consider a PRNG that re-seeds itself as needed from high-quality pseudo-random output, such as hardware devices.
- **Architecture and Design**: When deciding which PRNG to use, look at its sources of entropy. Depending on what your security needs are, you may need to use a random number generator that always uses strong random data -- i.e., a random number generator that attempts to be strong but will fail in a weak way or will always provide some middle ground of protection through techniques like re-seeding. Generally, something that always provides a predictable amount of strength is preferable.

## Related weaknesses
- CWE-331 (ChildOf)

## Observed examples (CVE)
- **[REF-1374]**: Chain: JavaScript-based cryptocurrency library can fall back to the insecure Math.random() function instead of reporting a failure (CWE-392), thus reducing the entropy (CWE-332) and leading to generation of non-unique cryptographic keys for Bitcoin wallets (CWE-1391)
- **CVE-2019-1715**: security product has insufficient entropy in the DRBG, allowing collisions and private key discovery

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/332.html
