---
capec_id: CAPEC-68
name: Subvert Code-signing Facilities
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Very High
related_cwe: [CWE-325, CWE-328, CWE-1326]
related_attack: [T1553.002]
url: https://capec.mitre.org/data/definitions/68.html
tags: [mitre-capec, attack-pattern, CAPEC-68]
---

# CAPEC-68 - Subvert Code-signing Facilities

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-68](https://capec.mitre.org/data/definitions/68.html)

## Description
Many languages use code signing facilities to vouch for code's identity and to thus tie code to its assigned privileges within an environment. Subverting this mechanism can be instrumental in an attacker escalating privilege. Any means of subverting the way that a virtual machine enforces code signing classifies for this style of attack.

## Prerequisites
- A framework-based language that supports code signing (such as, and most commonly, Java or .NET)
- Deployed code that has been signed by its authoring vendor, or a partner.
- The attacker will, for most circumstances, also need to be able to place code in the victim container. This does not necessarily mean that they will have to subvert host-level security, except when explicitly indicated.

## Skills required
- **High**: Subverting code signing is not a trivial activity. Most code signing and verification schemes are based on use of cryptography and the attacker needs to have an understanding of these cryptographic operations in good detail. Additionally the attacker also needs to be aware of the way memory is assigned and accessed by the container since, often, the only way to subvert code signing would be to patch the code in memory. Finally, a knowledge of the platform specific mechanisms of signing and verifying code is a must.

## Resources required
- The Attacker needs no special resources beyond the listed prerequisites in order to conduct this style of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Mitigations
- A given code signing scheme may be fallible due to improper use of cryptography. Developers must never roll out their own cryptography, nor should existing primitives be modified or ignored.
- If an attacker cannot attack the scheme directly, they might try to alter the environment that affects the signing and verification processes. A possible mitigation is to avoid reliance on flags or environment variables that are user-controllable.

## Related weaknesses (CWE)
- [CWE-325](https://cwe.mitre.org/data/definitions/325.html)
- [CWE-328](https://cwe.mitre.org/data/definitions/328.html)
- [CWE-1326](https://cwe.mitre.org/data/definitions/1326.html)

## Related ATT&CK techniques
- T1553.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/68.html
