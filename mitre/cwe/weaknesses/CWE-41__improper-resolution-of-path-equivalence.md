---
cwe_id: CWE-41
name: Improper Resolution of Path Equivalence
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-3]
url: https://cwe.mitre.org/data/definitions/41.html
tags: [mitre-cwe, weakness, CWE-41]
---

# CWE-41 - Improper Resolution of Path Equivalence

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-41](https://cwe.mitre.org/data/definitions/41.html)

## Description
The product is vulnerable to file system contents disclosure through path equivalence. Path equivalence involves the use of special characters in file and directory names. The associated manipulations are intended to generate multiple names for the same object.

## Extended description
Path equivalence is usually employed in order to circumvent access controls expressed using an incomplete set of file name or file path representations. This is different from path traversal, wherein the manipulations are performed to generate a name for a different object.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control**: Read Files or Directories, Modify Files or Directories, Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Use and specify an output encoding that can be handled by the downstream component that is reading the output. Common encodings include ISO-8859-1, UTF-7, and UTF-8. When an encoding is not specified, a downstream component may choose a different encoding, either by assuming a default encoding or automatically inferring which encoding is being used, which can be erroneous. When the encodings are inconsistent, the downstream component might treat some character or byte sequences as special, even if they are not special in the original encoding. Attackers might then be able to exploit this discrepancy and conduct injection attacks; they even might be able to bypass protection mechanisms that assume the original encoding is also being used by the downstream component.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)

## Related weaknesses
- CWE-706 (ChildOf)
- CWE-863 (ChildOf)
- CWE-1390 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-1114**: Source code disclosure using trailing dot
- **CVE-2002-1986**: Source code disclosure using trailing dot
- **CVE-2004-2213**: Source code disclosure using trailing dot or trailing encoding space "%20"
- **CVE-2005-3293**: Source code disclosure using trailing dot
- **CVE-2004-0061**: Bypass directory access restrictions using trailing dot in URL
- **CVE-2000-1133**: Bypass directory access restrictions using trailing dot in URL
- **CVE-2001-1386**: Bypass check for ".lnk" extension using ".lnk."
- **CVE-2001-0693**: Source disclosure via trailing encoded space "%20"
- **CVE-2001-0778**: Source disclosure via trailing encoded space "%20"
- **CVE-2001-1248**: Source disclosure via trailing encoded space "%20"
- **CVE-2004-0280**: Source disclosure via trailing encoded space "%20"
- **CVE-2005-0622**: Source disclosure via trailing encoded space "%20"
- **CVE-2005-1656**: Source disclosure via trailing encoded space "%20"
- **CVE-2002-1603**: Source disclosure via trailing encoded space "%20"
- **CVE-2001-0054**: Multi-Factor Vulnerability (MFV). directory traversal and other issues in FTP server using Web encodings such as "%20"; certain manipulations have unusual side effects.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/41.html
