---
capec_id: CAPEC-237
name: Escaping a Sandbox by Calling Code in Another Language
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Very High
related_cwe: [CWE-693]
related_attack: []
url: https://capec.mitre.org/data/definitions/237.html
tags: [mitre-capec, attack-pattern, CAPEC-237]
---

# CAPEC-237 - Escaping a Sandbox by Calling Code in Another Language

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-237](https://capec.mitre.org/data/definitions/237.html)

## Description
The attacker may submit malicious code of another language to obtain access to privileges that were not intentionally exposed by the sandbox, thus escaping the sandbox. For instance, Java code cannot perform unsafe operations, such as modifying arbitrary memory locations, due to restrictions placed on it by the Byte code Verifier and the JVM. If allowed, Java code can call directly into native C code, which may perform unsafe operations, such as call system calls and modify arbitrary memory locations on their behalf. To provide isolation, Java does not grant untrusted code with unmediated access to native C code. Instead, the sandboxed code is typically allowed to call some subset of the pre-existing native code that is part of standard libraries.

## Skills required
- **High**: The attacker must have a good knowledge of the platform specific mechanisms of signing and verifying code. Most code signing and verification schemes are based on use of cryptography, the attacker needs to have an understand of these cryptographic operations in good detail.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Bypass Protection Mechanism, Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Probing: The attacker probes the target application to see whether calling code of another language is allowed within a sandbox. Techniques The attacker probes the target application to see whether calling code of another language is allowed within a sandbox. Analysis: The attacker analyzes the target application to get a list of cross code weaknesses in the standard libraries of the sandbox. Techniques The attacker analyzes the target application to get a list of cross code weaknesses in the standard libraries of the sandbox. Experiment Verify the exploitable security weaknesses: The attacker tries to craft malicious code of another language allowed by the sandbox to verify the security weaknesses of the standard libraries found in the Explore phase. Techniques The attacker tries to explore the security weaknesses by calling malicious code of another language allowed by the sandbox. Exploit Exploit the security weaknesses in the standard libraries: The attacker calls malicious code of another language to exploit the security weaknesses in the standard libraries verified in the Experiment phase. The attacker will be able to obtain access to privileges that were not intentionally exposed by the sandbox, thus escaping the sandbox. Techniques The attacker calls malicious code of another language to exploit the security weaknesses in the standard libraries.

## Mitigations
- Assurance: Sanitize the code of the standard libraries to make sure there is no security weaknesses in them.
- Design: Use obfuscation and other techniques to prevent reverse engineering the standard libraries.
- Assurance: Use static analysis tool to do code review and dynamic tool to do penetration test on the standard library.
- Configuration: Get latest updates for the computer.

## Related weaknesses (CWE)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/237.html
