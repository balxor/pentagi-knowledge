---
cwe_id: CWE-1240
name: Use of a Cryptographic Primitive with a Risky Implementation
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip]
related_capec: [CAPEC-97]
url: https://cwe.mitre.org/data/definitions/1240.html
tags: [mitre-cwe, weakness, CWE-1240]
---

# CWE-1240 - Use of a Cryptographic Primitive with a Risky Implementation

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1240](https://cwe.mitre.org/data/definitions/1240.html)

## Description
To fulfill the need for a cryptographic primitive, the product implements a cryptographic algorithm using a non-standard, unproven, or disallowed/non-compliant cryptographic implementation.

## Extended description
Cryptographic protocols and systems depend on cryptographic primitives (and associated algorithms) as their basic building blocks. Some common examples of primitives are digital signatures, one-way hash functions, ciphers, and public key cryptography; however, the notion of "primitive" can vary depending on point of view. See "Terminology Notes" for further explanation of some concepts. Cryptographic primitives are defined to accomplish one very specific task in a precisely defined and mathematically reliable fashion. For example, suppose that for a specific cryptographic primitive (such as an encryption routine), the consensus is that the primitive can only be broken after trying out N different inputs (where the larger the value of N, the stronger the cryptography). For an encryption scheme like AES-256, one would expect N to be so large as to be infeasible to execute in a reasonable amount of time. If a vulnerability is ever found that shows that one can break a cryptographic primitive in significantly less than the expected number of attempts, then that primitive is considered weakened (or sometimes in extreme cases, colloquially it is "broken"). As a result, anything using this cryptographic primitive would now be considered insecure or risky. Thus, even breaking or weakening a seemingly small cryptographic primitive has the potential to render the whole system vulnerable, due to its reliance on the primitive. A historical example can be found in TLS when using DES. One would colloquially call DES the cryptographic primitive for transport encryption in this version of TLS. In the past, DES was considered strong, because no weaknesses were found in it; importantly, DES has a key length of 56 bits. Trying N=2^56 keys was considered impractical for most actors. Unfortunately, attacking a system with 56-bit keys is now practical via brute force, which makes defeating DES encryption practical. It is now practical for an adversary to read any information sent under this version of TLS and use this information to attack the system. As a result, it can be claimed that this use of TLS is weak, and that any system depending on TLS with DES could potentially render the entire system vulnerable to attack. Cryptographic primitives and associated algorithms are only considered safe after extensive research and review from experienced cryptographers from academia, industry, and government entities looking for any possible flaws. Furthermore, cryptographic primitives and associated algorithms are frequently reevaluated for safety when new mathematical and attack techniques are discovered. As a result and over time, even well-known cryptographic primitives can lose their compliance status with the discovery of novel attacks that might either defeat the algorithm or reduce its robustness significantly. If ad-hoc cryptographic primitives are implemented, it is almost certain that the implementation will be vulnerable to attacks that are well understood by cryptographers, resulting in the exposure of sensitive information and other consequences. This weakness is even more difficult to manage for hardware-implemented deployment of cryptographic algorithms. First, because hardware is not patchable as easily as software, any flaw discovered after release and production typically cannot be fixed without a recall of the product. Secondly, the hardware product is often expected to work for years, during which time computation power available to the attacker only increases. Therefore, for hardware implementations of cryptographic primitives, it is absolutely essential that only strong, proven cryptographic primitives are used.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Requirements**: Require compliance with the strongest-available recommendations from trusted parties, and require that compliance must be kept up-to-date, since recommendations evolve over time. For example, US government systems require FIPS 140-3 certification, which supersedes FIPS 140-2 [REF-1192] [REF-267].
- **Architecture and Design**: Ensure that the architecture/design uses the strongest-available primitives and algorithms from trusted parties. For example, US government systems require FIPS 140-3 certification, which supersedes FIPS 140-2 [REF-1192] [REF-267].
- **Architecture and Design**: Do not develop custom or private cryptographic algorithms. They will likely be exposed to attacks that are well-understood by cryptographers. As with all cryptographic mechanisms, the source code should be available for analysis. If the algorithm may be compromised when attackers find out how it works, then it is especially weak.
- **Architecture and Design**: Try not to use cryptographic algorithms in novel ways or with new modes of operation even when you "know" it is secure. For example, using SHA-2 chaining to create a 1-time pad for encryption might sound like a good idea, but one should not do this.
- **Architecture and Design**: Ensure that the design can replace one cryptographic primitive or algorithm with another in the next generation ("cryptographic agility"). Where possible, use wrappers to make the interfaces uniform. This will make it easier to upgrade to stronger algorithms. This is especially important for hardware, which can be more difficult to upgrade quickly than software; design the hardware at a replaceable block level.
- **Architecture and Design**: Do not use outdated or non-compliant cryptography algorithms. Some older algorithms, once thought to require a billion years of computing time, can now be broken in days or hours. This includes MD4, MD5, SHA1, DES, and other algorithms that were once regarded as strong [REF-267].
- **Architecture and Design, Implementation**: Do not use a linear-feedback shift register (LFSR) or other legacy methods as a substitute for an accepted and standard Random Number Generator.
- **Architecture and Design, Implementation**: Do not use a checksum as a substitute for a cryptographically generated hash.
- **Architecture and Design**: Use a vetted cryptographic library or framework. Industry-standard implementations will save development time and are more likely to avoid errors that can occur during implementation of cryptographic algorithms. However, the library/framework could be used incorrectly during implementation.
- **Architecture and Design, Implementation**: When using industry-approved techniques, use them correctly. Don't cut corners by skipping resource-intensive steps (CWE-325). These steps are often essential for the prevention of common attacks.
- **Architecture and Design, Implementation**: Do not store keys in areas accessible to untrusted agents. Carefully manage and protect the cryptographic keys (see CWE-320). If the keys can be guessed or stolen, then the strength of the cryptography algorithm is irrelevant.

## Related attack patterns (CAPEC)
- [CAPEC-97](https://capec.mitre.org/data/definitions/97.html)

## Related weaknesses
- CWE-327 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-4778**: software uses MD5, which is less safe than the default SHA-256 used by related products
- **CVE-2005-2946**: Default configuration of product uses MD5 instead of stronger algorithms that are available, simplifying forgery of certificates.
- **CVE-2019-3907**: identity card uses MD5 hash of a salt and password
- **CVE-2021-34687**: personal key is transmitted over the network using a substitution cipher
- **CVE-2020-14254**: product does not disable TLS-RSA cipher suites, allowing decryption of traffic if TLS 2.0 and secure ciphers are not enabled.
- **CVE-2019-1543**: SSL/TLS library generates 16-byte nonces but reduces them to 12 byte nonces for the ChaCha20-Poly1305 cipher, converting them in a way that violates the cipher's requirements for unique nonces.
- **CVE-2017-9267**: LDAP interface allows use of weak ciphers
- **CVE-2017-7971**: SCADA product allows "use of outdated cipher suites"
- **CVE-2020-6616**: Chip implementing Bluetooth uses a low-entropy PRNG instead of a hardware RNG, allowing spoofing.
- **CVE-2019-1715**: security product has insufficient entropy in the DRBG, allowing collisions and private key discovery
- **CVE-2014-4192**: Dual_EC_DRBG implementation in RSA toolkit does not correctly handle certain byte requests, simplifying plaintext recovery
- **CVE-2007-6755**: Recommendation for Dual_EC_DRBG algorithm contains point Q constants that could simplify decryption

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1240.html
