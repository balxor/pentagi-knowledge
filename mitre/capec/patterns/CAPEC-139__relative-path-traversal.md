---
capec_id: CAPEC-139
name: Relative Path Traversal
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-23]
related_attack: []
url: https://capec.mitre.org/data/definitions/139.html
tags: [mitre-capec, attack-pattern, CAPEC-139]
---

# CAPEC-139 - Relative Path Traversal

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-139](https://capec.mitre.org/data/definitions/139.html)

## Description
An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach material that is not available through intended channels. These attacks normally involve adding additional path separators (/ or \) and/or dots (.), or encodings thereof, in various combinations in order to reach parent directories or entirely separate trees of the target's directory structure.

## Prerequisites
- The target application must accept a string as user input, fail to sanitize combinations of characters in the input that have a special meaning in the context of path navigation, and insert the user-supplied string into path navigation commands.

## Skills required
- **High**: To bypass non trivial filters in the application
- **Low**: To inject the malicious payload in a web page

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Fingerprinting of the operating system: In order to perform a valid path traversal, the adversary needs to know what the underlying OS is so that the proper file seperator is used. Techniques Port mapping. Identify ports that the system is listening on, and attempt to identify inputs and protocol types on those ports. TCP/IP Fingerprinting. The adversary uses various software to make connections or partial connections and observe idiosyncratic responses from the operating system. Using those responses, they attempt to guess the actual operating system. Induce errors to find informative error messages Survey application: Using manual or automated means, an adversary will survey the target application looking for all areas where user input is taken to specify a file name or path. Techniques Use a spidering tool to follow and record all links on a web page. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of a web application. Make special note of any links that include parameters in the URL. Manual traversal of this type is frequently necessary to identify forms that are GET method forms rather than POST forms. Use a browser to manually explore a website and analyze how it is constructed. Many browser plug-ins are available to facilitate the analysis or automate the URL discovery. Experiment Attempt variations on input parameters: Using manual or automated means, an adversary attempts varying relative file path combinations on all found user input locations and observes the responses. Techniques Provide "../" or "..\" at the beginning of any filename to traverse to the parent directory Use a list of probe strings as path traversal payload. Different strings may be used for different platforms. Strings contain relative path sequences such as "../". Use a proxy tool to record results of manual input of relative path traversal probes in known URLs. Exploit Access, modify, or execute arbitrary files.: An adversary injects path traversal syntax into identified vulnerable inputs to cause inappropriate reading, writing or execution of files. An adversary could be able to read directories or files which they are normally not allowed to read. The adversary could also access data outside the web document root, or include scripts, source code and other kinds of files from external websites. Once the adversary accesses arbitrary files, they could also modify files. In particular situations, the adversary could also execute arbitrary code or system commands. Techniques Manipulate file and its path by injecting relative path sequences (e.g. "../"). Download files, modify files, or try to execute shell commands (with binary files).

## Mitigations
- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement
- Implementation: Perform input validation for all remote content, including remote and user-generated content.
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- using an allowlist approach.
- Implementation: Prefer working without user input when using file system calls
- Implementation: Use indirect references rather than actual file names.
- Implementation: Use possible permissions on file access when developing and deploying web applications.

## Related weaknesses (CWE)
- [CWE-23](https://cwe.mitre.org/data/definitions/23.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/139.html
