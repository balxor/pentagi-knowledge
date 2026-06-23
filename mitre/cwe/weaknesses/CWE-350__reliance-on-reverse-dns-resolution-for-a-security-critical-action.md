---
cwe_id: CWE-350
name: Reliance on Reverse DNS Resolution for a Security-Critical Action
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-142, CAPEC-275, CAPEC-73, CAPEC-89]
url: https://cwe.mitre.org/data/definitions/350.html
tags: [mitre-cwe, weakness, CWE-350]
---

# CWE-350 - Reliance on Reverse DNS Resolution for a Security-Critical Action

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-350](https://cwe.mitre.org/data/definitions/350.html)

## Description
The product performs reverse DNS resolution on an IP address to obtain the hostname and make a security decision, but it does not properly ensure that the IP address is truly associated with the hostname.

## Extended description
Since DNS names can be easily spoofed or misreported, and it may be difficult for the product to detect if a trusted DNS server has been compromised, DNS names do not constitute a valid authentication mechanism. When the product performs a reverse DNS resolution for an IP address, if an attacker controls the DNS server for that IP address, then the attacker can cause the server to return an arbitrary hostname. As a result, the attacker may be able to bypass authentication, cause the wrong hostname to be recorded in log files to hide activities, or perform other attacks. Attackers can spoof DNS names by either (1) compromising a DNS server and modifying its records (sometimes called DNS cache poisoning), or (2) having legitimate control over a DNS server associated with their IP address.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Use other means of identity verification that cannot be simply spoofed. Possibilities include a username/password or certificate.
- **Implementation**: Perform proper forward and reverse DNS lookups to detect DNS spoofing.

## Related attack patterns (CAPEC)
- [CAPEC-142](https://capec.mitre.org/data/definitions/142.html)
- [CAPEC-275](https://capec.mitre.org/data/definitions/275.html)
- [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
- [CAPEC-89](https://capec.mitre.org/data/definitions/89.html)

## Related weaknesses
- CWE-290 (ChildOf)
- CWE-807 (ChildOf)
- CWE-923 (CanPrecede)

## Observed examples (CVE)
- **CVE-2001-1488**: Does not do double-reverse lookup to prevent DNS spoofing.
- **CVE-2001-1500**: Does not verify reverse-resolved hostnames in DNS.
- **CVE-2000-1221**: Authentication bypass using spoofed reverse-resolved DNS hostnames.
- **CVE-2002-0804**: Authentication bypass using spoofed reverse-resolved DNS hostnames.
- **CVE-2001-1155**: Filter does not properly check the result of a reverse DNS lookup, which could allow remote attackers to bypass intended access restrictions via DNS spoofing.
- **CVE-2004-0892**: Reverse DNS lookup used to spoof trusted content in intermediary.
- **CVE-2003-0981**: Product records the reverse DNS name of a visitor in the logs, allowing spoofing and resultant XSS.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/350.html
