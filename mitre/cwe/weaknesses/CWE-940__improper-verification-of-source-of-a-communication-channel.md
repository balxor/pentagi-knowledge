---
cwe_id: CWE-940
name: Improper Verification of Source of a Communication Channel
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Mobile]
related_capec: [CAPEC-500, CAPEC-594, CAPEC-595, CAPEC-596]
url: https://cwe.mitre.org/data/definitions/940.html
tags: [mitre-cwe, weakness, CWE-940]
---

# CWE-940 - Improper Verification of Source of a Communication Channel

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-940](https://cwe.mitre.org/data/definitions/940.html)

## Description
The product establishes a communication channel to handle an incoming request that has been initiated by an actor, but it does not properly verify that the request is coming from the expected origin.

## Extended description
When an attacker can successfully establish a communication channel from an untrusted origin, the attacker may be able to gain privileges and access unexpected functionality.

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Access Control, Other**: Gain Privileges or Assume Identity, Varies by Context, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Use a mechanism that can validate the identity of the source, such as a certificate, and validate the integrity of data to ensure that it cannot be modified in transit using an Adversary-in-the-Middle (AITM) attack. When designing functionality of actions in the URL scheme, consider whether the action should be accessible to all mobile applications, or if an allowlist of applications to interface with is appropriate.

## Related attack patterns (CAPEC)
- [CAPEC-500](https://capec.mitre.org/data/definitions/500.html)
- [CAPEC-594](https://capec.mitre.org/data/definitions/594.html)
- [CAPEC-595](https://capec.mitre.org/data/definitions/595.html)
- [CAPEC-596](https://capec.mitre.org/data/definitions/596.html)

## Related weaknesses
- CWE-923 (ChildOf)
- CWE-346 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-3651**: desktop product does not properly verify the source of a communication channel, allowing command execution
- **CVE-2000-1218**: DNS server can accept DNS updates from hosts that it did not query, leading to cache poisoning
- **CVE-2005-0877**: DNS server can accept DNS updates from hosts that it did not query, leading to cache poisoning
- **CVE-2001-1452**: DNS server caches glue records received from non-delegated name servers

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/940.html
