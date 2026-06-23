---
cwe_id: CWE-428
name: Unquoted Search Path or Element
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Windows NT, macOS]
related_capec: []
url: https://cwe.mitre.org/data/definitions/428.html
tags: [mitre-cwe, weakness, CWE-428]
---

# CWE-428 - Unquoted Search Path or Element

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-428](https://cwe.mitre.org/data/definitions/428.html)

## Description
The product uses a search path that contains an unquoted element, in which the element contains whitespace or other separators. This can cause the product to access resources in a parent path.

## Extended description
If a malicious individual has access to the file system, it is possible to elevate privileges by inserting such a file as "C:\Program.exe" to be run by a privileged program making use of WinExec.

## Applicable platforms / languages
Not Language-Specific, Windows NT, macOS

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: Properly quote the full search path before executing a program on the system.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-668 (ChildOf)
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1185**: Small handful of others. Program doesn't quote the "C:\Program Files\" path when calling a program to be executed - or any other path with a directory or file whose name contains a space - so attacker can put a malicious program.exe into C:.
- **CVE-2005-2938**: CreateProcess() and CreateProcessAsUser() can be misused by applications to allow "program.exe" style attacks in C:
- **CVE-2000-1128**: Applies to "Common Files" folder, with a malicious common.exe, instead of "Program Files"/program.exe.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/428.html
