---
cwe_id: CWE-329
name: Generation of Predictable IV with CBC Mode
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/329.html
tags: [mitre-cwe, weakness, CWE-329]
---

# CWE-329 - Generation of Predictable IV with CBC Mode

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-329](https://cwe.mitre.org/data/definitions/329.html)

## Description
The product generates and uses a predictable initialization Vector (IV) with Cipher Block Chaining (CBC) Mode, which causes algorithms to be susceptible to dictionary attacks when they are encrypted under the same key.

## Extended description
CBC mode eliminates a weakness of Electronic Code Book (ECB) mode by allowing identical plaintext blocks to be encrypted to different ciphertext blocks. This is possible by the XOR-ing of an IV with the initial plaintext block so that every plaintext block in the chain is XOR'd with a different value before encryption. If IVs are reused, then identical plaintexts would be encrypted to identical ciphertexts. However, even if IVs are not identical but are predictable, then they still break the security of CBC mode against Chosen Plaintext Attacks (CPA).

## Applicable platforms / languages
Not Language-Specific, ICS/OT

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: NIST recommends two methods of generating unpredictable IVs for CBC mode [REF-1172]. The first is to generate the IV randomly. The second method is to encrypt a nonce with the same key and cipher to be used to encrypt the plaintext. In this case the nonce must be unique but can be predictable, since the block cipher will act as a pseudo random permutation.

## Related weaknesses
- CWE-1204 (ChildOf)
- CWE-573 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-5408**: encryption functionality in an authentication framework uses a fixed null IV with CBC mode, allowing attackers to decrypt traffic in applications that use this functionality
- **CVE-2017-17704**: messages for a door-unlocking product use a fixed IV in CBC mode, which is the same after each restart
- **CVE-2017-11133**: application uses AES in CBC mode, but the pseudo-random secret and IV are generated using math.random, which is not cryptographically strong.
- **CVE-2007-3528**: Blowfish-CBC implementation constructs an IV where each byte is calculated modulo 8 instead of modulo 256, resulting in less than 12 bits for the effective IV length, and less than 4096 possible IV values.
- **CVE-2011-3389**: BEAST attack in SSL 3.0 / TLS 1.0. In CBC mode, chained initialization vectors are non-random, allowing decryption of HTTPS traffic using a chosen plaintext attack.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/329.html
