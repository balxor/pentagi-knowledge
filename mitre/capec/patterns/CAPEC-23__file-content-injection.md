---
capec_id: CAPEC-23
name: File Content Injection
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/23.html
tags: [mitre-capec, attack-pattern, CAPEC-23]
---

# CAPEC-23 - File Content Injection

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-23](https://capec.mitre.org/data/definitions/23.html)

## Description
An adversary poisons files with a malicious payload (targeting the file systems accessible by the target software), which may be passed through by standard channels such as via email, and standard web content like PDF and multimedia files. The adversary exploits known vulnerabilities or handling routines in the target processes, in order to exploit the host's trust in executing remote content, including binary files.

## Extended description
Vulnerabilities of this type have been found in a wide variety of commercial applications from Microsoft Office to Adobe Acrobat and Apple Safari web browser. When the adversary knows the standard handling routines and can identify vulnerabilities and entry points, they can be exploited by otherwise seemingly normal content. Once the attack is executed, the adversary's program can access relative directories such as C:\Program Files or other standard system directories to launch further attacks. In a worst case scenario, these programs are combined with other propagation logic and work as a virus.

## Prerequisites
- The target software must consume files.
- The adversary must have access to modify files that the target software will consume.

## Skills required
- **Medium**: How to poison a file with malicious payload that will exploit a vulnerability when the file is opened. The adversary must also know how to place the file onto a system where it will be opened by an unsuspecting party, or force the file to be opened.

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Mitigations
- Design: Enforce principle of least privilege
- Design: Validate all input for content including files. Ensure that if files and remote content must be accepted that once accepted, they are placed in a sandbox type location so that lower assurance clients cannot write up to higher assurance processes (like Web server processes for example)
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Implementation: Virus scanning on host
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.

## Related weaknesses (CWE)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/23.html
