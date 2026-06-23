---
capec_id: CAPEC-251
name: Local Code Inclusion
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-829]
related_attack: [T1055]
url: https://capec.mitre.org/data/definitions/251.html
tags: [mitre-capec, attack-pattern, CAPEC-251]
---

# CAPEC-251 - Local Code Inclusion

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-251](https://capec.mitre.org/data/definitions/251.html)

## Description
The attacker forces an application to load arbitrary code files from the local machine. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load files that the attacker placed on the local machine during a prior attack, or to otherwise change the functionality of the targeted application in unexpected ways.

## Prerequisites
- The targeted application must have a bug that allows an adversary to control which code file is loaded at some juncture.
- Some variants of this attack may require that old versions of some code files be present and in predictable locations.

## Resources required
- The adversary needs to have enough access to the target application to control the identity of a locally included file. The attacker may also need to be able to upload arbitrary code files to the target machine, although any location for these files may be acceptable.

## Consequences
- **Confidentiality**: Read Data (An attacker may leverage local code inclusion in order to print sensitive data to a page, such as hidden configuration files or or password hashes.)
- **Integrity**: Execute Unauthorized Commands (Through local code inclusion, the adversary compromises the integrity of the application.)

## Mitigations
- Implementation: Avoid passing user input to filesystem or framework API. If necessary to do so, implement a specific, allowlist approach.

## Related weaknesses (CWE)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

## Related ATT&CK techniques
- T1055

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/251.html
