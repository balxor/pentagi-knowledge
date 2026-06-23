---
capec_id: CAPEC-15
name: Command Delimiters
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-146, CWE-77, CWE-184, CWE-78, CWE-185, CWE-93, CWE-140, CWE-157, CWE-138, CWE-154, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/15.html
tags: [mitre-capec, attack-pattern, CAPEC-15]
---

# CAPEC-15 - Command Delimiters

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-15](https://capec.mitre.org/data/definitions/15.html)

## Description
An attack of this type exploits a programs' vulnerabilities that allows an attacker's commands to be concatenated onto a legitimate command with the intent of targeting other resources such as the file system or database. The system that uses a filter or denylist input validation, as opposed to allowlist validation is vulnerable to an attacker who predicts delimiters (or combinations of delimiters) not present in the filter or denylist. As with other injection attacks, the attacker uses the command delimiter payload as an entry point to tunnel through the application and activate additional attacks through SQL queries, shell commands, network scanning, and so on.

## Prerequisites
- Software's input validation or filtering must not detect and block presence of additional malicious command.

## Skills required
- **Medium**: The attacker has to identify injection vector, identify the specific commands, and optionally collect the output, i.e. from an interactive session.

## Resources required
- Ability to communicate synchronously or asynchronously with server. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Assess Target Runtime Environment: In situations where the runtime environment is not implicitly known, the attacker makes connections to the target system and tries to determine the system's runtime environment. Knowing the environment is vital to choosing the correct delimiters. Techniques Port mapping using network connection-based software (e.g., nmap, nessus, etc.) Port mapping by exploring the operating system (netstat, sockstat, etc.) TCP/IP Fingerprinting Induce errors to find informative error messages Survey the Application: The attacker surveys the target application, possibly as a valid and authenticated user Techniques Spidering web sites for all available links Inventory all application inputs Experiment Attempt delimiters in inputs: The attacker systematically attempts variations of delimiters on known inputs, observing the application's response each time. Techniques Inject command delimiters using network packet injection tools (netcat, nemesis, etc.) Inject command delimiters using web test frameworks (proxies, TamperData, custom programs, etc.) Enter command delimiters directly in input fields. Exploit Use malicious command delimiters: The attacker uses combinations of payload and carefully placed command delimiters to attack the software.

## Mitigations
- Design: Perform allowlist validation against a positive specification for command length, type, and parameters.
- Design: Limit program privileges, so if commands circumvent program input validation or filter routines then commands do not running under a privileged account
- Implementation: Perform input validation for all remote content.
- Implementation: Use type conversions such as JDBC prepared statements.

## Related weaknesses (CWE)
- [CWE-146](https://cwe.mitre.org/data/definitions/146.html)
- [CWE-77](https://cwe.mitre.org/data/definitions/77.html)
- [CWE-184](https://cwe.mitre.org/data/definitions/184.html)
- [CWE-78](https://cwe.mitre.org/data/definitions/78.html)
- [CWE-185](https://cwe.mitre.org/data/definitions/185.html)
- [CWE-93](https://cwe.mitre.org/data/definitions/93.html)
- [CWE-140](https://cwe.mitre.org/data/definitions/140.html)
- [CWE-157](https://cwe.mitre.org/data/definitions/157.html)
- [CWE-138](https://cwe.mitre.org/data/definitions/138.html)
- [CWE-154](https://cwe.mitre.org/data/definitions/154.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/15.html
