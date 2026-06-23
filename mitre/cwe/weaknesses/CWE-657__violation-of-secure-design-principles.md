---
cwe_id: CWE-657
name: Violation of Secure Design Principles
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/657.html
tags: [mitre-cwe, weakness, CWE-657]
---

# CWE-657 - Violation of Secure Design Principles

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-657](https://cwe.mitre.org/data/definitions/657.html)

## Description
The product violates well-established principles for secure design.

## Extended description
This can introduce resultant weaknesses or make it easier for developers to introduce related weaknesses during implementation. Because code is centered around design, it can be resource-intensive to fix design problems.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Technology-Specific

## Common consequences
- **Other**: Other

## Related weaknesses
- CWE-710 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-6260**: Baseboard Management Controller (BMC) device implements Advanced High-performance Bus (AHB) bridges that do not require authentication for arbitrary read and write access to the BMC's physical address space from the host, and possibly the network [REF-1138].
- **CVE-2007-5277**: The failure of connection attempts in a web browser resets DNS pin restrictions. An attacker can then bypass the same origin policy by rebinding a domain name to a different IP address. This was an attempt to "fail functional."
- **CVE-2006-7142**: Hard-coded cryptographic key stored in executable program.
- **CVE-2007-0408**: Server does not properly validate client certificates when reusing cached connections.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/657.html
