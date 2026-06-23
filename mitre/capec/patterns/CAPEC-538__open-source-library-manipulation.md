---
capec_id: CAPEC-538
name: Open-Source Library Manipulation
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-494, CWE-829]
related_attack: [T1195.001]
url: https://capec.mitre.org/data/definitions/538.html
tags: [mitre-capec, attack-pattern, CAPEC-538]
---

# CAPEC-538 - Open-Source Library Manipulation

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-538](https://capec.mitre.org/data/definitions/538.html)

## Description
Adversaries implant malicious code in open source software (OSS) libraries to have it widely distributed, as OSS is commonly downloaded by developers and other users to incorporate into software development projects. The adversary can have a particular system in mind to target, or the implantation can be the first stage of follow-on attacks on many systems.

## Prerequisites
- Access to the open source code base being used by the manufacturer in a system being developed or currently deployed at a victim location.

## Skills required
- **High**: Advanced knowledge about the inclusion and specific usage of an open source code project within system being targeted for infiltration.

## Execution flow
Execution Flow Explore Determine the relevant open-source code project to target: The adversary will make the selection based on various criteria: Experiment Develop a plan for malicious contribution: The adversary develops a plan to contribute malicious code, taking the following into consideration: Exploit Execute the plan for malicious contribution: Write the code to be contributed based on the plan and then submit the contribution. Multiple commits, possibly using multiple identities, will help obscure the attack. Monitor the contribution site to try to determine if the code has been uploaded to the target system.

## Related weaknesses (CWE)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

## Related ATT&CK techniques
- T1195.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/538.html
