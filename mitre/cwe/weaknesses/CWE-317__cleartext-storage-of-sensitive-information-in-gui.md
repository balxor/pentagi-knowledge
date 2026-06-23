---
cwe_id: CWE-317
name: Cleartext Storage of Sensitive Information in GUI
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Windows]
related_capec: []
url: https://cwe.mitre.org/data/definitions/317.html
tags: [mitre-cwe, weakness, CWE-317]
---

# CWE-317 - Cleartext Storage of Sensitive Information in GUI

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-317](https://cwe.mitre.org/data/definitions/317.html)

## Description
The product stores sensitive information in cleartext within the GUI.

## Extended description
An attacker can often obtain data from a GUI, even if hidden, by using an API to directly access GUI objects such as windows and menus. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Applicable platforms / languages
Not Language-Specific, Windows

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data

## Related weaknesses
- CWE-312 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1848**: Unencrypted passwords stored in GUI dialog may allow local users to access the passwords.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/317.html
