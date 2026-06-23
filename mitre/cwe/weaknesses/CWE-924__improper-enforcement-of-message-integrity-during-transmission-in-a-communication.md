---
cwe_id: CWE-924
name: Improper Enforcement of Message Integrity During Transmission in a Communication Channel
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/924.html
tags: [mitre-cwe, weakness, CWE-924]
---

# CWE-924 - Improper Enforcement of Message Integrity During Transmission in a Communication Channel

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-924](https://cwe.mitre.org/data/definitions/924.html)

## Description
The product establishes a communication channel with an endpoint and receives a message from that endpoint, but it does not sufficiently ensure that the message was not modified during transmission.

## Extended description
Attackers might be able to modify the message and spoof the endpoint by interfering with the data as it crosses the network or by redirecting the connection to a system under their control.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Confidentiality**: Gain Privileges or Assume Identity

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-345 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/924.html
