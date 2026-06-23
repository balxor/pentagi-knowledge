---
capec_id: CAPEC-475
name: Signature Spoofing by Improper Validation
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-347, CWE-327, CWE-295]
related_attack: []
url: https://capec.mitre.org/data/definitions/475.html
tags: [mitre-capec, attack-pattern, CAPEC-475]
---

# CAPEC-475 - Signature Spoofing by Improper Validation

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-475](https://capec.mitre.org/data/definitions/475.html)

## Description
An adversary exploits a cryptographic weakness in the signature verification algorithm implementation to generate a valid signature without knowing the key.

## Extended description
Signature verification algorithms are generally used to determine whether a certificate or piece of code (e.g. executable, binary, etc.) possesses a valid signature and can be trusted. If the leveraged algorithm confirms that a valid signature exists, it establishes a foundation of trust that is further conveyed to the end-user when interacting with a website or application. However, if the signature verification algorithm improperly validates the signature, either by not validating the signature at all or by failing to fully validate the signature, it could result in an adversary generating a spoofed signature and being classified as a legitimate entity. Successfully exploiting such a weakness could further allow the adversary to reroute users to malicious sites, steals files, activates microphones, records keystrokes and passwords, wipes disks, installs malware, and more.

## Prerequisites
- Recipient is using a weak cryptographic signature verification algorithm or a weak implementation of a cryptographic signature verification algorithm, or the configuration of the recipient's application accepts the use of keys generated using cryptographically weak signature verification algorithms.

## Skills required
- **High**: Reverse engineering and cryptanalysis of signature verification algorithm implementation

## Mitigations
- Use programs and products that contain cryptographic elements that have been thoroughly tested for flaws in the signature verification routines.

## Related weaknesses (CWE)
- [CWE-347](https://cwe.mitre.org/data/definitions/347.html)
- [CWE-327](https://cwe.mitre.org/data/definitions/327.html)
- [CWE-295](https://cwe.mitre.org/data/definitions/295.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/475.html
