---
capec_id: CAPEC-35
name: Leverage Executable Code in Non-Executable Files
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-94, CWE-96, CWE-95, CWE-97, CWE-272, CWE-59, CWE-282, CWE-270]
related_attack: [T1027.006, T1027.009, T1564.009]
url: https://capec.mitre.org/data/definitions/35.html
tags: [mitre-capec, attack-pattern, CAPEC-35]
---

# CAPEC-35 - Leverage Executable Code in Non-Executable Files

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)

## Description
An attack of this type exploits a system's trust in configuration and resource files. When the executable loads the resource (such as an image file or configuration file) the attacker has modified the file to either execute malicious code directly or manipulate the target process (e.g. application server) to execute based on the malicious configuration parameters. Since systems are increasingly interrelated mashing up resources from local and remote sources the possibility of this attack occurring is high.

## Prerequisites
- The attacker must have the ability to modify non-executable files consumed by the target software.

## Skills required
- **Low**: To identify and execute against an over-privileged system interface

## Resources required
- Ability to communicate synchronously or asynchronously with server that publishes an over-privileged directory, program, or interface. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Mitigations
- Design: Enforce principle of least privilege
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- Implementation: Implement host integrity monitoring to detect any unwanted altering of configuration files.
- Implementation: Ensure that files that are not required to execute, such as configuration files, are not over-privileged, i.e. not allowed to execute.

## Related weaknesses (CWE)
- [CWE-94](https://cwe.mitre.org/data/definitions/94.html)
- [CWE-96](https://cwe.mitre.org/data/definitions/96.html)
- [CWE-95](https://cwe.mitre.org/data/definitions/95.html)
- [CWE-97](https://cwe.mitre.org/data/definitions/97.html)
- [CWE-272](https://cwe.mitre.org/data/definitions/272.html)
- [CWE-59](https://cwe.mitre.org/data/definitions/59.html)
- [CWE-282](https://cwe.mitre.org/data/definitions/282.html)
- [CWE-270](https://cwe.mitre.org/data/definitions/270.html)

## Related ATT&CK techniques
- T1027.006
- T1027.009
- T1564.009

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/35.html
