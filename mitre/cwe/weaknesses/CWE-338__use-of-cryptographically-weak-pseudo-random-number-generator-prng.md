---
cwe_id: CWE-338
name: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/338.html
tags: [mitre-cwe, weakness, CWE-338]
---

# CWE-338 - Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-338](https://cwe.mitre.org/data/definitions/338.html)

## Description
The product uses a Pseudo-Random Number Generator (PRNG) in a security context, but the PRNG's algorithm is not cryptographically strong.

## Extended description
When a non-cryptographic PRNG is used in a cryptographic context, it can expose the cryptography to certain types of attacks. Often a pseudo-random number generator (PRNG) is not designed for cryptography. Sometimes a mediocre source of randomness is sufficient or preferable for algorithms that use random numbers. Weak generators generally take less processing power and/or do not use the precious, finite, entropy sources on a system. While such PRNGs might have very useful features, these same features could be used to break the cryptography.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Use functions or hardware which use a hardware-based random number generation for all crypto. This is the recommended solution. Use CyptGenRandom on Windows, or hw_rand() on Linux.

## Related weaknesses
- CWE-330 (ChildOf)
- CWE-330 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-3692**: PHP framework uses mt_rand() function (Marsenne Twister) when generating tokens
- **CVE-2009-3278**: Crypto product uses rand() library function to generate a recovery key, making it easier to conduct brute force attacks.
- **CVE-2009-3238**: Random number generator can repeatedly generate the same value.
- **CVE-2009-2367**: Web application generates predictable session IDs, allowing session hijacking.
- **CVE-2008-0166**: SSL library uses a weak random number generator that only generates 65,536 unique keys.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/338.html
