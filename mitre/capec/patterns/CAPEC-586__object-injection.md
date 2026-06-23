---
capec_id: CAPEC-586
name: Object Injection
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: High
related_cwe: [CWE-502]
related_attack: []
url: https://capec.mitre.org/data/definitions/586.html
tags: [mitre-capec, attack-pattern, CAPEC-586]
---

# CAPEC-586 - Object Injection

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-586](https://capec.mitre.org/data/definitions/586.html)

## Description
An adversary attempts to exploit an application by injecting additional, malicious content during its processing of serialized objects. Developers leverage serialization in order to convert data or state into a static, binary format for saving to disk or transferring over a network. These objects are then deserialized when needed to recover the data/state. By injecting a malformed object into a vulnerable application, an adversary can potentially compromise the application by manipulating the deserialization process. This can result in a number of unwanted outcomes, including remote code execution.

## Prerequisites
- The target application must unserialize data before validation.

## Consequences
- **Authorization**: Execute Unauthorized Commands (Functions that assume information in the deserialized object is valid could be exploited.)
- **Availability**: Resource Consumption (If a function is making an assumption on when to terminate, based on a sentry in a string, it could easily never terminate and exhaust available resources.)
- **Integrity**: Modify Data (Attackers can modify objects or data that was assumed to be safe from modification.)

## Mitigations
- Implementation: Validate object before deserialization process
- Design: Limit which types can be deserialized.
- Implementation: Avoid having unnecessary types or gadgets available that can be leveraged for malicious ends. Use an allowlist of acceptable classes.
- Implementation: Keep session state on the server, when possible.

## Related weaknesses (CWE)
- [CWE-502](https://cwe.mitre.org/data/definitions/502.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/586.html
