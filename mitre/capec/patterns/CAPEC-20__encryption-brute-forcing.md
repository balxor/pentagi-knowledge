---
capec_id: CAPEC-20
name: Encryption Brute Forcing
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Low
related_cwe: [CWE-326, CWE-327, CWE-693, CWE-1204]
related_attack: []
url: https://capec.mitre.org/data/definitions/20.html
tags: [mitre-capec, attack-pattern, CAPEC-20]
---

# CAPEC-20 - Encryption Brute Forcing

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-20](https://capec.mitre.org/data/definitions/20.html)

## Description
An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.

## Prerequisites
- Ciphertext is known.
- Encryption algorithm and key size are known.

## Skills required
- **Low**: Brute forcing encryption does not require much skill.

## Resources required
- A powerful enough computer for the job with sufficient CPU, RAM and HD. Exact requirements will depend on the size of the brute force job and the time requirement for completion. Some brute forcing jobs may require grid or distributed computing (e.g. DES Challenge). On average, for a binary key of size N, 2^(N/2) trials will be needed to find the key that would decrypt the ciphertext to obtain the original plaintext. Obviously as N gets large the brute force approach becomes infeasible.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Determine the ciphertext and the encryption algorithm. Experiment Perform an exhaustive brute force search of the key space, producing candidate plaintexts and observing if they make sense.

## Mitigations
- Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.
- In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.

## Related weaknesses (CWE)
- [CWE-326](https://cwe.mitre.org/data/definitions/326.html)
- [CWE-327](https://cwe.mitre.org/data/definitions/327.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)
- [CWE-1204](https://cwe.mitre.org/data/definitions/1204.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/20.html
