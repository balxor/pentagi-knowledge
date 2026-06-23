---
capec_id: CAPEC-142
name: DNS Cache Poisoning
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-348, CWE-345, CWE-349, CWE-346, CWE-350]
related_attack: [T1584.002]
url: https://capec.mitre.org/data/definitions/142.html
tags: [mitre-capec, attack-pattern, CAPEC-142]
---

# CAPEC-142 - DNS Cache Poisoning

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-142](https://capec.mitre.org/data/definitions/142.html)

## Description
A domain name server translates a domain name (such as www.example.com) into an IP address that Internet hosts use to contact Internet resources. An adversary modifies a public DNS cache to cause certain names to resolve to incorrect addresses that the adversary specifies. The result is that client applications that rely upon the targeted cache for domain name resolution will be directed not to the actual address of the specified domain name but to some other address. Adversaries can use this to herd clients to sites that install malware on the victim's computer or to masquerade as part of a Pharming attack.

## Prerequisites
- A DNS cache must be vulnerable to some attack that allows the adversary to replace addresses in its lookup table.Client applications must trust the corrupted cashed values and utilize them for their domain name resolutions.

## Skills required
- **Medium**: To overwrite/modify targeted DNS cache

## Resources required
- The adversary must have the resources to modify the targeted cache. In addition, in most cases the adversary will wish to host the sites to which users will be redirected, although in some cases redirecting to a third party site will accomplish the adversary's goals.

## Execution flow
Execution Flow Explore Explore resolver caches: Check DNS caches on local DNS server and client's browser with DNS cache enabled. Techniques Run tools that check the resolver cache in the memory to see if it contains a target DNS entry. Figure out if the client's browser has DNS cache enabled. Experiment Attempt sending crafted records to DNS cache: A request is sent to the authoritative server for target website and wait for the iterative name resolver. An adversary sends bogus request to the DNS local server, and then floods responses that trick a DNS cache to remember malicious responses, which are wrong answers of DNS query. Techniques Adversary must know the transaction ID by intercepting a DNS query, or sending a bogus query with known transaction ID. If the transaction ID used to identify each query instance is randomized in some new DNS software, the attack must guess the transaction ID. Slow the response of the real DNS server by causing Denial-of-service. This gives adversaries enough time to guess transaction Adversary crafts DNS response with the same transaction ID as in the request. The adversary sends out DNS responses before the authorized DNS server. This forces DNS local cache stores fake DNS response (wrong answer). The fake DNS responses usually include a malicious website's IP address. Exploit Redirect users to malicious website: As the adversary succeeds in exploiting the vulnerability, the victim connects to a malicious site using a good web site's domain name. Techniques Redirecting Web traffic to a site that looks enough like the original so as to not raise any suspicion. Adversary-in-the-Middle (CAPEC-94) intercepts secure communication between two parties.

## Mitigations
- Configuration: Make sure your DNS servers have been updated to the latest versions
- Configuration: UNIX services like rlogin, rsh/rcp, xhost, and nfs are all susceptible to wrong information being held in a cache. Care should be taken with these services so they do not rely upon DNS caches that have been exposed to the Internet.
- Configuration: Disable client side DNS caching.

## Related weaknesses (CWE)
- [CWE-348](https://cwe.mitre.org/data/definitions/348.html)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)
- [CWE-349](https://cwe.mitre.org/data/definitions/349.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-350](https://cwe.mitre.org/data/definitions/350.html)

## Related ATT&CK techniques
- T1584.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/142.html
