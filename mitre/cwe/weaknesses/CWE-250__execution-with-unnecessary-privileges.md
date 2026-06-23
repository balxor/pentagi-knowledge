---
cwe_id: CWE-250
name: Execution with Unnecessary Privileges
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, AI/ML, Mobile]
related_capec: [CAPEC-104, CAPEC-470, CAPEC-69]
url: https://cwe.mitre.org/data/definitions/250.html
tags: [mitre-cwe, weakness, CWE-250]
---

# CWE-250 - Execution with Unnecessary Privileges

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-250](https://cwe.mitre.org/data/definitions/250.html)

## Description
The product performs an operation at a privilege level that is higher than the minimum level required, which creates new weaknesses or amplifies the consequences of other weaknesses.

## Applicable platforms / languages
Not Language-Specific, AI/ML, Mobile

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands, Read Application Data, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.
- **Architecture and Design**: Identify the functionality that requires additional privileges, such as access to privileged operating system resources. Wrap and centralize this functionality if possible, and isolate the privileged code as much as possible from other code [REF-76]. Raise privileges as late as possible, and drop them as soon as possible to avoid CWE-271. Avoid weaknesses such as CWE-288 and CWE-420 by protecting all possible communication channels that could interact with the privileged code, such as a secondary socket that is only intended to be accessed by administrators.
- **Architecture and Design**: Identify the functionality that requires additional privileges, such as access to privileged operating system resources. Wrap and centralize this functionality if possible, and isolate the privileged code as much as possible from other code [REF-76]. Raise privileges as late as possible, and drop them as soon as possible to avoid CWE-271. Avoid weaknesses such as CWE-288 and CWE-420 by protecting all possible communication channels that could interact with the privileged code, such as a secondary socket that is only intended to be accessed by administrators.
- **Implementation**: Perform extensive input validation for any privileged code that must be exposed to the user and reject anything that does not fit your strict requirements.
- **Implementation**: When dropping privileges, ensure that they have been dropped successfully to avoid CWE-273. As protection mechanisms in the environment get stronger, privilege-dropping calls may fail even if it seems like they would always succeed.
- **Implementation**: If circumstances force you to run with extra privileges, then determine the minimum access level necessary. First identify the different permissions that the software and its users will need to perform their actions, such as file read and write permissions, network socket permissions, and so forth. Then explicitly allow those actions while denying all else [REF-76]. Perform extensive input validation and canonicalization to minimize the chances of introducing a separate vulnerability. This mitigation is much more prone to error than dropping the privileges in the first place.
- **Operation, System Configuration**: Ensure that the software runs properly under the United States Government Configuration Baseline (USGCB) [REF-199] or an equivalent hardening configuration guide, which many organizations use to limit the attack surface and potential risk of deployed software.

## Related attack patterns (CAPEC)
- [CAPEC-104](https://capec.mitre.org/data/definitions/104.html)
- [CAPEC-470](https://capec.mitre.org/data/definitions/470.html)
- [CAPEC-69](https://capec.mitre.org/data/definitions/69.html)

## Related weaknesses
- CWE-269 (ChildOf)
- CWE-657 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-4217**: FTP client program on a certain OS runs with setuid privileges and has a buffer overflow. Most clients do not need extra privileges, so an overflow is not a vulnerability for those clients.
- **CVE-2008-1877**: Program runs with privileges and calls another program with the same privileges, which allows read of arbitrary files.
- **CVE-2007-5159**: OS incorrectly installs a program with setuid privileges, allowing users to gain privileges.
- **CVE-2008-4638**: Composite: application running with high privileges (CWE-250) allows user to specify a restricted file to process, which generates a parsing error that leaks the contents of the file (CWE-209).
- **CVE-2008-0162**: Program does not drop privileges before calling another program, allowing code execution.
- **CVE-2008-0368**: setuid root program allows creation of arbitrary files through command line argument.
- **CVE-2007-3931**: Installation script installs some programs as setuid when they shouldn't be.
- **CVE-2020-3812**: mail program runs as root but does not drop its privileges before attempting to access a file. Attacker can use a symlink from their home directory to a directory only readable by root, then determine whether the file exists based on the response.
- **CVE-2003-0908**: Product launches Help functionality while running with raised privileges, allowing command execution using Windows message to access "open file" dialog.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/250.html
