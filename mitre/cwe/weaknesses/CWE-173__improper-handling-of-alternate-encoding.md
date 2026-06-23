---
cwe_id: CWE-173
name: Improper Handling of Alternate Encoding
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-120, CAPEC-267, CAPEC-3, CAPEC-4, CAPEC-52, CAPEC-53, CAPEC-64, CAPEC-71, CAPEC-72, CAPEC-78, CAPEC-79, CAPEC-80]
url: https://cwe.mitre.org/data/definitions/173.html
tags: [mitre-cwe, weakness, CWE-173]
---

# CWE-173 - Improper Handling of Alternate Encoding

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-173](https://cwe.mitre.org/data/definitions/173.html)

## Description
The product does not properly handle when an input uses an alternate encoding that is valid for the control sphere to which the input is being sent.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Avoid making decisions based on names of resources (e.g. files) if those resources can have alternate names.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Use and specify an output encoding that can be handled by the downstream component that is reading the output. Common encodings include ISO-8859-1, UTF-7, and UTF-8. When an encoding is not specified, a downstream component may choose a different encoding, either by assuming a default encoding or automatically inferring which encoding is being used, which can be erroneous. When the encodings are inconsistent, the downstream component might treat some character or byte sequences as special, even if they are not special in the original encoding. Attackers might then be able to exploit this discrepancy and conduct injection attacks; they even might be able to bypass protection mechanisms that assume the original encoding is also being used by the downstream component.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-4](https://capec.mitre.org/data/definitions/4.html)
- [CAPEC-52](https://capec.mitre.org/data/definitions/52.html)
- [CAPEC-53](https://capec.mitre.org/data/definitions/53.html)
- [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
- [CAPEC-72](https://capec.mitre.org/data/definitions/72.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)

## Related weaknesses
- CWE-172 (ChildOf)
- CWE-289 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/173.html
