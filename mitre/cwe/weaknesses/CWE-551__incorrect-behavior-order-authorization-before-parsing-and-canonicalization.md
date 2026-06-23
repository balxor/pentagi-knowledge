---
cwe_id: CWE-551
name: Incorrect Behavior Order: Authorization Before Parsing and Canonicalization
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/551.html
tags: [mitre-cwe, weakness, CWE-551]
---

# CWE-551 - Incorrect Behavior Order: Authorization Before Parsing and Canonicalization

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-551](https://cwe.mitre.org/data/definitions/551.html)

## Description
If a web server does not fully parse requested URLs before it examines them for authorization, it may be possible for an attacker to bypass authorization protection.

## Extended description
For instance, the character strings /./ and / both mean current directory. If /SomeDirectory is a protected directory and an attacker requests /./SomeDirectory, the attacker may be able to gain access to the resource if /./ is not converted to / before the authorization check is performed.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, Web Server

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: URL Inputs should be decoded and canonicalized to the application's current internal representation before being validated and processed for authorization. Make sure that your application does not decode the same input twice. Such errors could be used to bypass allowlist schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-863 (ChildOf)
- CWE-696 (ChildOf)
- CWE-41 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/551.html
