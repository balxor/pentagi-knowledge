---
cwe_id: CWE-697
name: Incorrect Comparison
type: weakness
abstraction: Pillar
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-10, CAPEC-120, CAPEC-14, CAPEC-15, CAPEC-182, CAPEC-24, CAPEC-267, CAPEC-3, CAPEC-41, CAPEC-43, CAPEC-44, CAPEC-45, CAPEC-46, CAPEC-47, CAPEC-52, CAPEC-53, CAPEC-6, CAPEC-64, CAPEC-67, CAPEC-7, CAPEC-71, CAPEC-73, CAPEC-78, CAPEC-79, CAPEC-8, CAPEC-80, CAPEC-88, CAPEC-9, CAPEC-92]
url: https://cwe.mitre.org/data/definitions/697.html
tags: [mitre-cwe, weakness, CWE-697]
---

# CWE-697 - Incorrect Comparison

**Abstraction:** Pillar  -  **Status:** Incomplete  -  **CWE:** [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

## Description
The product compares two entities in a security-relevant context, but the comparison is incorrect.

## Extended description
This Pillar covers several possibilities: the comparison checks one factor incorrectly; the comparison should consider multiple factors, but it does not check at least one of those factors at all; the comparison checks the wrong factor.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Other**: Varies by Context

## Related attack patterns (CAPEC)
- [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-14](https://capec.mitre.org/data/definitions/14.html)
- [CAPEC-15](https://capec.mitre.org/data/definitions/15.html)
- [CAPEC-182](https://capec.mitre.org/data/definitions/182.html)
- [CAPEC-24](https://capec.mitre.org/data/definitions/24.html)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-41](https://capec.mitre.org/data/definitions/41.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-44](https://capec.mitre.org/data/definitions/44.html)
- [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
- [CAPEC-46](https://capec.mitre.org/data/definitions/46.html)
- [CAPEC-47](https://capec.mitre.org/data/definitions/47.html)
- [CAPEC-52](https://capec.mitre.org/data/definitions/52.html)
- [CAPEC-53](https://capec.mitre.org/data/definitions/53.html)
- [CAPEC-6](https://capec.mitre.org/data/definitions/6.html)
- [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
- [CAPEC-67](https://capec.mitre.org/data/definitions/67.html)
- [CAPEC-7](https://capec.mitre.org/data/definitions/7.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
- [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
- [CAPEC-8](https://capec.mitre.org/data/definitions/8.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)
- [CAPEC-88](https://capec.mitre.org/data/definitions/88.html)
- [CAPEC-9](https://capec.mitre.org/data/definitions/9.html)
- [CAPEC-92](https://capec.mitre.org/data/definitions/92.html)

## Observed examples (CVE)
- **CVE-2021-3116**: Chain: Python-based HTTP Proxy server uses the wrong boolean operators (CWE-480) causing an incorrect comparison (CWE-697) that identifies an authN failure if all three conditions are met instead of only one, allowing bypass of the proxy authentication (CWE-1390)
- **CVE-2020-15811**: Chain: Proxy uses a substring search instead of parsing the Transfer-Encoding header (CWE-697), allowing request splitting (CWE-113) and cache poisoning
- **CVE-2016-10003**: Proxy performs incorrect comparison of request headers, leading to infoleak

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/697.html
