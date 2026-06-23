---
cwe_id: CWE-301
name: Reflection Attack in an Authentication Protocol
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-90]
url: https://cwe.mitre.org/data/definitions/301.html
tags: [mitre-cwe, weakness, CWE-301]
---

# CWE-301 - Reflection Attack in an Authentication Protocol

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-301](https://cwe.mitre.org/data/definitions/301.html)

## Description
Simple authentication protocols are subject to reflection attacks if a malicious user can use the target machine to impersonate a trusted user.

## Extended description
A mutual authentication protocol requires each party to respond to a random challenge by the other party by encrypting it with a pre-shared key. Often, however, such protocols employ the same pre-shared key for communication with a number of different entities. A malicious user or an attacker can easily compromise this protocol without possessing the correct key by employing a reflection attack on the protocol. Reflection attacks capitalize on mutual authentication schemes in order to trick the target into revealing the secret shared between it and another valid user. In a basic mutual-authentication scheme, a secret is known to both the valid user and the server; this allows them to authenticate. In order that they may verify this shared secret without sending it plainly over the wire, they utilize a Diffie-Hellman-style scheme in which they each pick a value, then request the hash of that value as keyed by the shared secret. In a reflection attack, the attacker claims to be a valid user and requests the hash of a random value from the server. When the server returns this value and requests its own value to be hashed, the attacker opens another connection to the server. This time, the hash requested by the attacker is the value which the server requested in the first connection. When the server returns this hashed value, it is used in the first connection, authenticating the attacker successfully as the impersonated valid user.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Use different keys for the initiator and responder or of a different type of challenge for the initiator and responder.
- **Architecture and Design**: Let the initiator prove its identity before proceeding.

## Related attack patterns (CAPEC)
- [CAPEC-90](https://capec.mitre.org/data/definitions/90.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-327 (PeerOf)

## Observed examples (CVE)
- **CVE-2024-11022**: web server includes the nonce in its challenge/response mechanism, allowing a replay attack
- **CVE-2005-3435**: product authentication succeeds if user-provided MD5 hash matches the hash in its database; this can be subjected to replay attacks.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/301.html
