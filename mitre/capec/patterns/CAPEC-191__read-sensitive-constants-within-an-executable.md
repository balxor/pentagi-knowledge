---
capec_id: CAPEC-191
name: Read Sensitive Constants Within an Executable
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-798]
related_attack: [T1552.001]
url: https://capec.mitre.org/data/definitions/191.html
tags: [mitre-capec, attack-pattern, CAPEC-191]
---

# CAPEC-191 - Read Sensitive Constants Within an Executable

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-191](https://capec.mitre.org/data/definitions/191.html)

## Description
<xhtml:p>An adversary engages in activities to discover any sensitive constants present within the compiled code of an executable. These constants may include literal ASCII strings within the file itself, or possibly strings hard-coded into particular routines that can be revealed by code refactoring methods including static and dynamic analysis.</xhtml:p>

## Extended description
One specific example of a sensitive string is a hard-coded password. Typical examples of software with hard-coded passwords include server-side executables which may check for a hard-coded password or key during a user's authentication with the server. Hard-coded passwords can also be present in client-side executables which utilize the password or key when connecting to either a remote component, such as a database server, licensing server, or otherwise, or a processes on the same host that expects a key or password. When analyzing an executable the adversary may search for the presence of such strings by analyzing the byte-code of the file itself. Example utilities for revealing strings within a file include 'strings,' 'grep,' or other variants of these programs depending upon the type of operating system used. These programs can be used to dump any ASCII or UNICODE strings contained within a program. Strings can also be searched for using a hex editors by loading the binary or object code file and utilizing native search functions such as regular expressions. Additionally, sensitive numeric values can occur within an executable. This can be used to discover the location of cryptographic constants.

## Prerequisites
- Access to a binary or executable such that it can be analyzed by various utilities.

## Resources required
- Binary analysis programs such as 'strings' or 'grep', or hex editors.

## Related weaknesses (CWE)
- [CWE-798](https://cwe.mitre.org/data/definitions/798.html)

## Related ATT&CK techniques
- T1552.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/191.html
