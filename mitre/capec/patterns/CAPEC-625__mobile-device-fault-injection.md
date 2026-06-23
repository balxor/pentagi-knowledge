---
capec_id: CAPEC-625
name: Mobile Device Fault Injection
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-1247, CWE-1248, CWE-1256, CWE-1319, CWE-1332, CWE-1334, CWE-1338, CWE-1351]
related_attack: []
url: https://capec.mitre.org/data/definitions/625.html
tags: [mitre-capec, attack-pattern, CAPEC-625]
---

# CAPEC-625 - Mobile Device Fault Injection

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-625](https://capec.mitre.org/data/definitions/625.html)

## Description
Fault injection attacks against mobile devices use disruptive signals or events (e.g. electromagnetic pulses, laser pulses, clock glitches, etc.) to cause faulty behavior. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior can be exploited to derive secret key information. Although this attack usually requires physical control of the mobile device, it is non-destructive, and the device can be used after the attack without any indication that secret keys were compromised.

## Skills required
- **High**: Adversaries require non-trivial technical skills to create and implement fault injection attacks on mobile devices. Although this style of attack has become easier (commercial equipment and training classes are available to perform these attacks), they usual require significant setup and experimentation time during which physical access to the device is required. This prerequisite makes the attack challenging to perform (assuming that physical security countermeasures and monitoring are in place).

## Consequences
- **Access_Control**: Read Data (Extract long-term secret keys (e.g. keys used for VPN or WiFi authentication and encryption) to enable decryption of intercepted VOIP traffic.)
- **Confidentiality**: Read Data (Extract long-term secret keys (e.g. keys used for VPN or WiFi authentication and encryption) to enable decryption of intercepted VOIP traffic.)

## Mitigations
- Strong physical security of all devices that contain secret key information. (even when devices are not in use)
- Frequent changes to secret keys and certificates.

## Related weaknesses (CWE)
- [CWE-1247](https://cwe.mitre.org/data/definitions/1247.html)
- [CWE-1248](https://cwe.mitre.org/data/definitions/1248.html)
- [CWE-1256](https://cwe.mitre.org/data/definitions/1256.html)
- [CWE-1319](https://cwe.mitre.org/data/definitions/1319.html)
- [CWE-1332](https://cwe.mitre.org/data/definitions/1332.html)
- [CWE-1334](https://cwe.mitre.org/data/definitions/1334.html)
- [CWE-1338](https://cwe.mitre.org/data/definitions/1338.html)
- [CWE-1351](https://cwe.mitre.org/data/definitions/1351.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/625.html
