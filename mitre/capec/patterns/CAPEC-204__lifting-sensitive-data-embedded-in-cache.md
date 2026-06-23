---
capec_id: CAPEC-204
name: Lifting Sensitive Data Embedded in Cache
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-524, CWE-311, CWE-1239, CWE-1258]
related_attack: [T1005]
url: https://capec.mitre.org/data/definitions/204.html
tags: [mitre-capec, attack-pattern, CAPEC-204]
---

# CAPEC-204 - Lifting Sensitive Data Embedded in Cache

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-204](https://capec.mitre.org/data/definitions/204.html)

## Description
An adversary examines a target application's cache, or a browser cache, for sensitive information. Many applications that communicate with remote entities or which perform intensive calculations utilize caches to improve efficiency. However, if the application computes or receives sensitive information and the cache is not appropriately protected, an attacker can browse the cache and retrieve this information. This can result in the disclosure of sensitive information.

## Prerequisites
- The target application must store sensitive information in a cache.
- The cache must be inadequately protected against attacker access.

## Resources required
- The attacker must be able to reach the target application's cache. This may require prior access to the machine on which the target application runs. If the cache is encrypted, the attacker would need sufficient computational resources to crack the encryption. With strong encryption schemes, doing this could be intractable, but weaker encryption schemes could allow an attacker with sufficient resources to read the file.

## Execution flow
Execution Flow Explore Identify Application Cache: An adversary first identifies an application that utilizes a cache. This could either be a web application storing data in a browser cache, or an application running on a separate machine. The adversary examines the cache to determine file permissions and possible encryption. Techniques Use probing tools to look for application cache files on a machine. Use a web application and determine if any sensitive information is stored in browser cache. Experiment Attempt to Access Cache: Once the cache has been discovered, the adversary attempts to access the cached data. This often requires previous access to a machine hosting the target application. Techniques Use priviledge escalation to access cache files that might have strict privileges. If the application cache is encrypted with weak encryption, attempt to understand the encryption technique and break the encryption. Exploit Lift Sensitive Data from Cache: After gaining access to cached data, an adversary looks for potentially sensitive information and stores it for malicious use. This sensitive data could possibly be used in follow-up attacks related to authentication or authorization. Techniques Using a public computer, or gaining access to a victim's computer, examine browser cache to look for sensitive data left over from previous sessions.

## Related weaknesses (CWE)
- [CWE-524](https://cwe.mitre.org/data/definitions/524.html)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)
- [CWE-1239](https://cwe.mitre.org/data/definitions/1239.html)
- [CWE-1258](https://cwe.mitre.org/data/definitions/1258.html)

## Related ATT&CK techniques
- T1005

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/204.html
