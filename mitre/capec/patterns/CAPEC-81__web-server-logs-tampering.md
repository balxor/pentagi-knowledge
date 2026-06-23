---
capec_id: CAPEC-81
name: Web Server Logs Tampering
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-117, CWE-93, CWE-75, CWE-221, CWE-96, CWE-20, CWE-150, CWE-276, CWE-279, CWE-116]
related_attack: []
url: https://capec.mitre.org/data/definitions/81.html
tags: [mitre-capec, attack-pattern, CAPEC-81]
---

# CAPEC-81 - Web Server Logs Tampering

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)

## Description
Web Logs Tampering attacks involve an attacker injecting, deleting or otherwise tampering with the contents of web logs typically for the purposes of masking other malicious behavior. Additionally, writing malicious data to log files may target jobs, filters, reports, and other agents that process the logs in an asynchronous attack pattern. This pattern of attack is similar to "Log Injection-Tampering-Forging" except that in this case, the attack is targeting the logs of the web server and not the application.

## Prerequisites
- Target server software must be a HTTP server that performs web logging.

## Skills required
- **Low**: To input faked entries into Web logs

## Resources required
- Ability to send specially formatted HTTP request to web server

## Consequences
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Determine Application Web Server Log File Format: The attacker observes the system and looks for indicators of which logging utility is being used by the web server. Techniques Determine logging utility being used by application web server (e.g. log4j), only possible if the application is known by the attacker or if the application returns error messages with logging utility information. Experiment Determine Injectable Content: The attacker launches various logged actions with malicious data to determine what sort of log injection is possible. Techniques Attacker triggers logged actions with maliciously crafted data as inputs, parameters, arguments, etc. Exploit Manipulate Log Files: The attacker alters the log contents either directly through manipulation or forging or indirectly through injection of specially crafted request that the web server will receive and write into the logs. This type of attack typically follows another attack and is used to try to cover the traces of the previous attack. Techniques Indirectly through injection, use carriage return and/or line feed characters to start a new line in the log file, and then, add a fake entry. For example: The HTTP request for "/index.html%0A%0DIP_ADDRESS- - DATE_FORMAT] "GET /forged-path HTTP/1.1" 200 - "-" USER_AGENT" may add the log line into Apache "access_log" (for example). Different applications may require different encodings of the carriage return and line feed characters. Directly through log file or database manipulation, use carriage return and/or line feed characters to start a new line in the log file, and then, add a fake entry. For example: The HTTP request for "/index.html%0A%0DIP_ADDRESS- - DATE_FORMAT] "GET /forged-path HTTP/1.1" 200 - "-" USER_AGENT" may add the log line into Apache "access_log" (for example). Different applications may require different encodings of the carriage return and line feed characters. Directly through log file or database manipulation, modify existing log entries.

## Mitigations
- Design: Use input validation before writing to web log
- Design: Validate all log data before it is output

## Related weaknesses (CWE)
- [CWE-117](https://cwe.mitre.org/data/definitions/117.html)
- [CWE-93](https://cwe.mitre.org/data/definitions/93.html)
- [CWE-75](https://cwe.mitre.org/data/definitions/75.html)
- [CWE-221](https://cwe.mitre.org/data/definitions/221.html)
- [CWE-96](https://cwe.mitre.org/data/definitions/96.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-150](https://cwe.mitre.org/data/definitions/150.html)
- [CWE-276](https://cwe.mitre.org/data/definitions/276.html)
- [CWE-279](https://cwe.mitre.org/data/definitions/279.html)
- [CWE-116](https://cwe.mitre.org/data/definitions/116.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/81.html
