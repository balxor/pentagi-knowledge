---
cwe_id: CWE-623
name: Unsafe ActiveX Control Marked Safe For Scripting
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/623.html
tags: [mitre-cwe, weakness, CWE-623]
---

# CWE-623 - Unsafe ActiveX Control Marked Safe For Scripting

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-623](https://cwe.mitre.org/data/definitions/623.html)

## Description
An ActiveX control is intended for restricted use, but it has been marked as safe-for-scripting.

## Extended description
This might allow attackers to use dangerous functionality via a web page that accesses the control, which can lead to different resultant vulnerabilities, depending on the control's behavior.

## Applicable platforms / languages
Not Language-Specific, Web Based

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: During development, do not mark it as safe for scripting.
- **System Configuration**: After distribution, you can set the kill bit for the control so that it is not accessible from Internet Explorer.

## Related weaknesses
- CWE-267 (ChildOf)
- CWE-618 (PeerOf)

## Observed examples (CVE)
- **CVE-2007-0617**: control allows attackers to add malicious email addresses to bypass spam limits
- **CVE-2007-0219**: web browser uses certain COM objects as ActiveX
- **CVE-2006-6510**: kiosk allows bypass to read files

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/623.html
