---
capec_id: CAPEC-90
name: Reflection Attack in Authentication Protocol
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-301, CWE-303]
related_attack: []
url: https://capec.mitre.org/data/definitions/90.html
tags: [mitre-capec, attack-pattern, CAPEC-90]
---

# CAPEC-90 - Reflection Attack in Authentication Protocol

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-90](https://capec.mitre.org/data/definitions/90.html)

## Description
An adversary can abuse an authentication protocol susceptible to reflection attack in order to defeat it. Doing so allows the adversary illegitimate access to the target system, without possessing the requisite credentials. Reflection attacks are of great concern to authentication protocols that rely on a challenge-handshake or similar mechanism. An adversary can impersonate a legitimate user and can gain illegitimate access to the system by successfully mounting a reflection attack during authentication.

## Prerequisites
- The attacker must have direct access to the target server in order to successfully mount a reflection attack. An intermediate entity, such as a router or proxy, that handles these exchanges on behalf of the attacker inhibits the attackers' ability to attack the authentication protocol.

## Skills required
- **Medium**: The attacker needs to have knowledge of observing the protocol exchange and managing the required connections in order to issue and respond to challenges

## Resources required
- All that the attacker requires is a means to observe and understand the protocol exchanges in order to reflect the challenges appropriately.

## Consequences
- **Access_Control**: Gain Privileges, Bypass Protection Mechanism
- **Authorization**: Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Gain Privileges, Bypass Protection Mechanism, Read Data

## Execution flow
Execution Flow Explore Identify service with vulnerable handshake authentication: The adversary must first identify a vulnerable authentication protocol. The most common indication of an authentication protocol vulnerable to reflection attack is when the client initiates the handshake, rather than the server. This allows the client to get the server to encrypt targeted data using the server's pre-shared key. Experiment Send challenge to target server: The adversary opens a connection to the target server and sends it a challenge. This challenge is arbitrary and is simply used as a placeholder for the protocol in order to get the server to respond. Receive server challenge: The server responds by returning the challenge sent encrypted with the server's pre-shared key, as well as its own challenge to the attacker sent in plaintext. We will call this challenge sent by the server "C". C is very important and is stored off by the adversary for the next step. Initiate second handshake: Since the adversary does not possess the pre-shared key, they cannot encrypt C from the previous step in order for the server to authenticate them. To get around this, the adversary initiates a second connection to the server while still keeping the first connection alive. In the second connection, the adversary sends C as the initial client challenge, which rather than being arbitary like the first connection, is very intentional. Receive encrypted challenge: The server treats the intial client challenge in connection two as an arbitrary client challenge and responds by encrypting C with the pre-shared key. The server also sends a new challenge. The adversary ignores the server challenge and stores the encrypted version of C. The second connection is either terminated or left to expire by the adversary as it is no longer needed. Exploit The adversary now posseses the encrypted version of C that is obtained through connection two. The adversary continues the handshake in connection one by responding to the server with the encrypted version of C, verifying that they have access to the pre-shared key (when they actually do not). Because the server uses the same pre-shared key for all authentication it will decrypt C and authenticate the adversary for the first connection, giving the adversary illegitimate access to the target system.

## Mitigations
- The server must initiate the handshake by issuing the challenge. This ensures that the client has to respond before the exchange can move any further
- The use of HMAC to hash the response from the server can also be used to thwart reflection. The server responds by returning its own challenge as well as hashing the client's challenge, its own challenge and the pre-shared secret. Requiring the client to respond with the HMAC of the two challenges ensures that only the possessor of a valid pre-shared secret can successfully hash in the two values.
- Introducing a random nonce with each new connection ensures that the attacker cannot employ two connections to attack the authentication protocol

## Related weaknesses (CWE)
- [CWE-301](https://cwe.mitre.org/data/definitions/301.html)
- [CWE-303](https://cwe.mitre.org/data/definitions/303.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/90.html
