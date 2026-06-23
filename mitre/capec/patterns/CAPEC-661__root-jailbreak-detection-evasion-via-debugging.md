---
capec_id: CAPEC-661
name: Root/Jailbreak Detection Evasion via Debugging
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Very High
related_cwe: [CWE-489]
related_attack: []
url: https://capec.mitre.org/data/definitions/661.html
tags: [mitre-capec, attack-pattern, CAPEC-661]
---

# CAPEC-661 - Root/Jailbreak Detection Evasion via Debugging

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-661](https://capec.mitre.org/data/definitions/661.html)

## Description
An adversary inserts a debugger into the program entry point of a mobile application to modify the application binary, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Rooting/Jailbreaking a mobile device also provides users with access to system debuggers and disassemblers, which can be leveraged to exploit applications by dumping the application's memory at runtime in order to remove or bypass signature verification methods. This further allows the adversary to evade Root/Jailbreak detection mechanisms, which can result in execution of administrative commands, obtaining confidential data, impersonating legitimate users of the application, and more.

## Prerequisites
- A debugger must be able to be inserted into the targeted application.

## Skills required
- **High**: Knowledge about Root/Jailbreak detection and evasion techniques.
- **Medium**: Knowledge about runtime debugging.

## Resources required
- The adversary must have a Rooted/Jailbroken mobile device with debugging capabilities.

## Consequences
- **Access_Control**: Read Data (An adversary may leverage Root/Jailbreak Detection Evasion via Debugging in order to obtain sensitive information.)
- **Authorization**: Execute Unauthorized Commands (Through Root/Jailbreak Detection Evasion via Debugging, the adversary compromises the integrity of the application.), Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data (An adversary may leverage Root/Jailbreak Detection Evasion via Debugging in order to obtain sensitive information.)
- **Integrity**: Execute Unauthorized Commands (Through Root/Jailbreak Detection Evasion via Debugging, the adversary compromises the integrity of the application.)

## Execution flow
Execution Flow Explore Identify application with attack potential: The adversary searches for and identifies a mobile application that could be exploited for malicious purposes (e.g. banking, voting, or medical applications). Techniques Search application stores for mobile applications worth exploiting Experiment Debug the target application: The adversary inserts the debugger into the program entry point of the mobile application, after the application's signature has been identified, to dump its memory contents. Techniques Insert the debugger at the mobile application's program entry point, after the application's signature has been identified. Dump the memory region containing the now decrypted code from the address space of the binary. Remove application signature verification methods: Remove signature verification methods from the decrypted code and resign the application with a self-signed certificate. Exploit Execute the application and evade Root/Jailbreak detection methods: The application executes with the self-signed certificate, while believing it contains a trusted certificate. This now allows the adversary to evade Root/Jailbreak detection via code hooking or other methods. Techniques Optional: Hook code into the target application.

## Mitigations
- Instantiate checks within the application code that ensures debuggers are not attached.

## Related weaknesses (CWE)
- [CWE-489](https://cwe.mitre.org/data/definitions/489.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/661.html
