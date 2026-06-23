---
capec_id: CAPEC-182
name: Flash Injection
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Medium
related_cwe: [CWE-20, CWE-184, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/182.html
tags: [mitre-capec, attack-pattern, CAPEC-182]
---

# CAPEC-182 - Flash Injection

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-182](https://capec.mitre.org/data/definitions/182.html)

## Description
An attacker tricks a victim to execute malicious flash content that executes commands or makes flash calls specified by the attacker. One example of this attack is cross-site flashing, an attacker controlled parameter to a reference call loads from content specified by the attacker.

## Prerequisites
- The target must be capable of running Flash applications. In some cases, the victim must follow an attacker-supplied link.

## Skills required
- **Medium**: The attacker needs to have knowledge of Flash, especially how to insert content the executes commands.

## Resources required
- None: No specialized resources are required to execute this type of attack. The attacker may need to be able to serve the injected Flash content.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Other (Information Leakage), Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Find Injection Entry Points: The attacker first takes an inventory of the entry points of the application. Techniques Spider the website for all available URLs that reference a Flash application. List all uninitialized global variables (such as _root.*, _global.*, _level0.*) in ActionScript, registered global variables in included files, load variables to external movies. Experiment Determine the application's susceptibility to Flash injection: Determine the application's susceptibility to Flash injection. For each URL identified in the explore phase, the attacker attempts to use various techniques such as direct load asfunction, controlled evil page/host, Flash HTML injection, and DOM injection to determine whether the application is susceptible to Flash injection. Techniques Test the page using direct load asfunction, getURL,javascript:gotRoot("")///d.jpg Test the page using controlled evil page/host, http://example.com/evil.swf Test the page using Flash HTML injection, "'> Test the page using DOM injection, (gotRoot('')) Exploit Inject malicious content into target: Inject malicious content into target utilizing vulnerable injection vectors identified in the Experiment phase

## Mitigations
- Implementation: remove sensitive information such as user name and password in the SWF file.
- Implementation: use validation on both client and server side.
- Implementation: remove debug information.
- Implementation: use SSL when loading external data
- Implementation: use crossdomain.xml file to allow the application domain to load stuff or the SWF file called by other domain.

## Related weaknesses (CWE)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-184](https://cwe.mitre.org/data/definitions/184.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/182.html
