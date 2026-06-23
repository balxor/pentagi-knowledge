---
capec_id: CAPEC-445
name: Malicious Logic Insertion into Product Software via Configuration Management Manipulation
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: []
related_attack: [T1195.001]
url: https://capec.mitre.org/data/definitions/445.html
tags: [mitre-capec, attack-pattern, CAPEC-445]
---

# CAPEC-445 - Malicious Logic Insertion into Product Software via Configuration Management Manipulation

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-445](https://capec.mitre.org/data/definitions/445.html)

## Description
<xhtml:p>An adversary exploits a configuration management system so that malicious logic is inserted into a software products build, update or deployed environment. If an adversary can control the elements included in a product's configuration management for build they can potentially replace, modify or insert code files containing malicious logic. If an adversary can control elements of a product's ongoing operational configuration management baseline they can potentially force clients receiving updates from the system to install insecure software when receiving updates from the server.</xhtml:p>

## Extended description
Configuration management servers operate on the basis of a client pool, instructing each client on which software to install. In some cases the configuration management server will automate the software installation process. A malicious insider or an adversary who has compromised the server can alter the software baseline that clients must install, allowing the adversary to compromise a large number of satellite machines using the configuration management system. If an adversary can control elements of a product's configuration management for its deployed environment they can potentially alter fundamental security properties of the system based on assumptions that secure configurations are in place. It is also worth noting that this attack can occur during initial product development or throughout a product's sustainment.

## Prerequisites
- Access to the configuration management system during deployment or currently deployed at a victim location. This access is often obtained via insider access or by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- **Authorization**: Execute Unauthorized Commands

## Mitigations
- Assess software during development and prior to deployment to ensure that it functions as intended and without any malicious functionality.
- Leverage anti-virus products to detect and quarantine software with known virus.

## Related ATT&CK techniques
- T1195.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/445.html
