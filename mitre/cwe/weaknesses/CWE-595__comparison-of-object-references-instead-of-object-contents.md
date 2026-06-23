---
cwe_id: CWE-595
name: Comparison of Object References Instead of Object Contents
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java, JavaScript, PHP, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/595.html
tags: [mitre-cwe, weakness, CWE-595]
---

# CWE-595 - Comparison of Object References Instead of Object Contents

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-595](https://cwe.mitre.org/data/definitions/595.html)

## Description
The product compares object references instead of the contents of the objects themselves, preventing it from detecting equivalent objects.

## Extended description
For example, in Java, comparing objects using == usually produces deceptive results, since the == operator compares object references rather than values; often, this means that using == for strings is actually comparing the strings' references, not their values.

## Applicable platforms / languages
Java, JavaScript, PHP, Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Implementation**: In Java, use the equals() method to compare objects instead of the == operator. If using ==, it is important for performance reasons that your objects are created by a static factory, not by a constructor.

## Related weaknesses
- CWE-1025 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/595.html
