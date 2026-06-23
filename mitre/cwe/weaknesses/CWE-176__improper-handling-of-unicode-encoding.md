---
cwe_id: CWE-176
name: Improper Handling of Unicode Encoding
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-71]
url: https://cwe.mitre.org/data/definitions/176.html
tags: [mitre-cwe, weakness, CWE-176]
---

# CWE-176 - Improper Handling of Unicode Encoding

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-176](https://cwe.mitre.org/data/definitions/176.html)

## Description
The product does not properly handle when an input contains Unicode encoding.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Architecture and Design**: Avoid making decisions based on names of resources (e.g. files) if those resources can have alternate names.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)

## Related weaknesses
- CWE-172 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-0884**: Server allows remote attackers to read documents outside of the web root, and possibly execute arbitrary commands, via malformed URLs that contain Unicode encoded characters.
- **CVE-2001-0709**: Server allows a remote attacker to obtain source code of ASP files via a URL encoded with Unicode.
- **CVE-2001-0669**: Overlaps interaction error.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/176.html
