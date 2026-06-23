---
cwe_id: CWE-288
name: Authentication Bypass Using an Alternate Path or Channel
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: [CAPEC-127, CAPEC-665]
url: https://cwe.mitre.org/data/definitions/288.html
tags: [mitre-cwe, weakness, CWE-288]
---

# CWE-288 - Authentication Bypass Using an Alternate Path or Channel

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-288](https://cwe.mitre.org/data/definitions/288.html)

## Description
The product requires authentication, but the product has an alternate path or channel that does not require authentication.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Funnel all access through a single choke point to simplify how users can access a resource. For every access, perform a check to determine if the user has permissions to access the resource.

## Related attack patterns (CAPEC)
- [CAPEC-127](https://capec.mitre.org/data/definitions/127.html)
- [CAPEC-665](https://capec.mitre.org/data/definitions/665.html)

## Related weaknesses
- CWE-306 (ChildOf)
- CWE-284 (ChildOf)
- CWE-420 (PeerOf)

## Observed examples (CVE)
- **CVE-2000-1179**: Router allows remote attackers to read system logs without authentication by directly connecting to the login screen and typing certain control characters.
- **CVE-1999-1454**: Attackers with physical access to the machine may bypass the password prompt by pressing the ESC (Escape) key.
- **CVE-1999-1077**: OS allows local attackers to bypass the password protection of idled sessions via the programmer's switch or CMD-PWR keyboard sequence, which brings up a debugger that the attacker can use to disable the lock.
- **CVE-2003-0304**: Direct request of installation file allows attacker to create administrator accounts.
- **CVE-2002-0870**: Attackers may gain additional privileges by directly requesting the web management URL.
- **CVE-2002-0066**: Bypass authentication via direct request to named pipe.
- **CVE-2003-1035**: User can avoid lockouts by using an API instead of the GUI to conduct brute force password guessing.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/288.html
