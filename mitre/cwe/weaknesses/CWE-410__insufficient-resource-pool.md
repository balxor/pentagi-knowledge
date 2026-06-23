---
cwe_id: CWE-410
name: Insufficient Resource Pool
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/410.html
tags: [mitre-cwe, weakness, CWE-410]
---

# CWE-410 - Insufficient Resource Pool

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-410](https://cwe.mitre.org/data/definitions/410.html)

## Description
The product's resource pool is not large enough to handle peak demand, which allows an attacker to prevent others from accessing the resource by using a (relatively) large number of requests for resources.

## Extended description
Frequently the consequence is a "flood" of connection or sessions.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability, Integrity, Other**: DoS: Crash, Exit, or Restart, Other

## Potential mitigations
- **Architecture and Design**: Do not perform resource-intensive transactions for unauthenticated users and/or invalid requests.
- **Architecture and Design**: Consider implementing a velocity check mechanism which would detect abusive behavior.
- **Operation**: Consider load balancing as an option to handle heavy loads.
- **Implementation**: Make sure that resource handles are properly closed when no longer needed.
- **Architecture and Design**: Identify the system's resource intensive operations and consider protecting them from abuse (e.g. malicious automated script which runs the resources out).

## Related weaknesses
- CWE-664 (ChildOf)
- CWE-400 (CanPrecede)

## Observed examples (CVE)
- **CVE-1999-1363**: Large number of locks on file exhausts the pool and causes crash.
- **CVE-2001-1340**: Product supports only one connection and does not disconnect a user who does not provide credentials.
- **CVE-2002-0406**: Large number of connections without providing credentials allows connection exhaustion.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/410.html
