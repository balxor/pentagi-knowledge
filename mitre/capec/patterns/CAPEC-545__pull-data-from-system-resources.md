---
capec_id: CAPEC-545
name: Pull Data from System Resources
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-1239, CWE-1243, CWE-1258, CWE-1266, CWE-1272, CWE-1278, CWE-1323, CWE-1258, CWE-1330]
related_attack: [T1005, T1555.001]
url: https://capec.mitre.org/data/definitions/545.html
tags: [mitre-capec, attack-pattern, CAPEC-545]
---

# CAPEC-545 - Pull Data from System Resources

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)

## Description
An adversary who is authorized or has the ability to search known system resources, does so with the intention of gathering useful information. System resources include files, memory, and other aspects of the target system. In this pattern of attack, the adversary does not necessarily know what they are going to find when they start pulling data. This is different than CAPEC-150 where the adversary knows what they are looking for due to the common location.

## Related weaknesses (CWE)
- [CWE-1239](https://cwe.mitre.org/data/definitions/1239.html)
- [CWE-1243](https://cwe.mitre.org/data/definitions/1243.html)
- [CWE-1258](https://cwe.mitre.org/data/definitions/1258.html)
- [CWE-1266](https://cwe.mitre.org/data/definitions/1266.html)
- [CWE-1272](https://cwe.mitre.org/data/definitions/1272.html)
- [CWE-1278](https://cwe.mitre.org/data/definitions/1278.html)
- [CWE-1323](https://cwe.mitre.org/data/definitions/1323.html)
- [CWE-1258](https://cwe.mitre.org/data/definitions/1258.html)
- [CWE-1330](https://cwe.mitre.org/data/definitions/1330.html)

## Related ATT&CK techniques
- T1005
- T1555.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/545.html
