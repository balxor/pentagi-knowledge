---
cwe_id: CWE-300
name: Channel Accessible by Non-Endpoint
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-466, CAPEC-57, CAPEC-589, CAPEC-590, CAPEC-612, CAPEC-613, CAPEC-615, CAPEC-662, CAPEC-94]
url: https://cwe.mitre.org/data/definitions/300.html
tags: [mitre-cwe, weakness, CWE-300]
---

# CWE-300 - Channel Accessible by Non-Endpoint

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-300](https://cwe.mitre.org/data/definitions/300.html)

## Description
The product does not adequately verify the identity of actors at both ends of a communication channel, or does not adequately ensure the integrity of the channel, in a way that allows the channel to be accessed or influenced by an actor that is not an endpoint.

## Extended description
In order to establish secure communication between two parties, it is often important to adequately verify the identity of entities at each end of the communication channel. Inadequate or inconsistent verification may result in insufficient or incorrect identification of either communicating entity. This can have negative consequences such as misplaced trust in the entity at the other end of the channel. An attacker can leverage this by interposing between the communicating entities and masquerading as the original entity. In the absence of sufficient verification of identity, such an attacker can eavesdrop and potentially modify the communication between the original entities.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control**: Read Application Data, Modify Application Data, Gain Privileges or Assume Identity

## Potential mitigations
- **Implementation**: Always fully authenticate both ends of any communications channel.
- **Architecture and Design**: Adhere to the principle of complete mediation.
- **Implementation**: A certificate binds an identity to a cryptographic key to authenticate a communicating party. Often, the certificate takes the encrypted form of the hash of the identity of the subject, the public key, and information such as time of issue or expiration using the issuer's private key. The certificate can be validated by deciphering the certificate with the issuer's public key. See also X.509 certificate signature chains and the PGP certification structure.

## Related attack patterns (CAPEC)
- [CAPEC-466](https://capec.mitre.org/data/definitions/466.html)
- [CAPEC-57](https://capec.mitre.org/data/definitions/57.html)
- [CAPEC-589](https://capec.mitre.org/data/definitions/589.html)
- [CAPEC-590](https://capec.mitre.org/data/definitions/590.html)
- [CAPEC-612](https://capec.mitre.org/data/definitions/612.html)
- [CAPEC-613](https://capec.mitre.org/data/definitions/613.html)
- [CAPEC-615](https://capec.mitre.org/data/definitions/615.html)
- [CAPEC-662](https://capec.mitre.org/data/definitions/662.html)
- [CAPEC-94](https://capec.mitre.org/data/definitions/94.html)

## Related weaknesses
- CWE-923 (ChildOf)

## Observed examples (CVE)
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/300.html
