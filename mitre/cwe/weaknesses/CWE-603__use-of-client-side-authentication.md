---
cwe_id: CWE-603
name: Use of Client-Side Authentication
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/603.html
tags: [mitre-cwe, weakness, CWE-603]
---

# CWE-603 - Use of Client-Side Authentication

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-603](https://cwe.mitre.org/data/definitions/603.html)

## Description
A client/server product performs authentication within client code but not in server code, allowing server-side authentication to be bypassed via a modified client that omits the authentication check.

## Extended description
Client-side authentication is extremely weak and may be breached easily. Any attacker may read the source code and reverse-engineer the authentication mechanism to access parts of the application which would otherwise be protected.

## Applicable platforms / languages
Not Language-Specific, ICS/OT

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Do not rely on client side data. Always perform server side authentication.

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-602 (ChildOf)
- CWE-300 (PeerOf)
- CWE-656 (PeerOf)

## Observed examples (CVE)
- **CVE-2022-33139**: SCADA system only uses client-side authentication, allowing adversaries to impersonate other users.
- **CVE-2006-0230**: Client-side check for a password allows access to a server using crafted XML requests from a modified client.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/603.html
