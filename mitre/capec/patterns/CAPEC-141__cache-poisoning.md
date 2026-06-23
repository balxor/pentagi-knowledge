---
capec_id: CAPEC-141
name: Cache Poisoning
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-348, CWE-345, CWE-349, CWE-346]
related_attack: [T1557.002]
url: https://capec.mitre.org/data/definitions/141.html
tags: [mitre-capec, attack-pattern, CAPEC-141]
---

# CAPEC-141 - Cache Poisoning

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-141](https://capec.mitre.org/data/definitions/141.html)

## Description
An attacker exploits the functionality of cache technologies to cause specific data to be cached that aids the attackers' objectives. This describes any attack whereby an attacker places incorrect or harmful material in cache. The targeted cache can be an application's cache (e.g. a web browser cache) or a public cache (e.g. a DNS or ARP cache). Until the cache is refreshed, most applications or clients will treat the corrupted cache value as valid. This can lead to a wide range of exploits including redirecting web browsers towards sites that install malware and repeatedly incorrect calculations based on the incorrect value.

## Prerequisites
- The attacker must be able to modify the value stored in a cache to match a desired value.
- The targeted application must not be able to detect the illicit modification of the cache and must trust the cache value in its calculations.

## Skills required
- **Medium**: To overwrite/modify targeted cache

## Execution flow
Execution Flow Explore Identify and explore caches: Use tools to sniff traffic and scan a network in order to locate application's cache (e.g. a web browser cache) or a public cache (e.g. a DNS or ARP cache) that may have vulnerabilities. Look for poisoning point in cache table entries. Techniques Run tools that check available entries in the cache. Experiment Cause specific data to be cached: An attacker sends bogus request to the target, and then floods responses that trick a cache to remember malicious responses, which are wrong answers of queries. Techniques Intercept or modify a query, or send a bogus query with known credentials (such as transaction ID). Exploit Redirect users to malicious website: As the attacker succeeds in exploiting the vulnerability, they are able to manipulate and interpose malicious response data to targeted victim queries. Techniques Intercept or modify a query, or send a bogus query with known credentials (such as transaction ID). Adversary-in-the-Middle attacks (CAPEC-94) intercept secure communication between two parties.

## Mitigations
- Configuration: Disable client side caching.
- Implementation: Listens for query replies on a network, and sends a notification via email when an entry changes.

## Related weaknesses (CWE)
- [CWE-348](https://cwe.mitre.org/data/definitions/348.html)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)
- [CWE-349](https://cwe.mitre.org/data/definitions/349.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)

## Related ATT&CK techniques
- T1557.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/141.html
