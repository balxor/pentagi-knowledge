---
capec_id: CAPEC-126
name: Path Traversal
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-22]
related_attack: []
url: https://capec.mitre.org/data/definitions/126.html
tags: [mitre-capec, attack-pattern, CAPEC-126]
---

# CAPEC-126 - Path Traversal

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-126](https://capec.mitre.org/data/definitions/126.html)

## Description
An adversary uses path manipulation methods to exploit insufficient input validation of a target to obtain access to data that should be not be retrievable by ordinary well-formed requests. A typical variety of this attack involves specifying a path to a desired file together with dot-dot-slash characters, resulting in the file access API or function traversing out of the intended directory structure and into the root file system. By replacing or modifying the expected path information the access function or API retrieves the file desired by the attacker. These attacks either involve the attacker providing a complete path to a targeted file or using control characters (e.g. path separators (/ or \) and/or dots (.)) to reach desired directories or files.

## Prerequisites
- The attacker must be able to control the path that is requested of the target.
- The target must fail to adequately sanitize incoming paths

## Skills required
- **Low**: Simple command line attacks or to inject the malicious payload in a web page.
- **Medium**: Customizing attacks to bypass non trivial filters in the application.

## Resources required
- The ability to manually manipulate path information either directly through a client application relative to the service or application or via a proxy application.

## Consequences
- **Availability**: Execute Unauthorized Commands (The attacker may be able to create or overwrite critical files that are used to execute code, such as programs or libraries.), Unreliable Execution (The attacker may be able to overwrite, delete, or corrupt unexpected critical files such as programs, libraries, or important data. This may prevent the software from working at all and in the case of a protection mechanisms such as authentication, it has the potential to lockout every user of the software.)
- **Confidentiality**: Execute Unauthorized Commands (The attacker may be able to create or overwrite critical files that are used to execute code, such as programs or libraries.), Read Data (The attacker may be able read the contents of unexpected files and expose sensitive data. If the targeted file is used for a security mechanism, then the attacker may be able to bypass that mechanism. For example, by reading a password file, the attacker could conduct brute force password guessing attacks in order to break into an account on the system.)
- **Integrity**: Execute Unauthorized Commands (The attacker may be able to create or overwrite critical files that are used to execute code, such as programs or libraries.), Modify Data (The attacker may be able to overwrite or create critical files, such as programs, libraries, or important data. If the targeted file is used for a security mechanism, then the attacker may be able to bypass that mechanism. For example, appending a new account at the end of a password file may allow an attacker to bypass authentication.)

## Execution flow
Execution Flow Explore Fingerprinting of the operating system: In order to perform a valid path traversal, the attacker needs to know what the underlying OS is so that the proper file seperator is used. Techniques Port mapping. Identify ports that the system is listening on, and attempt to identify inputs and protocol types on those ports. TCP/IP Fingerprinting. The attacker uses various software to make connections or partial connections and observe idiosyncratic responses from the operating system. Using those responses, they attempt to guess the actual operating system. Induce errors to find informative error messages Survey the Application to Identify User-controllable Inputs: The attacker surveys the target application to identify all user-controllable file inputs Experiment Vary inputs, looking for malicious results: Depending on whether the application being exploited is a remote or local one, the attacker crafts the appropriate malicious input containing the path of the targeted file or other file system control syntax to be passed to the application Exploit Manipulate files accessible by the application: The attacker may steal information or directly manipulate files (delete, copy, flush, etc.)

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
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- using an allowlist approach.

## Related weaknesses (CWE)
- [CWE-22](https://cwe.mitre.org/data/definitions/22.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/126.html
