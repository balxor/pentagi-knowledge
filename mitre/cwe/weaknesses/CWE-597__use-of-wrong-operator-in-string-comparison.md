---
cwe_id: CWE-597
name: Use of Wrong Operator in String Comparison
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Java, JavaScript, PHP]
related_capec: []
url: https://cwe.mitre.org/data/definitions/597.html
tags: [mitre-cwe, weakness, CWE-597]
---

# CWE-597 - Use of Wrong Operator in String Comparison

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-597](https://cwe.mitre.org/data/definitions/597.html)

## Description
The product uses the wrong operator when comparing a string, such as using "==" when the .equals() method should be used instead.

## Extended description
In Java, using == or != to compare two strings for equality actually compares two objects for equality rather than their string values for equality. Chances are good that the two references will never be equal. While this weakness often only affects program correctness, if the equality is used for a security decision, the unintended comparison result could be leveraged to affect program security.

## Applicable platforms / languages
Not Language-Specific, Java, JavaScript, PHP

## Common consequences
- **Other**: Other

## Potential mitigations
- **Implementation**: Within Java, use .equals() to compare string values. Within JavaScript, use == to compare string values. Within PHP, use == to compare a numeric value to a string value. (PHP converts the string to a number.)

## Related weaknesses
- CWE-595 (ChildOf)
- CWE-595 (ChildOf)
- CWE-480 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/597.html
