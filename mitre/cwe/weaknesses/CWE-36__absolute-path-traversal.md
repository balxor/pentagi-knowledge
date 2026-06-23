---
cwe_id: CWE-36
name: Absolute Path Traversal
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based, AI/ML]
related_capec: [CAPEC-597]
url: https://cwe.mitre.org/data/definitions/36.html
tags: [mitre-cwe, weakness, CWE-36]
---

# CWE-36 - Absolute Path Traversal

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-36](https://cwe.mitre.org/data/definitions/36.html)

## Description
The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize absolute path sequences such as "/abs/path" that can resolve to a location that is outside of that directory.

## Extended description
This allows attackers to traverse the file system to access files or directories that are outside of the restricted directory.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, AI/ML

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands
- **Integrity**: Modify Files or Directories
- **Confidentiality**: Read Files or Directories
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When validating filenames, use stringent allowlists that limit the character set to be used. If feasible, only allow a single "." character in the filename to avoid weaknesses such as CWE-23, and exclude directory separators such as "/" to avoid CWE-36. Use a list of allowable file extensions, which will help to avoid CWE-434. Do not rely exclusively on a filtering mechanism that removes potentially dangerous characters. This is equivalent to a denylist, which may be incomplete (CWE-184). For example, filtering "/" is insufficient protection if the filesystem also supports the use of "\" as a directory separator. Another possible error could occur when the filtering is applied in a way that still produces dangerous data (CWE-182). For example, if "../" sequences are removed from the ".../...//" string in a sequential fashion, two instances of "../" would be removed from the original string, but the remaining characters would still form the "../" string.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.
- **Operation**: Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].

## Related attack patterns (CAPEC)
- [CAPEC-597](https://capec.mitre.org/data/definitions/597.html)

## Related weaknesses
- CWE-22 (ChildOf)
- CWE-22 (ChildOf)
- CWE-22 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-0520**: Product for managing datasets for AI model training and evaluation allows both relative (CWE-23) and absolute (CWE-36) path traversal to overwrite files via the Content-Disposition header
- **CVE-2022-31503**: Python package constructs filenames using an unsafe os.path.join call on untrusted input, allowing absolute path traversal because os.path.join resets the pathname to an absolute path that is specified as part of the input.
- **CVE-2002-1345**: Multiple FTP clients write arbitrary files via absolute paths in server responses
- **CVE-2001-1269**: ZIP file extractor allows full path
- **CVE-2002-1818**: Path traversal using absolute pathname
- **CVE-2002-1913**: Path traversal using absolute pathname
- **CVE-2005-2147**: Path traversal using absolute pathname
- **CVE-2000-0614**: Arbitrary files may be overwritten via compressed attachments that specify absolute path names for the decompressed output.
- **CVE-1999-1263**: Mail client allows remote attackers to overwrite arbitrary files via an e-mail message containing a uuencoded attachment that specifies the full pathname for the file to be modified.
- **CVE-2003-0753**: Remote attackers can read arbitrary files via a full pathname to the target file in config parameter.
- **CVE-2002-1525**: Remote attackers can read arbitrary files via an absolute pathname.
- **CVE-2001-0038**: Remote attackers can read arbitrary files by specifying the drive letter in the requested URL.
- **CVE-2001-0255**: FTP server allows remote attackers to list arbitrary directories by using the "ls" command and including the drive letter name (e.g. C:) in the requested pathname.
- **CVE-2001-0933**: FTP server allows remote attackers to list the contents of arbitrary drives via a ls command that includes the drive letter as an argument.
- **CVE-2002-0466**: Server allows remote attackers to browse arbitrary directories via a full pathname in the arguments to certain dynamic pages.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/36.html
