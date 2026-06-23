---
cwe_id: CWE-360
name: Trust of System Event Data
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/360.html
tags: [mitre-cwe, weakness, CWE-360]
---

# CWE-360 - Trust of System Event Data

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-360](https://cwe.mitre.org/data/definitions/360.html)

## Description
Security based on event locations are insecure and can be spoofed.

## Extended description
Events are a messaging system which may provide control data to programs listening for events. Events often do not have any type of authentication framework to allow them to be verified from a trusted source. Any application, in Windows, on a given desktop can send a message to any window on the same desktop. There is no authentication framework for these messages. Therefore, any message can be used to manipulate any process on the desktop if the process does not check the validity and safeness of those messages.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Confidentiality, Availability, Access Control**: Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Never trust or rely any of the information in an Event for security.

## Related weaknesses
- CWE-345 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-0213**: Attacker uses Shatter attack to bypass GUI-enforced protection for CVE-2003-0908.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/360.html
