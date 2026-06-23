---
capec_id: CAPEC-177
name: Create files with the same name as files protected with a higher classification
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Very High
related_cwe: [CWE-706]
related_attack: [T1036]
url: https://capec.mitre.org/data/definitions/177.html
tags: [mitre-capec, attack-pattern, CAPEC-177]
---

# CAPEC-177 - Create files with the same name as files protected with a higher classification

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-177](https://capec.mitre.org/data/definitions/177.html)

## Description
An attacker exploits file location algorithms in an operating system or application by creating a file with the same name as a protected or privileged file. The attacker could manipulate the system if the attacker-created file is trusted by the operating system or an application component that attempts to load the original file. Applications often load or include external files, such as libraries or configuration files. These files should be protected against malicious manipulation. However, if the application only uses the name of the file when locating it, an attacker may be able to create a file with the same name and place it in a directory that the application will search before the directory with the legitimate file is searched. Because the attackers' file is discovered first, it would be used by the target application. This attack can be extremely destructive if the referenced file is executable and/or is granted special privileges based solely on having a particular name.

## Prerequisites
- The target application must include external files. Most non-trivial applications meet this criterion.
- The target application does not verify that a located file is the one it was looking for through means other than the name. Many applications fail to perform checks of this type.
- The directories the target application searches to find the included file include directories writable by the attacker which are searched before the protected directory containing the actual files. It is much less common for applications to meet this criterion, but if an attacker can manipulate the application's search path (possibly by controlling environmental variables) then they can force this criterion to be met.

## Resources required
- The attacker must have sufficient access to place an arbitrarily named file somewhere early in the application's search path.

## Related weaknesses (CWE)
- [CWE-706](https://cwe.mitre.org/data/definitions/706.html)

## Related ATT&CK techniques
- T1036

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/177.html
