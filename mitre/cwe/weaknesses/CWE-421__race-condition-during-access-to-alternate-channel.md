---
cwe_id: CWE-421
name: Race Condition During Access to Alternate Channel
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/421.html
tags: [mitre-cwe, weakness, CWE-421]
---

# CWE-421 - Race Condition During Access to Alternate Channel

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-421](https://cwe.mitre.org/data/definitions/421.html)

## Description
The product opens an alternate channel to communicate with an authorized user, but the channel is accessible to other actors.

## Extended description
This creates a race condition that allows an attacker to access the channel before the authorized user does.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Related weaknesses
- CWE-420 (ChildOf)
- CWE-362 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-0351**: FTP "Pizza Thief" vulnerability. Attacker can connect to a port that was intended for use by another client.
- **CVE-2003-0230**: Product creates Windows named pipe during authentication that another attacker can hijack by connecting to it.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/421.html
