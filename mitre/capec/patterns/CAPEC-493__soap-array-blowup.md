---
capec_id: CAPEC-493
name: SOAP Array Blowup
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-770]
related_attack: []
url: https://capec.mitre.org/data/definitions/493.html
tags: [mitre-capec, attack-pattern, CAPEC-493]
---

# CAPEC-493 - SOAP Array Blowup

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-493](https://capec.mitre.org/data/definitions/493.html)

## Description
An adversary may execute an attack on a web service that uses SOAP messages in communication. By sending a very large SOAP array declaration to the web service, the attacker forces the web service to allocate space for the array elements before they are parsed by the XML parser. The attacker message is typically small in size containing a large array declaration of say 1,000,000 elements and a couple of array elements. This attack targets exhaustion of the memory resources of the web service.

## Prerequisites
- This type of an attack requires the attacker to know the endpoint of the web service, and be able to reach the endpoint with a malicious SOAP message.

## Mitigations
- Enforce strict schema validation. The schema should enforce a maximum number of array elements. If the number of maximum array elements can't be limited another validation method should be used. One such method could be comparing the declared number of items in the array with the existing number of elements of the array. If these numbers don't match drop the SOAP packet at the web service layer.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/493.html
