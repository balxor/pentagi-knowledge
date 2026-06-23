---
capec_id: CAPEC-27
name: Leveraging Race Conditions via Symbolic Links
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-367, CWE-61, CWE-662, CWE-689, CWE-667]
related_attack: []
url: https://capec.mitre.org/data/definitions/27.html
tags: [mitre-capec, attack-pattern, CAPEC-27]
---

# CAPEC-27 - Leveraging Race Conditions via Symbolic Links

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-27](https://capec.mitre.org/data/definitions/27.html)

## Description
This attack leverages the use of symbolic links (Symlinks) in order to write to sensitive files. An attacker can create a Symlink link to a target file not otherwise accessible to them. When the privileged program tries to create a temporary file with the same name as the Symlink link, it will actually write to the target file pointed to by the attackers' Symlink link. If the attacker can insert malicious content in the temporary file they will be writing to the sensitive file by using the Symlink. The race occurs because the system checks if the temporary file exists, then creates the file. The attacker would typically create the Symlink during the interval between the check and the creation of the temporary file.

## Prerequisites
- The attacker is able to create Symlink links on the target host.
- Tainted data from the attacker is used and copied to temporary files.
- The target host does insecure temporary file creation.

## Skills required
- **Medium**: This attack is sophisticated because the attacker has to overcome a few challenges such as creating symlinks on the target host during a precise timing, inserting malicious data in the temporary file and have knowledge about the temporary files created (file name and function which creates them).

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Resource Consumption (Denial of Service)
- **Confidentiality**: Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Verify that target host's platform supports symbolic links.: This attack pattern is only applicable on platforms that support symbolic links. Techniques Research target platform to determine whether it supports symbolic links. Create a symbolic link and ensure that it works as expected on the given platform. Examine application's file I/O behavior: Analyze the application's file I/O behavior to determine where it stores files, as well as the operations it performs to read/write files. Techniques Use kernel tracing utility such as ktrace to monitor application behavior. Use debugging utility such as File Monitor to monitor the application's filesystem I/O calls Watch temporary directories to see when temporary files are created, modified and deleted. Analyze source code for open-source systems like Linux, Apache, etc. Experiment Verify ability to write to filesystem: The attacker verifies ability to write to the target host's file system. Techniques Create a file that does not exist in the target directory (e.g. "touch temp.txt" in UNIX-like systems) On platforms that differentiate between file creation and file modification, if the target file that the application writes to already exists, attempt to modify it. Verify permissions on target directory Exploit Replace file with a symlink to a sensitive system file.: Between the time that the application checks to see if a file exists (or if the user has access to it) and the time the application actually opens the file, the attacker replaces the file with a symlink to a sensitive system file. Techniques Create an infinite loop containing commands such as "rm -f tempfile.dat; ln -s /etc/shadow tempfile.dat". Wait for an instance where the following steps occur in the given order: (1) Application ensures that tempfile.dat exists and that the user has access to it, (2) "rm -f tempfile.dat; ln -s /etc/shadow tempfile.dat", and (3) Application opens tempfile.dat for writing, and inadvertently opens /etc/shadow for writing instead. Use other techniques with debugging tools to replace the file between the time the application checks the file and the time the application opens it.

## Mitigations
- Use safe libraries when creating temporary files. For instance the standard library function mkstemp can be used to safely create temporary files. For shell scripts, the system utility mktemp does the same thing.
- Access to the directories should be restricted as to prevent attackers from manipulating the files. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file.
- Follow the principle of least privilege when assigning access rights to files.
- Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## Related weaknesses (CWE)
- [CWE-367](https://cwe.mitre.org/data/definitions/367.html)
- [CWE-61](https://cwe.mitre.org/data/definitions/61.html)
- [CWE-662](https://cwe.mitre.org/data/definitions/662.html)
- [CWE-689](https://cwe.mitre.org/data/definitions/689.html)
- [CWE-667](https://cwe.mitre.org/data/definitions/667.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/27.html
