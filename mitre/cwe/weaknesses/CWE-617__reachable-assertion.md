---
cwe_id: CWE-617
name: Reachable Assertion
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, C, Java, Rust, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/617.html
tags: [mitre-cwe, weakness, CWE-617]
---

# CWE-617 - Reachable Assertion

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-617](https://cwe.mitre.org/data/definitions/617.html)

## Description
The product contains an assert() or similar statement that can be triggered by an attacker, which leads to an application exit or other behavior that is more severe than necessary.

## Extended description
While assertion is good for catching logic errors and reducing the chances of reaching more serious vulnerability conditions, it can still lead to a denial of service. For example, if a server handles multiple simultaneous connections, and an assert() occurs in one single connection that causes all other connections to be dropped, this is a reachable assertion that leads to a denial of service.

## Applicable platforms / languages
Not Language-Specific, C, Java, Rust, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Make sensitive open/close operation non reachable by directly user-controlled data (e.g. open/close resources)
- **Implementation**: Perform input validation on user data.

## Related weaknesses
- CWE-705 (ChildOf)
- CWE-670 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-8768**: API server for LLM library can crash when provided an empty prompt, which triggers a reachable assertion
- **CVE-2023-49286**: Chain: function in web caching proxy does not correctly check a return value (CWE-253) leading to a reachable assertion (CWE-617)
- **CVE-2006-6767**: FTP server allows remote attackers to cause a denial of service (daemon abort) via crafted commands which trigger an assertion failure.
- **CVE-2006-6811**: Chat client allows remote attackers to cause a denial of service (crash) via a long message string when connecting to a server, which causes an assertion failure.
- **CVE-2006-5779**: Product allows remote attackers to cause a denial of service (daemon crash) via LDAP BIND requests with long authcid names, which triggers an assertion failure.
- **CVE-2006-4095**: Product allows remote attackers to cause a denial of service (crash) via certain queries, which cause an assertion failure.
- **CVE-2006-4574**: Chain: security monitoring product has an off-by-one error that leads to unexpected length values, triggering an assertion.
- **CVE-2004-0270**: Anti-virus product has assert error when line length is non-numeric.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/617.html
