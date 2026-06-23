---
cwe_id: CWE-1088
name: Synchronous Access of Remote Resource without Timeout
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1088.html
tags: [mitre-cwe, weakness, CWE-1088]
---

# CWE-1088 - Synchronous Access of Remote Resource without Timeout

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1088](https://cwe.mitre.org/data/definitions/1088.html)

## Description
The code has a synchronous call to a remote resource, but there is no timeout for the call, or the timeout is set to infinite.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-821 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-8062**: API endpoint performs a HEAD request without a timeout, allowing attackers to cause the server to hang
- **CVE-2024-8061**: development product for AI can make requests to external servers without timeouts and does not respond to other requests while waiting, allowing DoS

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1088.html
