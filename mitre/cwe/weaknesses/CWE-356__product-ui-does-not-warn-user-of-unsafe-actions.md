---
cwe_id: CWE-356
name: Product UI does not Warn User of Unsafe Actions
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/356.html
tags: [mitre-cwe, weakness, CWE-356]
---

# CWE-356 - Product UI does not Warn User of Unsafe Actions

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-356](https://cwe.mitre.org/data/definitions/356.html)

## Description
The product's user interface does not warn the user before undertaking an unsafe action on behalf of that user. This makes it easier for attackers to trick users into inflicting damage to their system.

## Extended description
Product systems should warn users that a potentially dangerous action may occur if the user proceeds. For example, if the user downloads a file from an unknown source and attempts to execute the file on their machine, then the application's GUI can indicate that the file is unsafe.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Non-Repudiation**: Hide Activities

## Related weaknesses
- CWE-221 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-1055**: Product does not warn user when document contains certain dangerous functions or macros.
- **CVE-1999-0794**: Product does not warn user when document contains certain dangerous functions or macros.
- **CVE-2000-0277**: Product does not warn user when document contains certain dangerous functions or macros.
- **CVE-2000-0517**: Product does not warn user about a certificate if it has already been accepted for a different site. Possibly resultant.
- **CVE-2005-0602**: File extractor does not warn user if setuid/setgid files could be extracted. Overlaps privileges/permissions.
- **CVE-2000-0342**: E-mail client allows bypass of warning for dangerous attachments via a Windows .LNK file that refers to the attachment.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/356.html
