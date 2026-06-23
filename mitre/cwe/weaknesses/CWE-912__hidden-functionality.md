---
cwe_id: CWE-912
name: Hidden Functionality
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, ICS/OT]
related_capec: [CAPEC-133, CAPEC-190]
url: https://cwe.mitre.org/data/definitions/912.html
tags: [mitre-cwe, weakness, CWE-912]
---

# CWE-912 - Hidden Functionality

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-912](https://cwe.mitre.org/data/definitions/912.html)

## Description
The product contains functionality that is not documented, not part of the specification, and not accessible through an interface or command sequence that is obvious to the product's users or administrators.

## Extended description
Hidden functionality can take many forms, such as intentionally malicious code, "Easter Eggs" that contain extraneous functionality such as games, developer-friendly shortcuts that reduce maintenance or support costs such as hard-coded accounts, etc. From a security perspective, even when the functionality is not intentionally malicious or damaging, it can increase the product's attack surface and expose additional weaknesses beyond what is already exposed by the intended functionality. Even if it is not easily accessible, the hidden functionality could be useful for attacks that modify the control flow of the application.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Other, Integrity**: Varies by Context, Alter Execution Logic

## Potential mitigations
- **Installation**: Always verify the integrity of the product that is being installed.

## Related attack patterns (CAPEC)
- [CAPEC-133](https://capec.mitre.org/data/definitions/133.html)
- [CAPEC-190](https://capec.mitre.org/data/definitions/190.html)

## Related weaknesses
- CWE-684 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-31260**: Chain: a digital asset management program has an undisclosed backdoor in the legacy version of a PHP script (CWE-912) that could allow an unauthenticated user to export metadata (CWE-306)
- **CVE-2022-3203**: A wireless access point manual specifies that the only method of configuration is via web interface (CWE-1059), but there is an undisclosed telnet server that was activated by default (CWE-912).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/912.html
