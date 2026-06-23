---
capec_id: CAPEC-674
name: Design for FPGA Maliciously Altered
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.003]
url: https://capec.mitre.org/data/definitions/674.html
tags: [mitre-capec, attack-pattern, CAPEC-674]
---

# CAPEC-674 - Design for FPGA Maliciously Altered

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-674](https://capec.mitre.org/data/definitions/674.html)

## Description
<xhtml:p>An adversary alters the functionality of a field-programmable gate array (FPGA) by causing an FPGA configuration memory chip reload in order to introduce a malicious function that could result in the FPGA performing or enabling malicious functions on a host system. Prior to the memory chip reload, the adversary alters the program for the FPGA by adding a function to impact system operation.</xhtml:p>

## Prerequisites
- An adversary would need to have access to FPGA programming/configuration-related systems in a chip maker’s development environment where FPGAs can be initially configured prior to delivery to a customer or have access to such systems in a customer facility where end-user FPGA configuration/reconfiguration can be performed.

## Skills required
- **High**: An adversary would need to be skilled in FPGA programming in order to create/manipulate configurations in such a way that when loaded into an FPGA, the end user would be able to observe through testing all user-defined required functions but would be unaware of any additional functions the adversary may have introduced.

## Consequences
- **Integrity**: Alter Execution Logic

## Mitigations
- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management including for FPGA programming and program uploads to FPGA chips.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.

## Related ATT&CK techniques
- T1195.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/674.html
