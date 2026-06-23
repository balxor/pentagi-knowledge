---
capec_id: CAPEC-650
name: Upload a Web Shell to a Web Server
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: [CWE-287, CWE-553]
related_attack: [T1505.003]
url: https://capec.mitre.org/data/definitions/650.html
tags: [mitre-capec, attack-pattern, CAPEC-650]
---

# CAPEC-650 - Upload a Web Shell to a Web Server

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-650](https://capec.mitre.org/data/definitions/650.html)

## Description
By exploiting insufficient permissions, it is possible to upload a web shell to a web server in such a way that it can be executed remotely. This shell can have various capabilities, thereby acting as a "gateway" to the underlying web server. The shell might execute at the higher permission level of the web server, providing the ability the execute malicious code at elevated levels.

## Prerequisites
- The web server is susceptible to one of the various web application exploits that allows for uploading a shell file.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands
- **Confidentiality**: Read Data, Gain Privileges, Execute Unauthorized Commands
- **Integrity**: Execute Unauthorized Commands

## Mitigations
- Make sure your web server is up-to-date with all patches to protect against known vulnerabilities.
- Ensure that the file permissions in directories on the web server from which files can be execute is set to the "least privilege" settings, and that those directories contents is controlled by an allowlist.

## Related weaknesses (CWE)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)
- [CWE-553](https://cwe.mitre.org/data/definitions/553.html)

## Related ATT&CK techniques
- T1505.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/650.html
