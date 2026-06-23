---
cwe_id: CWE-422
name: Unprotected Windows Messaging Channel ('Shatter')
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/422.html
tags: [mitre-cwe, weakness, CWE-422]
---

# CWE-422 - Unprotected Windows Messaging Channel ('Shatter')

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-422](https://cwe.mitre.org/data/definitions/422.html)

## Description
The product does not properly verify the source of a message in the Windows Messaging System while running at elevated privileges, creating an alternate channel through which an attacker can directly send a message to the product.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Always verify and authenticate the source of the message.

## Related weaknesses
- CWE-420 (ChildOf)
- CWE-360 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0971**: Bypass GUI and access restricted dialog box.
- **CVE-2002-1230**: Gain privileges via Windows message.
- **CVE-2003-0350**: A control allows a change to a pointer for a callback function using Windows message.
- **CVE-2003-0908**: Product launches Help functionality while running with raised privileges, allowing command execution using Windows message to access "open file" dialog.
- **CVE-2004-0213**: Attacker uses Shatter attack to bypass GUI-enforced protection for CVE-2003-0908.
- **CVE-2004-0207**: User can call certain API functions to modify certain properties of privileged programs.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/422.html
