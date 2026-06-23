---
capec_id: CAPEC-76
name: Manipulating Web Input to File System Calls
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-23, CWE-22, CWE-73, CWE-77, CWE-346, CWE-348, CWE-285, CWE-272, CWE-59, CWE-74, CWE-15]
related_attack: []
url: https://capec.mitre.org/data/definitions/76.html
tags: [mitre-capec, attack-pattern, CAPEC-76]
---

# CAPEC-76 - Manipulating Web Input to File System Calls

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)

## Description
An attacker manipulates inputs to the target software which the target software passes to file system calls in the OS. The goal is to gain access to, and perhaps modify, areas of the file system that the target software did not intend to be accessible.

## Prerequisites
- Program must allow for user controlled variables to be applied directly to the filesystem

## Skills required
- **Low**: To identify file system entry point and execute against an over-privileged system interface

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Fingerprinting of the operating system: In order to create a valid file injection, the attacker needs to know what the underlying OS is so that the proper file seperator is used. Techniques Port mapping. Identify ports that the system is listening on, and attempt to identify inputs and protocol types on those ports. TCP/IP Fingerprinting. The attacker uses various software to make connections or partial connections and observe idiosyncratic responses from the operating system. Using those responses, they attempt to guess the actual operating system. Induce errors to find informative error messages Survey the Application to Identify User-controllable Inputs: The attacker surveys the target application to identify all user-controllable inputs, possibly as a valid and authenticated user Techniques Spider web sites for all available links, entry points to the web site. Manually explore application and inventory all application inputs Experiment Vary inputs, looking for malicious results: Depending on whether the application being exploited is a remote or local one, the attacker crafts the appropriate malicious input containing the path of the targeted file or other file system control syntax to be passed to the application Techniques Inject context-appropriate malicious file path using network packet injection tools (netcat, nemesis, etc.) Inject context-appropriate malicious file path using web test frameworks (proxies, TamperData, custom programs, etc.) or simple HTTP requests Inject context-appropriate malicious file system control syntax Exploit Manipulate files accessible by the application: The attacker may steal information or directly manipulate files (delete, copy, flush, etc.) Techniques The attacker injects context-appropriate malicious file path to access the content of the targeted file. The attacker injects context-appropriate malicious file system control syntax to access the content of the targeted file. The attacker injects context-appropriate malicious file path to cause the application to create, delete a targeted file. The attacker injects context-appropriate malicious file system control syntax to cause the application to create, delete a targeted file. The attacker injects context-appropriate malicious file path in order to manipulate the meta-data of the targeted file. The attacker injects context-appropriate malicious file system control syntax in order to manipulate the meta-data of the targeted file.

## Mitigations
- Design: Enforce principle of least privilege.
- Design: Ensure all input is validated, and does not contain file system commands
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Design: For interactive user applications, consider if direct file system interface is necessary, instead consider having the application proxy communication.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.

## Related weaknesses (CWE)
- [CWE-23](https://cwe.mitre.org/data/definitions/23.html)
- [CWE-22](https://cwe.mitre.org/data/definitions/22.html)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CWE-77](https://cwe.mitre.org/data/definitions/77.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-348](https://cwe.mitre.org/data/definitions/348.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-272](https://cwe.mitre.org/data/definitions/272.html)
- [CWE-59](https://cwe.mitre.org/data/definitions/59.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/76.html
