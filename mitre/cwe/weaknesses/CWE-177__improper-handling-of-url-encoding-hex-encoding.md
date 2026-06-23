---
cwe_id: CWE-177
name: Improper Handling of URL Encoding (Hex Encoding)
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-120, CAPEC-468, CAPEC-64, CAPEC-72]
url: https://cwe.mitre.org/data/definitions/177.html
tags: [mitre-cwe, weakness, CWE-177]
---

# CWE-177 - Improper Handling of URL Encoding (Hex Encoding)

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-177](https://cwe.mitre.org/data/definitions/177.html)

## Description
The product does not properly handle when all or part of an input has been URL encoded.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Architecture and Design**: Avoid making decisions based on names of resources (e.g. files) if those resources can have alternate names.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-468](https://capec.mitre.org/data/definitions/468.html)
- [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
- [CAPEC-72](https://capec.mitre.org/data/definitions/72.html)

## Related weaknesses
- CWE-172 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-0900**: Hex-encoded path traversal variants - "%2e%2e", "%2e%2e%2f", "%5c%2e%2e"
- **CVE-2005-2256**: Hex-encoded path traversal variants - "%2e%2e", "%2e%2e%2f", "%5c%2e%2e"
- **CVE-2004-2121**: Hex-encoded path traversal variants - "%2e%2e", "%2e%2e%2f", "%5c%2e%2e"
- **CVE-2004-0280**: "%20" (encoded space)
- **CVE-2003-0424**: "%20" (encoded space)
- **CVE-2001-0693**: "%20" (encoded space)
- **CVE-2001-0778**: "%20" (encoded space)
- **CVE-2002-1831**: Crash via hex-encoded space "%20".
- **CVE-2000-0671**: "%00" (encoded null)
- **CVE-2004-0189**: "%00" (encoded null)
- **CVE-2002-1291**: "%00" (encoded null)
- **CVE-2002-1031**: "%00" (encoded null)
- **CVE-2001-1140**: "%00" (encoded null)
- **CVE-2004-0760**: "%00" (encoded null)
- **CVE-2002-1025**: "%00" (encoded null)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/177.html
