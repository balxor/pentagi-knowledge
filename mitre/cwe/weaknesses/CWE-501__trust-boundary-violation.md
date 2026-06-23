---
cwe_id: CWE-501
name: Trust Boundary Violation
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/501.html
tags: [mitre-cwe, weakness, CWE-501]
---

# CWE-501 - Trust Boundary Violation

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-501](https://cwe.mitre.org/data/definitions/501.html)

## Description
The product mixes trusted and untrusted data in the same data structure or structured message.

## Extended description
A trust boundary can be thought of as line drawn through a program. On one side of the line, data is untrusted. On the other side of the line, data is assumed to be trustworthy. The purpose of validation logic is to allow data to safely cross the trust boundary - to move from untrusted to trusted. A trust boundary violation occurs when a program blurs the line between what is trusted and what is untrusted. By combining trusted and untrusted data in the same data structure, it becomes easier for programmers to mistakenly trust unvalidated data.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related weaknesses
- CWE-664 (ChildOf)
- CWE-349 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/501.html
