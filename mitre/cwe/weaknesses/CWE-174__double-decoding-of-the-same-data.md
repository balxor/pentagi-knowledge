---
cwe_id: CWE-174
name: Double Decoding of the Same Data
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/174.html
tags: [mitre-cwe, weakness, CWE-174]
---

# CWE-174 - Double Decoding of the Same Data

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-174](https://cwe.mitre.org/data/definitions/174.html)

## Description
The product decodes the same input twice, which can limit the effectiveness of any protection mechanism that occurs in between the decoding operations.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Confidentiality, Availability, Integrity, Other**: Bypass Protection Mechanism, Execute Unauthorized Code or Commands, Varies by Context

## Potential mitigations
- **Architecture and Design**: Avoid making decisions based on names of resources (e.g. files) if those resources can have alternate names.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Use and specify an output encoding that can be handled by the downstream component that is reading the output. Common encodings include ISO-8859-1, UTF-7, and UTF-8. When an encoding is not specified, a downstream component may choose a different encoding, either by assuming a default encoding or automatically inferring which encoding is being used, which can be erroneous. When the encodings are inconsistent, the downstream component might treat some character or byte sequences as special, even if they are not special in the original encoding. Attackers might then be able to exploit this discrepancy and conduct injection attacks; they even might be able to bypass protection mechanisms that assume the original encoding is also being used by the downstream component.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-172 (ChildOf)
- CWE-675 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-1315**: Forum software improperly URL decodes the highlight parameter when extracting text to highlight, which allows remote attackers to execute arbitrary PHP code by double-encoding the highlight value so that special characters are inserted into the result.
- **CVE-2004-1939**: XSS protection mechanism attempts to remove "/" that could be used to close tags, but it can be bypassed using double encoded slashes (%252F)
- **CVE-2001-0333**: Directory traversal using double encoding.
- **CVE-2004-1938**: "%2527" (double-encoded single quote) used in SQL injection.
- **CVE-2005-1945**: Double hex-encoded data.
- **CVE-2005-0054**: Browser executes HTML at higher privileges via URL with hostnames that are double hex encoded, which are decoded twice to generate a malicious hostname.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/174.html
