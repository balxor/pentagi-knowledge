---
capec_id: CAPEC-459
name: Creating a Rogue Certification Authority Certificate
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Very High
related_cwe: [CWE-327, CWE-295, CWE-290]
related_attack: []
url: https://capec.mitre.org/data/definitions/459.html
tags: [mitre-capec, attack-pattern, CAPEC-459]
---

# CAPEC-459 - Creating a Rogue Certification Authority Certificate

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-459](https://capec.mitre.org/data/definitions/459.html)

## Description
An adversary exploits a weakness resulting from using a hashing algorithm with weak collision resistance to generate certificate signing requests (CSR) that contain collision blocks in their "to be signed" parts. The adversary submits one CSR to be signed by a trusted certificate authority then uses the signed blob to make a second certificate appear signed by said certificate authority. Due to the hash collision, both certificates, though different, hash to the same value and so the signed blob works just as well in the second certificate. The net effect is that the adversary's second X.509 certificate, which the Certification Authority has never seen, is now signed and validated by that Certification Authority.

## Extended description
Alternatively, the second certificate could be a signing certificate. Thus the adversary is able to start their own Certification Authority that is anchored in its root of trust in the legitimate Certification Authority that has signed the attacker's first X.509 certificate. If the original Certificate Authority was accepted by default by browsers, so will the Certificate Authority set up by the adversary and any certificates that it signs. As a result, the adversary is able to generate any SSL certificates to impersonate any web server, and the user's browser will not issue any warning to the victim. This can be used to compromise HTTPS communications and other types of systems where PKI and X.509 certificates may be used (e.g., VPN, IPSec).

## Prerequisites
- Certification Authority is using a hash function with insufficient collision resistance to generate the certificate hash to be signed

## Skills required
- **High**: An attacker must be able to craft two X.509 certificates that produce the same hash value
- **Medium**: Knowledge needed to set up a certification authority

## Resources required
- Knowledge of a certificate authority that uses hashing algorithms with poor collision resistance
- A valid certificate request and a malicious certificate request with identical hash values

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges

## Execution flow
Execution Flow Experiment Craft Certificates: The adversary crafts two different, but valid X.509 certificates that when hashed with an insufficiently collision resistant hashing algorithm would yield the same value. Send CSR to Certificate Authority: The adversary sends the CSR for one of the certificates to the Certification Authority which uses the targeted hashing algorithm. That request is completely valid and the Certificate Authority issues an X.509 certificate to the adversary which is signed with its private key. Exploit Insert Signed Blob into Unsigned Certificate: The adversary takes the signed blob and inserts it into the second X.509 certificate that the attacker generated. Due to the hash collision, both certificates, though different, hash to the same value and so the signed blob is valid in the second certificate. The result is two certificates that appear to be signed by a valid certificate authority despite only one having been signed.

## Mitigations
- Certification Authorities need to stop using deprecated or cryptographically insecure hashing algorithms to hash the certificates that they are about to sign. Instead they should be using stronger hashing functions such as SHA-256 or SHA-512.

## Related weaknesses (CWE)
- [CWE-327](https://cwe.mitre.org/data/definitions/327.html)
- [CWE-295](https://cwe.mitre.org/data/definitions/295.html)
- [CWE-290](https://cwe.mitre.org/data/definitions/290.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/459.html
