---
cwe_id: CWE-1285
name: Improper Validation of Specified Index, Position, or Offset in Input
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1285.html
tags: [mitre-cwe, weakness, CWE-1285]
---

# CWE-1285 - Improper Validation of Specified Index, Position, or Offset in Input

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1285](https://cwe.mitre.org/data/definitions/1285.html)

## Description
The product receives input that is expected to specify an index, position, or offset into an indexable resource such as a buffer or file, but it does not validate or incorrectly validates that the specified index/position/offset has the required properties.

## Extended description
Often, indexable resources such as memory buffers or files can be accessed using a specific position, index, or offset, such as an index for an array or a position for a file. When untrusted input is not properly validated before it is used as an index, attackers could access (or attempt to access) unauthorized portions of these resources. This could be used to cause buffer overflows, excessive resource allocation, or trigger unexpected failures.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

## Related weaknesses
- CWE-20 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-0369**: large ID in packet used as array index
- **CVE-2001-1009**: negative array index as argument to POP LIST command

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1285.html
