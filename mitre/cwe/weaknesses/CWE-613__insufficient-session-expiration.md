---
cwe_id: CWE-613
name: Insufficient Session Expiration
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/613.html
tags: [mitre-cwe, weakness, CWE-613]
---

# CWE-613 - Insufficient Session Expiration

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-613](https://cwe.mitre.org/data/definitions/613.html)

## Description
According to WASC, "Insufficient Session Expiration is when a web site permits an attacker to reuse old session credentials or session IDs for authorization."

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Set sessions/credentials expiration date.

## Related weaknesses
- CWE-672 (ChildOf)
- CWE-672 (ChildOf)
- CWE-287 (CanPrecede)

## Observed examples (CVE)
- **CVE-2025-46344**: JavaScript SDK does not set an expiration time for JWE tokens related to a session
- **CVE-2024-8888**: Web interface for a power quality analyzer uses tokens without an expiration date
- **CVE-2024-35206**: network traffic analyzer for PROFINET networks does not expire sessions
- **CVE-2024-27782**: AI/ML monitor for IT operations allows re-use of old session tokens due to insufficient session expiration

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/613.html
