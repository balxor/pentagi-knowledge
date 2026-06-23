---
capec_id: CAPEC-624
name: Hardware Fault Injection
type: attack-pattern
abstraction: Meta
likelihood: Low
severity: High
related_cwe: [CWE-1247, CWE-1248, CWE-1256, CWE-1319, CWE-1332, CWE-1334, CWE-1338, CWE-1351]
related_attack: []
url: https://capec.mitre.org/data/definitions/624.html
tags: [mitre-capec, attack-pattern, CAPEC-624]
---

# CAPEC-624 - Hardware Fault Injection

**Abstraction:** Meta  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-624](https://capec.mitre.org/data/definitions/624.html)

## Description
The adversary uses disruptive signals or events, or alters the physical environment a device operates in, to cause faulty behavior in electronic devices. This can include electromagnetic pulses, laser pulses, clock glitches, ambient temperature extremes, and more. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior can be exploited to derive secret key information.

## Prerequisites
- Physical access to the system
- The adversary must be cognizant of where fault injection vulnerabilities exist in the system in order to leverage them for exploitation.

## Skills required
- **High**: Adversaries require non-trivial technical skills to create and implement fault injection attacks. Although this style of attack has become easier (commercial equipment and training classes are available to perform these attacks), they usual require significant setup and experimentation time during which physical access to the device is required.

## Resources required
- The relevant sensors and tools to detect and analyze fault/side-channel data from a system. A tool capable of injecting fault/side-channel data into a system or application.

## Consequences
- **Confidentiality**: Read Data (An adversary capable of successfully collecting and analyzing sensitive, fault/side-channel information, has compromised the confidentiality of that application or information system data.), Bypass Protection Mechanism (An adversary capable of successfully collecting and analyzing sensitive, fault/side-channel information, has compromised the confidentiality of that application or information system data.), Hide Activities (An adversary capable of successfully collecting and analyzing sensitive, fault/side-channel information, has compromised the confidentiality of that application or information system data.)
- **Integrity**: Execute Unauthorized Commands (If an adversary is able to inject data via a fault or side channel vulnerability towards malicious ends, the integrity of the application or information system will be compromised.)

## Mitigations
- Implement robust physical security countermeasures and monitoring.

## Related weaknesses (CWE)
- [CWE-1247](https://cwe.mitre.org/data/definitions/1247.html)
- [CWE-1248](https://cwe.mitre.org/data/definitions/1248.html)
- [CWE-1256](https://cwe.mitre.org/data/definitions/1256.html)
- [CWE-1319](https://cwe.mitre.org/data/definitions/1319.html)
- [CWE-1332](https://cwe.mitre.org/data/definitions/1332.html)
- [CWE-1334](https://cwe.mitre.org/data/definitions/1334.html)
- [CWE-1338](https://cwe.mitre.org/data/definitions/1338.html)
- [CWE-1351](https://cwe.mitre.org/data/definitions/1351.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/624.html
