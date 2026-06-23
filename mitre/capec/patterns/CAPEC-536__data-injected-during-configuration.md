---
capec_id: CAPEC-536
name: Data Injected During Configuration
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: [CWE-284]
related_attack: []
url: https://capec.mitre.org/data/definitions/536.html
tags: [mitre-capec, attack-pattern, CAPEC-536]
---

# CAPEC-536 - Data Injected During Configuration

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-536](https://capec.mitre.org/data/definitions/536.html)

## Description
An attacker with access to data files and processes on a victim's system injects malicious data into critical operational data during configuration or recalibration, causing the victim's system to perform in a suboptimal manner that benefits the adversary.

## Prerequisites
- The attacker must have previously compromised the victim's systems or have physical access to the victim's systems.
- Advanced knowledge of software and hardware capabilities of a manufacturer's product.

## Skills required
- **High**: Ability to generate and inject false data into operational data into a system with the intent of causing the victim to alter the configuration of the system.

## Execution flow
Execution Flow Explore Determine configuration process: The adversary, through a previously compromised system, either remotely or physically, determines what the configuration process is. They look at configuration files, data files, and running processes on the system to identify areas where they could inject malicious data. Determine when configuration occurs: The adversary needs to then determine when configuration or recalibration of a system occurs so they know when to inject malicious data. Techniques Look for a weekly update cycle or repeated update schedule. Insert a malicious process into the target system that notifies the adversary when configuration is occurring. Experiment Determine malicious data to inject: By looking at the configuration process, the adversary needs to determine what malicious data they want to insert and where to insert it. Techniques Add false log data Change configuration files Change data files Exploit Inject malicious data: Right before, or during system configuration, the adversary injects the malicious data. This leads to the system behaving in a way that is beneficial to the adversary and is often followed by other attacks.

## Mitigations
- Ensure that proper access control is implemented on all systems to prevent unauthorized access to system files and processes.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/536.html
