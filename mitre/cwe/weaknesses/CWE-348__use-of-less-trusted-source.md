---
cwe_id: CWE-348
name: Use of Less Trusted Source
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-141, CAPEC-142, CAPEC-73, CAPEC-76, CAPEC-85]
url: https://cwe.mitre.org/data/definitions/348.html
tags: [mitre-cwe, weakness, CWE-348]
---

# CWE-348 - Use of Less Trusted Source

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-348](https://cwe.mitre.org/data/definitions/348.html)

## Description
The product has two different sources of the same data or information, but it uses the source that has less support for verification, is less trusted, or is less resistant to attack.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Related attack patterns (CAPEC)
- [CAPEC-141](https://capec.mitre.org/data/definitions/141.html)
- [CAPEC-142](https://capec.mitre.org/data/definitions/142.html)
- [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)
- [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)

## Related weaknesses
- CWE-345 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-0860**: Product uses IP address provided by a client, instead of obtaining it from the packet headers, allowing easier spoofing.
- **CVE-2004-1950**: Web product uses the IP address in the X-Forwarded-For HTTP header instead of a server variable that uses the connecting IP address, allowing filter bypass.
- **CVE-2001-0908**: Product logs IP address specified by the client instead of obtaining it from the packet headers, allowing information hiding.
- **CVE-2006-1126**: PHP application uses IP address from X-Forwarded-For HTTP header, instead of REMOTE_ADDR.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/348.html
