---
capec_id: CAPEC-97
name: Cryptanalysis
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Very High
related_cwe: [CWE-327, CWE-1204, CWE-1240, CWE-1241, CWE-1279]
related_attack: []
url: https://capec.mitre.org/data/definitions/97.html
tags: [mitre-capec, attack-pattern, CAPEC-97]
---

# CAPEC-97 - Cryptanalysis

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-97](https://capec.mitre.org/data/definitions/97.html)

## Description
Cryptanalysis is a process of finding weaknesses in cryptographic algorithms and using these weaknesses to decipher the ciphertext without knowing the secret key (instance deduction). Sometimes the weakness is not in the cryptographic algorithm itself, but rather in how it is applied that makes cryptanalysis successful. An attacker may have other goals as well, such as: Total Break (finding the secret key), Global Deduction (finding a functionally equivalent algorithm for encryption and decryption that does not require knowledge of the secret key), Information Deduction (gaining some information about plaintexts or ciphertexts that was not previously known) and Distinguishing Algorithm (the attacker has the ability to distinguish the output of the encryption (ciphertext) from a random permutation of bits).

## Prerequisites
- The target software utilizes some sort of cryptographic algorithm.
- An underlying weaknesses exists either in the cryptographic algorithm used or in the way that it was applied to a particular chunk of plaintext.
- The encryption algorithm is known to the attacker.
- An attacker has access to the ciphertext.

## Skills required
- **High**: Cryptanalysis generally requires a very significant level of understanding of mathematics and computation.

## Resources required
- Computing resource requirements will vary based on the complexity of a given cryptanalysis technique. Access to the encryption/decryption routines of the algorithm is also required.

## Consequences
- **Confidentiality**: Read Data (In most cases, if cryptanalysis is successful at all, an adversary will not be able to decrypt the entire message, but instead will only be able to deduce some information about the plaintext. However, that may be sufficient for an adversary, depending on the context of the attack.)

## Execution flow
Execution Flow Explore An attacker discovers a weakness in the cryptographic algorithm or a weakness in how it was applied to a particular chunk of plaintext. Exploit An attacker leverages the discovered weakness to decrypt, partially decrypt or infer some information about the contents of the encrypted message. All of that is done without knowing the secret key.

## Mitigations
- Use proven cryptographic algorithms with recommended key sizes.
- Ensure that the algorithms are used properly. That means: 1. Not rolling out your own crypto; Use proven algorithms and implementations. 2. Choosing initialization vectors with sufficiently random numbers 3. Generating key material using good sources of randomness and avoiding known weak keys 4. Using proven protocols and their implementations. 5. Picking the most appropriate cryptographic algorithm for your usage context and data

## Related weaknesses (CWE)
- [CWE-327](https://cwe.mitre.org/data/definitions/327.html)
- [CWE-1204](https://cwe.mitre.org/data/definitions/1204.html)
- [CWE-1240](https://cwe.mitre.org/data/definitions/1240.html)
- [CWE-1241](https://cwe.mitre.org/data/definitions/1241.html)
- [CWE-1279](https://cwe.mitre.org/data/definitions/1279.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/97.html
