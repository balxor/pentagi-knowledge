---
cwe_id: CWE-665
name: Improper Initialization
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-26, CAPEC-29]
url: https://cwe.mitre.org/data/definitions/665.html
tags: [mitre-cwe, weakness, CWE-665]
---

# CWE-665 - Improper Initialization

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-665](https://cwe.mitre.org/data/definitions/665.html)

## Description
The product does not initialize or incorrectly initializes a resource, which might leave the resource in an unexpected state when it is accessed or used.

## Extended description
This can have security implications when the associated resource is expected to have certain properties or values, such as a variable that determines whether a user has been authenticated or not.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data
- **Access Control**: Bypass Protection Mechanism
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Requirements**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, in Java, if the programmer does not explicitly initialize a variable, then the code could produce a compile-time error (if the variable is local) or automatically initialize the variable to the default value for the variable's type. In Perl, if explicit initialization is not performed, then a default value of undef is assigned, which is interpreted as 0, false, or an equivalent value depending on the context in which the variable is accessed.
- **Architecture and Design**: Identify all variables and data stores that receive information from external sources, and apply input validation to make sure that they are only initialized to expected values.
- **Implementation**: Explicitly initialize all your variables and other data stores, either during declaration or just before the first usage.
- **Implementation**: Pay close attention to complex conditionals that affect initialization, since some conditions might not perform the initialization.
- **Implementation**: Avoid race conditions (CWE-362) during initialization routines.
- **Build and Compilation**: Run or compile your product with settings that generate warnings about uninitialized variables or data.

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-1471**: chain: an invalid value prevents a library file from being included, skipping initialization of key variables, leading to resultant eval injection.
- **CVE-2008-3637**: Improper error checking in protection mechanism produces an uninitialized variable, allowing security bypass and code execution.
- **CVE-2008-4197**: Use of uninitialized memory may allow code execution.
- **CVE-2008-2934**: Free of an uninitialized pointer leads to crash and possible code execution.
- **CVE-2007-3749**: OS kernel does not reset a port when starting a setuid program, allowing local users to access the port and gain privileges.
- **CVE-2008-0063**: Product does not clear memory contents when generating an error message, leading to information leak.
- **CVE-2008-0062**: Lack of initialization triggers NULL pointer dereference or double-free.
- **CVE-2008-0081**: Uninitialized variable leads to code execution in popular desktop application.
- **CVE-2008-3688**: chain: Uninitialized variable leads to infinite loop.
- **CVE-2008-3475**: chain: Improper initialization leads to memory corruption.
- **CVE-2008-5021**: Composite: race condition allows attacker to modify an object while it is still being initialized, causing software to access uninitialized memory.
- **CVE-2005-1036**: Chain: Bypass of access restrictions due to improper authorization (CWE-862) of a user results from an improperly initialized (CWE-909) I/O permission bitmap
- **CVE-2008-3597**: chain: game server can access player data structures before initialization has happened leading to NULL dereference
- **CVE-2009-2692**: Chain: Use of an unimplemented network socket operation pointing to an uninitialized handler function (CWE-456) causes a crash because of a null pointer dereference (CWE-476)
- **CVE-2009-0949**: chain: improper initialization of memory can lead to NULL dereference

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/665.html
