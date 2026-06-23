---
cwe_id: CWE-684
name: Incorrect Provision of Specified Functionality
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/684.html
tags: [mitre-cwe, weakness, CWE-684]
---

# CWE-684 - Incorrect Provision of Specified Functionality

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-684](https://cwe.mitre.org/data/definitions/684.html)

## Description
The code does not function according to its published specifications, potentially leading to incorrect usage.

## Extended description
When providing functionality to an external party, it is important that the product behaves in accordance with the details specified. When requirements of nuances are not documented, the functionality may produce unintended behaviors for the caller, possibly leading to an exploitable state.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: Ensure that your code strictly conforms to specifications.

## Related weaknesses
- CWE-710 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1446**: Error checking routine in PKCS#11 library returns "OK" status even when invalid signature is detected, allowing spoofed messages.
- **CVE-2001-1559**: Chain: System call returns wrong value (CWE-393), leading to a resultant NULL dereference (CWE-476).
- **CVE-2003-0187**: Program uses large timeouts on unconfirmed connections resulting from inconsistency in linked lists implementations.
- **CVE-1999-1446**: UI inconsistency; visited URLs list not cleared when "Clear History" option is selected.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/684.html
