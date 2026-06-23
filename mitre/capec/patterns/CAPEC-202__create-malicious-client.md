---
capec_id: CAPEC-202
name: Create Malicious Client
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-602]
related_attack: []
url: https://capec.mitre.org/data/definitions/202.html
tags: [mitre-capec, attack-pattern, CAPEC-202]
---

# CAPEC-202 - Create Malicious Client

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-202](https://capec.mitre.org/data/definitions/202.html)

## Description
An adversary creates a client application to interface with a target service where the client violates assumptions the service makes about clients. Services that have designated client applications (as opposed to services that use general client applications, such as IMAP or POP mail servers which can interact with any IMAP or POP client) may assume that the client will follow specific procedures.

## Extended description
For example, servers may assume that clients will accurately compute values (such as prices), will send correctly structured messages, and will attempt to ensure efficient interactions with the server. By reverse-engineering a client and creating their own version, an adversary can take advantage of these assumptions to abuse service functionality. For example, a purchasing service might send a unit price to its client and expect the client to correctly compute the total cost of a purchase. If the adversary uses a malicious client, however, the adversary could ignore the server input and declare any total price. Likewise, an adversary could configure the client to retain network or other server resources for longer than legitimately necessary in order to degrade server performance. Even services with general clients can be susceptible to this attack if they assume certain client behaviors. However, such services generally can make fewer assumptions about the behavior of their clients in the first place and, as such, are less likely to make assumptions that an adversary can exploit.

## Prerequisites
- The targeted service must make assumptions about the behavior of the client application that interacts with it, which can be abused by an adversary.

## Resources required
- The adversary must be able to reverse engineer a client of the targeted service. However, the adversary does not need to reverse engineer all client functionality - they only need to recreate enough of the functionality to access the desired server functionality.

## Related weaknesses (CWE)
- [CWE-602](https://cwe.mitre.org/data/definitions/602.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/202.html
