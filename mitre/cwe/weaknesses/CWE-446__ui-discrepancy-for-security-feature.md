---
cwe_id: CWE-446
name: UI Discrepancy for Security Feature
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/446.html
tags: [mitre-cwe, weakness, CWE-446]
---

# CWE-446 - UI Discrepancy for Security Feature

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-446](https://cwe.mitre.org/data/definitions/446.html)

## Description
The user interface does not correctly enable or configure a security feature, but the interface provides feedback that causes the user to believe that the feature is in a secure state.

## Extended description
When the user interface does not properly reflect what the user asks of it, then it can lead the user into a false sense of security. For example, the user might check a box to enable a security option to enable encrypted communications, but the product does not actually enable the encryption. Alternately, the user might provide a "restrict ALL" access control rule, but the product only implements "restrict SOME".

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Related weaknesses
- CWE-684 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-1446**: UI inconsistency; visited URLs list not cleared when "Clear History" option is selected.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/446.html
