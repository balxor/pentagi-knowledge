---
capec_id: CAPEC-234
name: Hijacking a privileged process
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-732, CWE-648]
related_attack: []
url: https://capec.mitre.org/data/definitions/234.html
tags: [mitre-capec, attack-pattern, CAPEC-234]
---

# CAPEC-234 - Hijacking a privileged process

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-234](https://capec.mitre.org/data/definitions/234.html)

## Description
An adversary gains control of a process that is assigned elevated privileges in order to execute arbitrary code with those privileges. Some processes are assigned elevated privileges on an operating system, usually through association with a particular user, group, or role. If an attacker can hijack this process, they will be able to assume its level of privilege in order to execute their own code.

## Prerequisites
- The targeted process or operating system must contain a bug that allows attackers to hijack the targeted process.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Execution flow
Execution Flow Explore Find process with elevated priveleges: The adversary probes for processes running with elevated privileges. Techniques On Windows, use the process explorer's security tab to see if a process is running with administror privileges. On Linux, use the ps command to view running processes and pipe the output to a search for a particular user, or the root user. Experiment Find vulnerability in running process: The adversary looks for a vulnerability in the running process that would allow for arbitrary code execution with the privilege of the running process. Techniques Look for improper input validation Look for a buffer overflow which may be exploited if an adversary can inject unvalidated data. Utilize system utilities that support process control that have been inadequately secured Exploit Execute arbitrary code: The adversary exploits the vulnerability that they have found and hijacks the running process.

## Related weaknesses (CWE)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)
- [CWE-648](https://cwe.mitre.org/data/definitions/648.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/234.html
