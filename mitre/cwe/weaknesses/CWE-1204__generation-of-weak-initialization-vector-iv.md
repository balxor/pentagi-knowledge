---
cwe_id: CWE-1204
name: Generation of Weak Initialization Vector (IV)
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-20, CAPEC-97]
url: https://cwe.mitre.org/data/definitions/1204.html
tags: [mitre-cwe, weakness, CWE-1204]
---

# CWE-1204 - Generation of Weak Initialization Vector (IV)

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1204](https://cwe.mitre.org/data/definitions/1204.html)

## Description
The product uses a cryptographic primitive that uses an Initialization Vector (IV), but the product does not generate IVs that are sufficiently unpredictable or unique according to the expected cryptographic requirements for that primitive.

## Extended description
By design, some cryptographic primitives (such as block ciphers) require that IVs must have certain properties for the uniqueness and/or unpredictability of an IV. Primitives may vary in how important these properties are. If these properties are not maintained, e.g. by a bug in the code, then the cryptography may be weakened or broken by attacking the IVs themselves.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Different cipher modes have different requirements for their IVs. When choosing and implementing a mode, it is important to understand those requirements in order to keep security guarantees intact. Generally, it is safest to generate a random IV, since it will be both unpredictable and have a very low chance of being non-unique. IVs do not have to be kept secret, so if generating duplicate IVs is a concern, a list of already-used IVs can be kept and checked against. NIST offers recommendations on generation of IVs for modes of which they have approved. These include options for when random IVs are not practical. For CBC, CFB, and OFB, see [REF-1175]; for GCM, see [REF-1178].

## Related attack patterns (CAPEC)
- [CAPEC-20](https://capec.mitre.org/data/definitions/20.html)
- [CAPEC-97](https://capec.mitre.org/data/definitions/97.html)

## Related weaknesses
- CWE-330 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-1472**: ZeroLogon vulnerability - use of a static IV of all zeroes in AES-CFB8 mode
- **CVE-2011-3389**: BEAST attack in SSL 3.0 / TLS 1.0. In CBC mode, chained initialization vectors are non-random, allowing decryption of HTTPS traffic using a chosen plaintext attack.
- **CVE-2001-0161**: wireless router does not use 6 of the 24 bits for WEP encryption, making it easier for attackers to decrypt traffic
- **CVE-2001-0160**: WEP card generates predictable IV values, making it easier for attackers to decrypt traffic
- **CVE-2017-3225**: device bootloader uses a zero initialization vector during AES-CBC
- **CVE-2016-6485**: crypto framework uses PHP rand function - which is not cryptographically secure - for an initialization vector
- **CVE-2014-5386**: encryption routine does not seed the random number generator, causing the same initialization vector to be generated repeatedly
- **CVE-2020-5408**: encryption functionality in an authentication framework uses a fixed null IV with CBC mode, allowing attackers to decrypt traffic in applications that use this functionality
- **CVE-2017-17704**: messages for a door-unlocking product use a fixed IV in CBC mode, which is the same after each restart
- **CVE-2017-11133**: application uses AES in CBC mode, but the pseudo-random secret and IV are generated using math.random, which is not cryptographically strong.
- **CVE-2007-3528**: Blowfish-CBC implementation constructs an IV where each byte is calculated modulo 8 instead of modulo 256, resulting in less than 12 bits for the effective IV length, and less than 4096 possible IV values.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1204.html
