---
cwe_id: CWE-1284
name: Improper Validation of Specified Quantity in Input
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1284.html
tags: [mitre-cwe, weakness, CWE-1284]
---

# CWE-1284 - Improper Validation of Specified Quantity in Input

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1284](https://cwe.mitre.org/data/definitions/1284.html)

## Description
The product receives input that is expected to specify a quantity (such as size or length), but it does not validate or incorrectly validates that the quantity has the required properties.

## Extended description
Specified quantities include size, length, frequency, price, rate, number of operations, time, and others. Code may rely on specified quantities to allocate resources, perform calculations, control iteration, etc.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other, Integrity, Availability**: Varies by Context, DoS: Resource Consumption (CPU), Modify Memory, Read Memory

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

## Related weaknesses
- CWE-20 (ChildOf)
- CWE-20 (ChildOf)
- CWE-789 (CanPrecede)

## Observed examples (CVE)
- **CVE-2025-4037**: ATM simulator does not check for negative values with deposits or withdrawals, allowing attackers to increase their balance
- **CVE-2025-46687**: Chain: Javascript engine code does not perform a length check (CWE-1284) leading to integer overflow (CWE-190) causing allocation of smaller buffer than expected (CWE-131) resulting in a heap-based buffer overflow (CWE-122)
- **CVE-2019-19911**: Chain: Python library does not limit the resources used to process images that specify a very large number of bands (CWE-1284), leading to excessive memory consumption (CWE-789) or an integer overflow (CWE-190).
- **CVE-2008-1440**: lack of validation of length field leads to infinite loop
- **CVE-2008-2374**: lack of validation of string length fields allows memory consumption or buffer over-read

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1284.html
