---
cwe_id: CWE-923
name: Improper Restriction of Communication Channel to Intended Endpoints
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based, Web Server]
related_capec: [CAPEC-161, CAPEC-481, CAPEC-501, CAPEC-697]
url: https://cwe.mitre.org/data/definitions/923.html
tags: [mitre-cwe, weakness, CWE-923]
---

# CWE-923 - Improper Restriction of Communication Channel to Intended Endpoints

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-923](https://cwe.mitre.org/data/definitions/923.html)

## Description
The product establishes a communication channel to (or from) an endpoint for privileged or protected operations, but it does not properly ensure that it is communicating with the correct endpoint.

## Extended description
Attackers might be able to spoof the intended endpoint from a different system or process, thus gaining the same level of access as the intended endpoint. While this issue frequently involves authentication between network-based clients and servers, other types of communication channels and endpoints can have this weakness.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, Web Server

## Common consequences
- **Integrity, Confidentiality**: Gain Privileges or Assume Identity

## Related attack patterns (CAPEC)
- [CAPEC-161](https://capec.mitre.org/data/definitions/161.html)
- [CAPEC-481](https://capec.mitre.org/data/definitions/481.html)
- [CAPEC-501](https://capec.mitre.org/data/definitions/501.html)
- [CAPEC-697](https://capec.mitre.org/data/definitions/697.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30319**: S-bus functionality in a home automation product performs access control using an IP allowlist, which can be bypassed by a forged IP address.
- **CVE-2022-22547**: A troubleshooting tool exposes a web server on a random port between 9000-65535 that could be used for information gathering
- **CVE-2022-4390**: A WAN interface on a router has firewall restrictions enabled for IPv4, but it does not for IPv6, which is enabled by default
- **CVE-2012-2292**: Product has a Silverlight cross-domain policy that does not restrict access to another application, which allows remote attackers to bypass the Same Origin Policy.
- **CVE-2012-5810**: Mobile banking application does not verify hostname, leading to financial loss.
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.
- **CVE-2000-1218**: DNS server can accept DNS updates from hosts that it did not query, leading to cache poisoning

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/923.html
