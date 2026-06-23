---
cwe_id: CWE-37
name: Path Traversal: '/absolute/pathname/here'
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/37.html
tags: [mitre-cwe, weakness, CWE-37]
---

# CWE-37 - Path Traversal: '/absolute/pathname/here'

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-37](https://cwe.mitre.org/data/definitions/37.html)

## Description
The product accepts input in the form of a slash absolute path ('/absolute/pathname/here') without appropriate validation, which can allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When validating filenames, use stringent allowlists that limit the character set to be used. If feasible, only allow a single "." character in the filename to avoid weaknesses such as CWE-23, and exclude directory separators such as "/" to avoid CWE-36. Use a list of allowable file extensions, which will help to avoid CWE-434. Do not rely exclusively on a filtering mechanism that removes potentially dangerous characters. This is equivalent to a denylist, which may be incomplete (CWE-184). For example, filtering "/" is insufficient protection if the filesystem also supports the use of "\" as a directory separator. Another possible error could occur when the filtering is applied in a way that still produces dangerous data (CWE-182). For example, if "../" sequences are removed from the ".../...//" string in a sequential fashion, two instances of "../" would be removed from the original string, but the remaining characters would still form the "../" string.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-36 (ChildOf)
- CWE-160 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1345**: Multiple FTP clients write arbitrary files via absolute paths in server responses
- **CVE-2001-1269**: ZIP file extractor allows full path
- **CVE-2002-1818**: Path traversal using absolute pathname
- **CVE-2002-1913**: Path traversal using absolute pathname
- **CVE-2005-2147**: Path traversal using absolute pathname
- **CVE-2000-0614**: Arbitrary files may be overwritten via compressed attachments that specify absolute path names for the decompressed output.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/37.html
