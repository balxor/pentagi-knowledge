---
capec_id: CAPEC-6
name: Argument Injection
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-74, CWE-146, CWE-184, CWE-78, CWE-185, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/6.html
tags: [mitre-capec, attack-pattern, CAPEC-6]
---

# CAPEC-6 - Argument Injection

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-6](https://capec.mitre.org/data/definitions/6.html)

## Description
An attacker changes the behavior or state of a targeted application through injecting data or command syntax through the targets use of non-validated and non-filtered arguments of exposed services or methods.

## Prerequisites
- Target software fails to strip all user-supplied input of any content that could cause the shell to perform unexpected actions.
- Software must allow for unvalidated or unfiltered input to be executed on operating system shell, and, optionally, the system configuration must allow for output to be sent back to client.

## Skills required
- **Medium**: The attacker has to identify injection vector, identify the operating system-specific commands, and optionally collect the output.

## Resources required
- Ability to communicate synchronously or asynchronously with server. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Discovery of potential injection vectors: Using an automated tool or manual discovery, the attacker identifies services or methods with arguments that could potentially be used as injection vectors (OS, API, SQL procedures, etc.). Techniques Manually cover the application and record the possible places where arguments could be passed into external systems. Use a spider, for web applications, to create a list of URLs and associated inputs. Experiment 1. Attempt variations on argument content: Possibly using an automated tool, the attacker will perform injection variations of the arguments. Techniques Use a very large list of probe strings in order to detect if there is a positive result, and, what type of system has been targeted (if obscure). Use a proxy tool to record results, error messages and/or log if accessible. Exploit Abuse of the application: The attacker injects specific syntax into a particular argument in order to generate a specific malicious effect in the targeted application. Techniques Manually inject specific payload into targeted argument.

## Mitigations
- Design: Do not program input values directly on command shell, instead treat user input as guilty until proven innocent. Build a function that takes user input and converts it to applications specific types and values, stripping or filtering out all unauthorized commands and characters in the process.
- Design: Limit program privileges, so if metacharacters or other methods circumvent program input validation routines and shell access is attained then it is not running under a privileged account. chroot jails create a sandbox for the application to execute in, making it more difficult for an attacker to elevate privilege even in the case that a compromise has occurred.
- Implementation: Implement an audit log that is written to a separate host, in the event of a compromise the audit log may be able to provide evidence and details of the compromise.

## Related weaknesses (CWE)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-146](https://cwe.mitre.org/data/definitions/146.html)
- [CWE-184](https://cwe.mitre.org/data/definitions/184.html)
- [CWE-78](https://cwe.mitre.org/data/definitions/78.html)
- [CWE-185](https://cwe.mitre.org/data/definitions/185.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/6.html
