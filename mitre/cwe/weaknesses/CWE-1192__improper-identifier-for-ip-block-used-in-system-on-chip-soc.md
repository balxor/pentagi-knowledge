---
cwe_id: CWE-1192
name: Improper Identifier for IP Block used in System-On-Chip (SOC)
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, System on Chip]
related_capec: [CAPEC-113]
url: https://cwe.mitre.org/data/definitions/1192.html
tags: [mitre-cwe, weakness, CWE-1192]
---

# CWE-1192 - Improper Identifier for IP Block used in System-On-Chip (SOC)

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1192](https://cwe.mitre.org/data/definitions/1192.html)

## Description
The System-on-Chip (SoC) does not have unique, immutable identifiers for each of its components.

## Extended description
A System-on-Chip (SoC) comprises several components (IP) with varied trust requirements. It is required that each IP is identified uniquely and should distinguish itself from other entities in the SoC without any ambiguity. The unique secured identity is required for various purposes. Most of the time the identity is used to route a transaction or perform certain actions, including resetting, retrieving a sensitive information, and acting upon or on behalf of something else. There are several variants of this weakness: A "missing" identifier is when the SoC does not define any mechanism to uniquely identify the IP. An "insufficient" identifier might provide some defenses - for example, against the most common attacks - but it does not protect against everything that is intended. A "misconfigured" mechanism occurs when a mechanism is available but not implemented correctly. An "ignored" identifier occurs when the SoC/IP has not applied any policies or does not act upon the identifier securely.

## Applicable platforms / languages
Not Language-Specific, System on Chip

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Every identity generated in the SoC should be unique and immutable in hardware. The actions that an IP is trusted or not trusted should be clearly defined, implemented, configured, and tested. If the definition is implemented via a policy, then the policy should be immutable or protected with clear authentication and authorization.

## Related attack patterns (CAPEC)
- [CAPEC-113](https://capec.mitre.org/data/definitions/113.html)

## Related weaknesses
- CWE-657 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1192.html
