---
cwe_id: CWE-427
name: Uncontrolled Search Path Element
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Technology-Specific]
related_capec: [CAPEC-38, CAPEC-471]
url: https://cwe.mitre.org/data/definitions/427.html
tags: [mitre-cwe, weakness, CWE-427]
---

# CWE-427 - Uncontrolled Search Path Element

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-427](https://cwe.mitre.org/data/definitions/427.html)

## Description
The product uses a fixed or controlled search path to find resources, but one or more locations in that path can be under the control of unintended actors.

## Extended description
Although this weakness can occur with any type of resource, it is frequently introduced when a product uses a directory search path to find executables or code libraries, but the path contains a directory that can be modified by an attacker, such as "/tmp" or the current working directory. In Windows-based systems, when the LoadLibrary or LoadLibraryEx function is called with a DLL name that does not contain a fully qualified path, the function follows a search order that includes two path elements that might be uncontrolled: the directory from which the program has been loaded the current working directory In some cases, the attack can be conducted remotely, such as when SMB or WebDAV network shares are used. One or more locations in that path could include the Windows drive root or its subdirectories. This often exists in Linux-based code assuming the controlled nature of the root directory (/) or its subdirectories (/etc, etc), or a code that recursively accesses the parent directory. In Windows, the drive root and some of its subdirectories have weak permissions by default, which makes them uncontrolled. In some Unix-based systems, a PATH might be created that contains an empty element, e.g. by splicing an empty variable into the PATH. This empty element can be interpreted as equivalent to the current working directory, which might be an untrusted search element. In software package management frameworks (e.g., npm, RubyGems, or PyPi), the framework may identify dependencies on third-party libraries or other packages, then consult a repository that contains the desired package. The framework may search a public repository before a private repository. This could be exploited by attackers by placing a malicious package in the public repository that has the same name as a package from the private repository. The search path might not be directly under control of the developer relying on the framework, but this search order effectively contains an untrusted element.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design, Implementation**: Hard-code the search path to a set of known-safe values (such as system directories), or only allow them to be specified by the administrator in a configuration file. Do not allow these settings to be modified by an external party. Be careful to avoid related weaknesses such as CWE-426 and CWE-428.
- **Implementation**: When invoking other programs, specify those programs using fully-qualified pathnames. While this is an effective approach, code that uses fully-qualified pathnames might not be portable to other systems that do not use the same pathnames. The portability can be improved by locating the full-qualified paths in a centralized, easily-modifiable location within the source code, and having the code refer to these paths.
- **Implementation**: Remove or restrict all environment settings before invoking other programs. This includes the PATH environment variable, LD_LIBRARY_PATH, and other settings that identify the location of code libraries, and any application-specific search paths.
- **Implementation**: Check your search path before use and remove any elements that are likely to be unsafe, such as the current working directory or a temporary files directory. Since this is a denylist approach, it might not be a complete solution.
- **Implementation**: Use other functions that require explicit paths. Making use of any of the other readily available functions that require explicit paths is a safe way to avoid this problem. For example, system() in C does not require a full path since the shell can take care of finding the program using the PATH environment variable, while execl() and execv() require a full path.

## Related attack patterns (CAPEC)
- [CAPEC-38](https://capec.mitre.org/data/definitions/38.html)
- [CAPEC-471](https://capec.mitre.org/data/definitions/471.html)

## Related weaknesses
- CWE-668 (ChildOf)
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-25815**: chain: a change in an underlying package causes the gettext function to use implicit initialization with a hard-coded path (CWE-1419) under the user-writable C:\ drive, introducing an untrusted search path element (CWE-427) that enables spoofing of messages.
- **CVE-2022-4826**: Go-based git extension on Windows can search for and execute a malicious "..exe" in a repository because Go searches the current working directory if git.exe is not found in the PATH
- **CVE-2020-26284**: A Static Site Generator built in Go, when running on Windows, searches the current working directory for a command, possibly allowing code execution using a malicious .exe or .bat file with the name being searched
- **CVE-2022-24765**: Windows-based fork of git creates a ".git" folder in the C: drive, allowing local attackers to create a .git folder with a malicious config file
- **CVE-2019-1552**: SSL package searches under "C:/usr/local" for configuration files and other critical data, but C:/usr/local might be world-writable.
- **CVE-2010-3402**: "DLL hijacking" issue in document editor.
- **CVE-2010-3397**: "DLL hijacking" issue in encryption software.
- **CVE-2010-3138**: "DLL hijacking" issue in library used by multiple media players.
- **CVE-2010-3152**: "DLL hijacking" issue in illustration program.
- **CVE-2010-3147**: "DLL hijacking" issue in address book.
- **CVE-2010-3135**: "DLL hijacking" issue in network monitoring software.
- **CVE-2010-3131**: "DLL hijacking" issue in web browser.
- **CVE-2010-1795**: "DLL hijacking" issue in music player/organizer.
- **CVE-2002-1576**: Product uses the current working directory to find and execute a program, which allows local users to gain privileges by creating a symlink that points to a malicious version of the program.
- **CVE-1999-1461**: Product trusts the PATH environmental variable to find and execute a program, which allows local users to obtain root access by modifying the PATH to point to a malicous version of that program.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/427.html
