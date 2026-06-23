---
cwe_id: CWE-304
name: Missing Critical Step in Authentication
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/304.html
tags: [mitre-cwe, weakness, CWE-304]
---

# CWE-304 - Missing Critical Step in Authentication

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-304](https://cwe.mitre.org/data/definitions/304.html)

## Description
The product implements an authentication technique, but it skips a step that weakens the technique.

## Extended description
Authentication techniques should follow the algorithms that define them exactly, otherwise authentication can be bypassed or more easily subjected to brute force attacks.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Integrity, Confidentiality**: Bypass Protection Mechanism, Gain Privileges or Assume Identity, Read Application Data, Execute Unauthorized Code or Commands

## Related weaknesses
- CWE-303 (ChildOf)
- CWE-573 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-2163**: Shared secret not verified in a RADIUS response packet, allowing authentication bypass by spoofing server replies.
- **CVE-2005-3327**: Chain: Authentication bypass by skipping the first startup step as required by the protocol.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/304.html
