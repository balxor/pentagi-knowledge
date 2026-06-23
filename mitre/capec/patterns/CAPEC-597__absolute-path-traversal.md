---
capec_id: CAPEC-597
name: Absolute Path Traversal
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-36]
related_attack: []
url: https://capec.mitre.org/data/definitions/597.html
tags: [mitre-capec, attack-pattern, CAPEC-597]
---

# CAPEC-597 - Absolute Path Traversal

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-597](https://capec.mitre.org/data/definitions/597.html)

## Description
An adversary with access to file system resources, either directly or via application logic, will use various file absolute paths and navigation mechanisms such as ".." to extend their range of access to inappropriate areas of the file system. The goal of the adversary is to access directories and files that are intended to be restricted from their access.

## Prerequisites
- The target must leverage and access an underlying file system.

## Skills required
- **Low**: Simple command line attacks.
- **Medium**: Programming attacks.

## Resources required
- The attacker must have access to an application interface or a direct shell that allows them to inject directory strings and monitor the results.

## Consequences
- **Availability**: Execute Unauthorized Commands (The attacker may be able to create or overwrite critical files that are used to execute code, such as programs or libraries.), Unreliable Execution (The attacker may be able to overwrite, delete, or corrupt unexpected critical files such as programs, libraries, or important data. This may prevent the software from working at all and in the case of a protection mechanisms such as authentication, it has the potential to lockout every user of the software.)
- **Confidentiality**: Execute Unauthorized Commands (The attacker may be able to create or overwrite critical files that are used to execute code, such as programs or libraries.), Read Data (The attacker may be able read the contents of unexpected files and expose sensitive data. If the targeted file is used for a security mechanism, then the attacker may be able to bypass that mechanism. For example, by reading a password file, the attacker could conduct brute force password guessing attacks in order to break into an account on the system.)
- **Integrity**: Execute Unauthorized Commands (The attacker may be able to create or overwrite critical files that are used to execute code, such as programs or libraries.), Modify Data (The attacker may be able to overwrite or create critical files, such as programs, libraries, or important data. If the targeted file is used for a security mechanism, then the attacker may be able to bypass that mechanism. For example, appending a new account at the end of a password file may allow an attacker to bypass authentication.)

## Execution flow
Execution Flow Explore Fingerprinting of the operating system: In order to perform a valid path traversal, the adversary needs to know what the underlying OS is so that the proper file seperator is used. Techniques Port mapping. Identify ports that the system is listening on, and attempt to identify inputs and protocol types on those ports. TCP/IP Fingerprinting. The adversary uses various software to make connections or partial connections and observe idiosyncratic responses from the operating system. Using those responses, they attempt to guess the actual operating system. Induce errors to find informative error messages Survey application: Using manual or automated means, an adversary will survey the target application looking for all areas where user input is taken to specify a file name or path. Techniques Use a spidering tool to follow and record all links on a web page. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of a web application. Make special note of any links that include parameters in the URL. Manual traversal of this type is frequently necessary to identify forms that are GET method forms rather than POST forms. Use a browser to manually explore a website and analyze how it is constructed. Many browser's plug-in are available to facilitate the analysis or automate the URL discovery. Experiment Attempt variations on input parameters: Using manual or automated means, an adversary attempts varying absolute file paths on all found user input locations and observes the responses. Techniques Access common files in root directories such as "/bin", "/boot", "/lib", or "/home" Access a specific drive letter or windows volume letter by specifying "C:dirname" for example Access a known Windows UNC share by specifying "\\UNC\share\name" for example Exploit Access, modify, or execute arbitrary files.: An adversary injects absolute path traversal syntax into identified vulnerable inputs to cause inappropriate reading, writing or execution of files. An adversary could be able to read directories or files which they are normally not allowed to read. The adversary could also access data outside the web document root, or include scripts, source code and other kinds of files from external websites. Once the adversary accesses arbitrary files, they could also modify files. In particular situations, the adversary could also execute arbitrary code or system commands. Techniques Manipulate file and its path by injecting absolute path sequences (e.g. "/home/file.txt"). Download files, modify files, or try to execute shell commands (with binary files).

## Mitigations
- Design: Configure the access control correctly.
- Design: Enforce principle of least privilege.
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.
- Implementation: Perform input validation for all remote content, including remote and user-generated content.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- Implementation: Use indirect references rather than actual file names.
- Implementation: Use possible permissions on file access when developing and deploying web applications.
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification using an allowlist approach.

## Related weaknesses (CWE)
- [CWE-36](https://cwe.mitre.org/data/definitions/36.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/597.html
