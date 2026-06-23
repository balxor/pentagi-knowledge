---
capec_id: CAPEC-88
name: OS Command Injection
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-78, CWE-88, CWE-20, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/88.html
tags: [mitre-capec, attack-pattern, CAPEC-88]
---

# CAPEC-88 - OS Command Injection

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-88](https://capec.mitre.org/data/definitions/88.html)

## Description
In this type of an attack, an adversary injects operating system commands into existing application functions. An application that uses untrusted input to build command strings is vulnerable. An adversary can leverage OS command injection in an application to elevate privileges, execute arbitrary commands and compromise the underlying operating system.

## Prerequisites
- User controllable input used as part of commands to the underlying operating system.

## Skills required
- **High**: The attacker needs to have knowledge of not only the application to exploit but also the exact nature of commands that pertain to the target operating system. This may involve, though not always, knowledge of specific assembly commands for the platform.

## Consequences
- **Access_Control**: Gain Privileges, Bypass Protection Mechanism
- **Authorization**: Gain Privileges, Bypass Protection Mechanism
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism, Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Identify inputs for OS commands: The attacker determines user controllable input that gets passed as part of a command to the underlying operating system. Techniques Port mapping. Identify ports that the system is listening on, and attempt to identify inputs and protocol types on those ports. TCP/IP Fingerprinting. The attacker uses various software to make connections or partial connections and observe idiosyncratic responses from the operating system. Using those responses, they attempt to guess the actual operating system. Induce errors to find informative error messages Survey the Application: The attacker surveys the target application, possibly as a valid and authenticated user Techniques Spidering web sites for all available links Inventory all application inputs Experiment Vary inputs, looking for malicious results.: Depending on whether the application being exploited is a remote or local one the attacker crafts the appropriate malicious input, containing OS commands, to be passed to the application Techniques Inject command delimiters using network packet injection tools (netcat, nemesis, etc.) Inject command delimiters using web test frameworks (proxies, TamperData, custom programs, etc.) Exploit Execute malicious commands: The attacker may steal information, install a back door access mechanism, elevate privileges or compromise the system in some other way. Techniques The attacker executes a command that stores sensitive information into a location where they can retrieve it later (perhaps using a different command injection).

## Mitigations
- Use language APIs rather than relying on passing data to the operating system shell or command line. Doing so ensures that the available protection mechanisms in the language are intact and applicable.
- Filter all incoming data to escape or remove characters or strings that can be potentially misinterpreted as operating system or shell commands
- All application processes should be run with the minimal privileges required. Also, processes must shed privileges as soon as they no longer require them.

## Related weaknesses (CWE)
- [CWE-78](https://cwe.mitre.org/data/definitions/78.html)
- [CWE-88](https://cwe.mitre.org/data/definitions/88.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/88.html
