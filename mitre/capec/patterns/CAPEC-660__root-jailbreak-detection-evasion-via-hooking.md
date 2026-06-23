---
capec_id: CAPEC-660
name: Root/Jailbreak Detection Evasion via Hooking
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Very High
related_cwe: [CWE-829]
related_attack: [T1055]
url: https://capec.mitre.org/data/definitions/660.html
tags: [mitre-capec, attack-pattern, CAPEC-660]
---

# CAPEC-660 - Root/Jailbreak Detection Evasion via Hooking

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-660](https://capec.mitre.org/data/definitions/660.html)

## Description
An adversary forces a non-restricted mobile application to load arbitrary code or code files, via Hooking, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Adversaries may further leverage these capabilities to escalate privileges or bypass access control on legitimate applications. Although many mobile applications check if a mobile device is Rooted/Jailbroken prior to authorized use of the application, adversaries may be able to "hook" code in order to circumvent these checks. Successfully evading Root/Jailbreak detection allows an adversary to execute administrative commands, obtain confidential data, impersonate legitimate users of the application, and more.

## Prerequisites
- The targeted application must be non-restricted to allow code hooking.

## Skills required
- **High**: Knowledge about Root/Jailbreak detection and evasion techniques.
- **Medium**: Knowledge about code hooking.

## Resources required
- The adversary must have a Rooted/Jailbroken mobile device.
- The adversary needs to have enough access to the target application to control the included code or file.

## Consequences
- **Access_Control**: Read Data (An adversary may leverage Root/Jailbreak Detection Evasion via Hooking in order to obtain sensitive information.)
- **Authorization**: Execute Unauthorized Commands (Through Root/Jailbreak Detection Evasion via Hooking, the adversary compromises the integrity of the application.), Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data (An adversary may leverage Root/Jailbreak Detection Evasion via Hooking in order to obtain sensitive information.)
- **Integrity**: Execute Unauthorized Commands (Through Root/Jailbreak Detection Evasion via Hooking, the adversary compromises the integrity of the application.)

## Execution flow
Execution Flow Explore Identify application with attack potential: The adversary searches for and identifies a mobile application that could be exploited for malicious purposes (e.g. banking, voting, or medical applications). Techniques Search application stores for mobile applications worth exploiting Experiment Develop code to be hooked into chosen target application: The adversary develops code or leverages existing code that will be hooked into the target application in order to evade Root/Jailbreak detection methods. Techniques Develop code or leverage existing code to bypass Root/Jailbreak detection methods. Test the code to see if it works. Iteratively develop the code until Root/Jailbreak detection methods are evaded. Exploit Execute code hooking to evade Root/Jailbreak detection methods: Once hooking code has been developed or obtained, execute the code against the target application to evade Root/Jailbreak detection methods. Techniques Hook code into the target application.

## Mitigations
- Ensure mobile applications are signed appropriately to avoid code inclusion via hooking.
- Inspect the application's memory for suspicious artifacts, such as shared objects/JARs or dylibs, after other Root/Jailbreak detection methods.
- Inspect the application's stack trace for suspicious method calls.
- Allow legitimate native methods, and check for non-allowed native methods during Root/Jailbreak detection methods.
- For iOS applications, ensure application methods do not originate from outside of Apple's SDK.

## Related weaknesses (CWE)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

## Related ATT&CK techniques
- T1055

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/660.html
