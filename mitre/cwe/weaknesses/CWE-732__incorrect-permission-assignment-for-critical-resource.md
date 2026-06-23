---
cwe_id: CWE-732
name: Incorrect Permission Assignment for Critical Resource
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Cloud Computing]
related_capec: [CAPEC-1, CAPEC-122, CAPEC-127, CAPEC-17, CAPEC-180, CAPEC-206, CAPEC-234, CAPEC-60, CAPEC-61, CAPEC-62, CAPEC-642]
url: https://cwe.mitre.org/data/definitions/732.html
tags: [mitre-cwe, weakness, CWE-732]
---

# CWE-732 - Incorrect Permission Assignment for Critical Resource

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-732](https://cwe.mitre.org/data/definitions/732.html)

## Description
The product specifies permissions for a security-critical resource in a way that allows that resource to be read or modified by unintended actors.

## Extended description
When a resource is given a permission setting that provides access to a wider range of actors than required, it could lead to the exposure of sensitive information, or the modification of that resource by unintended parties. This is especially dangerous when the resource is related to program configuration, execution, or sensitive user data. For example, consider a misconfigured storage account for the cloud that can be read or written by a public or anonymous user.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Cloud Computing

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories
- **Access Control**: Gain Privileges or Assume Identity
- **Integrity, Other**: Modify Application Data, Other

## Potential mitigations
- **Implementation**: When using a critical resource such as a configuration file, check to see if the resource has insecure permissions (such as being modifiable by any regular user) [REF-62], and generate an error or even exit the software if there is a possibility that the resource could have been modified by an unauthorized party.
- **Architecture and Design**: Divide the software into anonymous, normal, privileged, and administrative areas. Reduce the attack surface by carefully defining distinct user groups, privileges, and/or roles. Map these against data, functionality, and the related resources. Then set the permissions accordingly. This will allow you to maintain more fine-grained control over your resources. [REF-207]
- **Architecture and Design, Operation**: Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.
- **Implementation, Installation**: During program startup, explicitly set the default permissions or umask to the most restrictive setting possible. Also set the appropriate permissions during program installation. This will prevent you from inheriting insecure permissions from any user who installs or runs the program.
- **System Configuration**: For all configuration files, executables, and libraries, make sure that they are only readable and writable by the software's administrator.
- **Documentation**: Do not suggest insecure configuration changes in documentation, especially if those configurations can extend to resources and other programs that are outside the scope of the application.
- **Installation**: Do not assume that a system administrator will manually change the configuration to the settings that are recommended in the software's manual.
- **Operation, System Configuration**: Ensure that the software runs properly under the United States Government Configuration Baseline (USGCB) [REF-199] or an equivalent hardening configuration guide, which many organizations use to limit the attack surface and potential risk of deployed software.
- **Implementation, System Configuration, Operation**: When storing data in the cloud (e.g., S3 buckets, Azure blobs, Google Cloud Storage, etc.), use the provider's controls to disable public access.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-122](https://capec.mitre.org/data/definitions/122.html)
- [CAPEC-127](https://capec.mitre.org/data/definitions/127.html)
- [CAPEC-17](https://capec.mitre.org/data/definitions/17.html)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)
- [CAPEC-206](https://capec.mitre.org/data/definitions/206.html)
- [CAPEC-234](https://capec.mitre.org/data/definitions/234.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
- [CAPEC-61](https://capec.mitre.org/data/definitions/61.html)
- [CAPEC-62](https://capec.mitre.org/data/definitions/62.html)
- [CAPEC-642](https://capec.mitre.org/data/definitions/642.html)

## Related weaknesses
- CWE-285 (ChildOf)
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-29527**: Go application for cloud management creates a world-writable sudoers file that allows local attackers to inject sudo rules and escalate privileges to root by winning a race condition.
- **CVE-2009-3482**: Anti-virus product sets insecure "Everyone: Full Control" permissions for files under the "Program Files" folder, allowing attackers to replace executables with Trojan horses.
- **CVE-2009-3897**: Product creates directories with 0777 permissions at installation, allowing users to gain privileges and access a socket used for authentication.
- **CVE-2009-3489**: Photo editor installs a service with an insecure security descriptor, allowing users to stop or start the service, or execute commands as SYSTEM.
- **CVE-2020-15708**: socket created with insecure permissions
- **CVE-2009-3289**: Library function copies a file to a new target and uses the source file's permissions for the target, which is incorrect when the source file is a symbolic link, which typically has 0777 permissions.
- **CVE-2009-0115**: Device driver uses world-writable permissions for a socket file, allowing attackers to inject arbitrary commands.
- **CVE-2009-1073**: LDAP server stores a cleartext password in a world-readable file.
- **CVE-2009-0141**: Terminal emulator creates TTY devices with world-writable permissions, allowing an attacker to write to the terminals of other users.
- **CVE-2008-0662**: VPN product stores user credentials in a registry key with "Everyone: Full Control" permissions, allowing attackers to steal the credentials.
- **CVE-2008-0322**: Driver installs its device interface with "Everyone: Write" permissions.
- **CVE-2009-3939**: Driver installs a file with world-writable permissions.
- **CVE-2009-3611**: Product changes permissions to 0777 before deleting a backup; the permissions stay insecure for subsequent backups.
- **CVE-2007-6033**: Product creates a share with "Everyone: Full Control" permissions, allowing arbitrary program execution.
- **CVE-2007-5544**: Product uses "Everyone: Full Control" permissions for memory-mapped files (shared memory) in inter-process communication, allowing attackers to tamper with a session.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/732.html
