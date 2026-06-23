---
cwe_id: CWE-457
name: Use of Uninitialized Variable
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++, Perl, PHP, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/457.html
tags: [mitre-cwe, weakness, CWE-457]
---

# CWE-457 - Use of Uninitialized Variable

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-457](https://cwe.mitre.org/data/definitions/457.html)

## Description
The code uses a variable that has not been initialized, leading to unpredictable or unintended results.

## Extended description
In some languages such as C and C++, stack variables are not initialized by default. They generally contain junk data with the contents of stack memory before the function was invoked. An attacker can sometimes control or read these contents. In other languages or conditions, a variable that is not explicitly initialized can be given a default value that has security implications, depending on the logic of the program. The presence of an uninitialized variable can sometimes indicate a typographic error in the code.

## Applicable platforms / languages
C, C++, Perl, PHP, Not Language-Specific

## Common consequences
- **Availability, Integrity, Other**: Other
- **Authorization, Other**: Other

## Potential mitigations
- **Implementation**: Ensure that critical variables are initialized before first use [REF-1485].
- **Build and Compilation**: Most compilers will complain about the use of uninitialized variables if warnings are turned on.
- **Implementation, Operation**: When using a language that does not require explicit declaration of variables, run or compile the software in a mode that reports undeclared or unknown variables. This may indicate the presence of a typographic error in the variable's name.
- **Requirements**: Choose a language that is not susceptible to these issues.
- **Architecture and Design**: Mitigating technologies such as safe string libraries and container abstractions could be introduced.

## Related weaknesses
- CWE-908 (ChildOf)
- CWE-665 (ChildOf)
- CWE-665 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-15900**: Chain: sscanf() call is used to check if a username and group exists, but the return value of sscanf() call is not checked (CWE-252), causing an uninitialized variable to be checked (CWE-457), returning success to allow authorization bypass for executing a privileged (CWE-863).
- **CVE-2008-3688**: Chain: A denial of service may be caused by an uninitialized variable (CWE-457) allowing an infinite loop (CWE-835) resulting from a connection to an unresponsive server.
- **CVE-2008-0081**: Uninitialized variable leads to code execution in popular desktop application.
- **CVE-2007-4682**: Crafted input triggers dereference of an uninitialized object pointer.
- **CVE-2007-3468**: Crafted audio file triggers crash when an uninitialized variable is used.
- **CVE-2007-2728**: Uninitialized random seed variable used.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/457.html
