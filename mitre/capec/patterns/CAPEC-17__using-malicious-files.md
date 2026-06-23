---
capec_id: CAPEC-17
name: Using Malicious Files
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-732, CWE-285, CWE-272, CWE-59, CWE-282, CWE-270, CWE-693]
related_attack: [T1574.005, T1574.010]
url: https://capec.mitre.org/data/definitions/17.html
tags: [mitre-capec, attack-pattern, CAPEC-17]
---

# CAPEC-17 - Using Malicious Files

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-17](https://capec.mitre.org/data/definitions/17.html)

## Description
An attack of this type exploits a system's configuration that allows an adversary to either directly access an executable file, for example through shell access; or in a possible worst case allows an adversary to upload a file and then execute it. Web servers, ftp servers, and message oriented middleware systems which have many integration points are particularly vulnerable, because both the programmers and the administrators must be in synch regarding the interfaces and the correct privileges for each interface.

## Prerequisites
- System's configuration must allow an attacker to directly access executable files or upload files to execute. This means that any access control system that is supposed to mediate communications between the subject and the object is set incorrectly or assumes a benign environment.

## Skills required
- **Low**: To identify and execute against an over-privileged system interface

## Resources required
- Ability to communicate synchronously or asynchronously with server that publishes an over-privileged directory, program, or interface. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data, Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Determine File/Directory Configuration: The adversary looks for misconfigured files or directories on a system that might give executable access to an overly broad group of users. Techniques Through shell access to a system, use the command "ls -l" to view permissions for files and directories. Experiment Upload Malicious Files: If the adversary discovers a directory that has executable permissions, they will attempt to upload a malicious file to execute. Techniques Upload a malicious file through a misconfigured FTP server. Exploit Execute Malicious File: The adversary either executes the uploaded malicious file, or executes an existing file that has been misconfigured to allow executable access to the adversary.

## Mitigations
- Design: Enforce principle of least privilege
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.

## Related weaknesses (CWE)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-272](https://cwe.mitre.org/data/definitions/272.html)
- [CWE-59](https://cwe.mitre.org/data/definitions/59.html)
- [CWE-282](https://cwe.mitre.org/data/definitions/282.html)
- [CWE-270](https://cwe.mitre.org/data/definitions/270.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

## Related ATT&CK techniques
- T1574.005
- T1574.010

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/17.html
