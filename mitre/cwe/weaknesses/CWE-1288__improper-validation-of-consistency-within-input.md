---
cwe_id: CWE-1288
name: Improper Validation of Consistency within Input
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1288.html
tags: [mitre-cwe, weakness, CWE-1288]
---

# CWE-1288 - Improper Validation of Consistency within Input

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1288](https://cwe.mitre.org/data/definitions/1288.html)

## Description
The product receives a complex input with multiple elements or fields that must be consistent with each other, but it does not validate or incorrectly validates that the input is actually consistent.

## Extended description
Some input data can be structured with multiple elements or fields that must be consistent with each other, e.g. a number-of-items field that is followed by the expected number of elements. When such complex inputs are inconsistent, attackers could trigger unexpected errors, cause incorrect actions to take place, or exploit latent vulnerabilities.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

## Related weaknesses
- CWE-20 (ChildOf)

## Observed examples (CVE)
- **CVE-2018-16733**: product does not validate that the start block appears before the end block
- **CVE-2006-3790**: size field that is inconsistent with packet size leads to buffer over-read
- **CVE-2008-4114**: system crash with offset value that is inconsistent with packet size

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1288.html
