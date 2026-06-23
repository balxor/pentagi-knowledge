---
cwe_id: CWE-73
name: External Control of File Name or Path
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Unix, Windows, macOS]
related_capec: [CAPEC-13, CAPEC-267, CAPEC-64, CAPEC-72, CAPEC-76, CAPEC-78, CAPEC-79, CAPEC-80]
url: https://cwe.mitre.org/data/definitions/73.html
tags: [mitre-cwe, weakness, CWE-73]
---

# CWE-73 - External Control of File Name or Path

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-73](https://cwe.mitre.org/data/definitions/73.html)

## Description
The product allows user input to control or influence paths or file names that are used in filesystem operations.

## Extended description
This could allow an attacker to access or modify system files or other files that are critical to the application. Path manipulation errors occur when the following two conditions are met: 1. An attacker can specify a path used in an operation on the filesystem. 2. By specifying the resource, the attacker gains a capability that would not otherwise be permitted. For example, the program may give the attacker the ability to overwrite the specified file or run with a configuration controlled by the attacker.

## Applicable platforms / languages
Not Language-Specific, Unix, Windows, macOS

## Common consequences
- **Integrity, Confidentiality**: Read Files or Directories, Modify Files or Directories
- **Integrity, Confidentiality, Availability**: Modify Files or Directories, Execute Unauthorized Code or Commands
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design**: When the set of filenames is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames, and reject all other inputs. For example, ID 1 could map to "inbox.txt" and ID 2 could map to "profile.txt". Features such as the ESAPI AccessReferenceMap provide this capability.
- **Architecture and Design, Operation**: Run your code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict all access to files within a particular directory. Examples include the Unix chroot jail and AppArmor. In general, managed code may provide some protection. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of your application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.
- **Architecture and Design**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When validating filenames, use stringent allowlists that limit the character set to be used. If feasible, only allow a single "." character in the filename to avoid weaknesses such as CWE-23, and exclude directory separators such as "/" to avoid CWE-36. Use a list of allowable file extensions, which will help to avoid CWE-434. Do not rely exclusively on a filtering mechanism that removes potentially dangerous characters. This is equivalent to a denylist, which may be incomplete (CWE-184). For example, filtering "/" is insufficient protection if the filesystem also supports the use of "\" as a directory separator. Another possible error could occur when the filtering is applied in a way that still produces dangerous data (CWE-182). For example, if "../" sequences are removed from the ".../...//" string in a sequential fashion, two instances of "../" would be removed from the original string, but the remaining characters would still form the "../" string.
- **Implementation**: Use a built-in path canonicalization function (such as realpath() in C) that produces the canonical version of the pathname, which effectively removes ".." sequences and symbolic links (CWE-23, CWE-59).
- **Installation, Operation**: Use OS-level permissions and run as a low-privileged user to limit the scope of any successful attack.
- **Operation, Implementation**: If you are using PHP, configure your application so that it does not use register_globals. During implementation, develop your application so that it does not rely on this feature, but be wary of implementing a register_globals emulation that is subject to weaknesses such as CWE-95, CWE-621, and similar issues.
- **Testing**: Use tools and techniques that require manual (human) analysis, such as penetration testing, threat modeling, and interactive tools that allow the tester to record and modify an active session. These may be more effective than strictly automated techniques. This is especially the case with weaknesses that are related to design and business rules.

## Related attack patterns (CAPEC)
- [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
- [CAPEC-72](https://capec.mitre.org/data/definitions/72.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)

## Related weaknesses
- CWE-642 (ChildOf)
- CWE-610 (ChildOf)
- CWE-20 (ChildOf)
- CWE-22 (CanPrecede)
- CWE-41 (CanPrecede)
- CWE-98 (CanPrecede)
- CWE-434 (CanPrecede)
- CWE-59 (CanPrecede)

## Observed examples (CVE)
- **CVE-2022-45918**: Chain: a learning management tool debugger uses external input to locate previous session logs (CWE-73) and does not properly validate the given path (CWE-20), allowing for filesystem path traversal using "../" sequences (CWE-24)
- **CVE-2008-5748**: Chain: external control of values for user's desired language and theme enables path traversal.
- **CVE-2008-5764**: Chain: external control of user's target language enables remote file inclusion.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/73.html
