---
cwe_id: CWE-322
name: Key Exchange without Entity Authentication
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/322.html
tags: [mitre-cwe, weakness, CWE-322]
---

# CWE-322 - Key Exchange without Entity Authentication

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-322](https://cwe.mitre.org/data/definitions/322.html)

## Description
The product performs a key exchange with an actor without verifying the identity of that actor.

## Extended description
Performing a key exchange will preserve the integrity of the information sent between two entities, but this will not guarantee that the entities are who they claim they are. This may enable an attacker to impersonate an actor by modifying traffic between the two entities. Typically, this involves a victim client that contacts a malicious server that is impersonating a trusted server. If the client skips authentication or ignores an authentication failure, the malicious server may request authentication information from the user. The malicious server can then use this authentication information to log in to the trusted server using the victim's credentials, sniff traffic between the victim and trusted server, etc.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Ensure that proper authentication is included in the system design.
- **Implementation**: Understand and properly implement all checks necessary to ensure the identity of entities involved in encrypted communications.

## Related weaknesses
- CWE-306 (ChildOf)
- CWE-923 (CanPrecede)
- CWE-295 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/322.html
