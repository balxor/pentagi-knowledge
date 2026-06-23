---
cwe_id: CWE-172
name: Encoding Error
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-120, CAPEC-267, CAPEC-3, CAPEC-52, CAPEC-53, CAPEC-64, CAPEC-71, CAPEC-72, CAPEC-78, CAPEC-80]
url: https://cwe.mitre.org/data/definitions/172.html
tags: [mitre-cwe, weakness, CWE-172]
---

# CWE-172 - Encoding Error

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-172](https://cwe.mitre.org/data/definitions/172.html)

## Description
The product does not properly encode or decode the data, resulting in unexpected values.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: While it is risky to use dynamically-generated query strings, code, or commands that mix control and data together, sometimes it may be unavoidable. Properly quote arguments and escape any special characters within those arguments. The most conservative approach is to escape or filter all characters that do not pass an extremely strict allowlist (such as everything that is not alphanumeric or white space). If some special characters are still needed, such as white space, wrap each argument in quotes after the escaping/filtering step. Be careful of argument injection (CWE-88).
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-52](https://capec.mitre.org/data/definitions/52.html)
- [CAPEC-53](https://capec.mitre.org/data/definitions/53.html)
- [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
- [CAPEC-72](https://capec.mitre.org/data/definitions/72.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)

## Related weaknesses
- CWE-707 (ChildOf)
- CWE-22 (CanPrecede)
- CWE-41 (CanPrecede)

## Observed examples (CVE)
- **CVE-2004-1315**: Forum software improperly URL decodes the highlight parameter when extracting text to highlight, which allows remote attackers to execute arbitrary PHP code by double-encoding the highlight value so that special characters are inserted into the result.
- **CVE-2004-1939**: XSS protection mechanism attempts to remove "/" that could be used to close tags, but it can be bypassed using double encoded slashes (%252F)
- **CVE-2001-0709**: Server allows a remote attacker to obtain source code of ASP files via a URL encoded with Unicode.
- **CVE-2005-2256**: Hex-encoded path traversal variants - "%2e%2e", "%2e%2e%2f", "%5c%2e%2e"

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/172.html
