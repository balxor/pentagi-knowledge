---
capec_id: CAPEC-463
name: Padding Oracle Crypto Attack
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: [CWE-209, CWE-514, CWE-649, CWE-347, CWE-354, CWE-696]
related_attack: []
url: https://capec.mitre.org/data/definitions/463.html
tags: [mitre-capec, attack-pattern, CAPEC-463]
---

# CAPEC-463 - Padding Oracle Crypto Attack

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-463](https://capec.mitre.org/data/definitions/463.html)

## Description
An adversary is able to efficiently decrypt data without knowing the decryption key if a target system leaks data on whether or not a padding error happened while decrypting the ciphertext. A target system that leaks this type of information becomes the padding oracle and an adversary is able to make use of that oracle to efficiently decrypt data without knowing the decryption key by issuing on average 128*b calls to the padding oracle (where b is the number of bytes in the ciphertext block). In addition to performing decryption, an adversary is also able to produce valid ciphertexts (i.e., perform encryption) by using the padding oracle, all without knowing the encryption key.

## Extended description
Any cryptosystem can be vulnerable to padding oracle attacks if the encrypted messages are not authenticated to ensure their validity prior to decryption, and then the information about padding error is leaked to the adversary. This attack technique may be used, for instance, to break CAPTCHA systems or decrypt/modify state information stored in client side objects (e.g., hidden fields or cookies). This attack technique is a side-channel attack on the cryptosystem that uses a data leak from an improperly implemented decryption routine to completely subvert the cryptosystem. The one bit of information that tells the adversary whether a padding error during decryption has occurred, in whatever form it comes, is sufficient for the adversary to break the cryptosystem. That bit of information can come in a form of an explicit error message about a padding error, a returned blank page, or even the server taking longer to respond (a timing attack). This attack can be launched cross domain where an adversary is able to use cross-domain information leaks to get the bits of information from the padding oracle from a target system / service with which the victim is communicating.

## Prerequisites
- The decryption routine does not properly authenticate the message / does not verify its integrity prior to performing the decryption operation
- The target system leaks data (in some way) on whether a padding error has occurred when attempting to decrypt the ciphertext.
- The padding oracle remains available for enough time / for as many requests as needed for the adversary to decrypt the ciphertext.

## Resources required
- Ability to detect instances where a target system is vulnerable to an oracle padding attack Sufficient cryptography knowledge and tools needed to take advantage of the presence of the padding oracle to perform decryption / encryption of data without a key

## Mitigations
- Design: Use a message authentication code (MAC) or another mechanism to perform verification of message authenticity / integrity prior to decryption
- Implementation: Do not leak information back to the user as to any cryptography (e.g., padding) encountered during decryption.

## Related weaknesses (CWE)
- [CWE-209](https://cwe.mitre.org/data/definitions/209.html)
- [CWE-514](https://cwe.mitre.org/data/definitions/514.html)
- [CWE-649](https://cwe.mitre.org/data/definitions/649.html)
- [CWE-347](https://cwe.mitre.org/data/definitions/347.html)
- [CWE-354](https://cwe.mitre.org/data/definitions/354.html)
- [CWE-696](https://cwe.mitre.org/data/definitions/696.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/463.html
