---
cwe_id: CWE-602
name: Client-Side Enforcement of Server-Side Security
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, ICS/OT, Mobile]
related_capec: [CAPEC-162, CAPEC-202, CAPEC-207, CAPEC-208, CAPEC-21, CAPEC-31, CAPEC-383, CAPEC-384, CAPEC-385, CAPEC-386, CAPEC-387, CAPEC-388]
url: https://cwe.mitre.org/data/definitions/602.html
tags: [mitre-cwe, weakness, CWE-602]
---

# CWE-602 - Client-Side Enforcement of Server-Side Security

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-602](https://cwe.mitre.org/data/definitions/602.html)

## Description
The product is composed of a server that relies on the client to implement a mechanism that is intended to protect the server.

## Extended description
When the server relies on protection mechanisms placed on the client side, an attacker can modify the client-side behavior to bypass the protection mechanisms, resulting in potentially unexpected interactions between the client and server. The consequences will vary, depending on what the mechanisms are trying to protect.

## Applicable platforms / languages
Not Language-Specific, ICS/OT, Mobile

## Common consequences
- **Access Control, Availability**: Bypass Protection Mechanism, DoS: Crash, Exit, or Restart
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server. Even though client-side checks provide minimal benefits with respect to server-side security, they are still useful. First, they can support intrusion detection. If the server receives input that should have been rejected by the client, then it may be an indication of an attack. Second, client-side error-checking can provide helpful feedback to the user about the expectations for valid input. Third, there may be a reduction in server-side processing time for accidental input errors, although this is typically a small savings.
- **Architecture and Design**: If some degree of trust is required between the two entities, then use integrity checking and strong authentication to ensure that the inputs are coming from a trusted source. Design the product so that this trust is managed in a centralized fashion, especially if there are complex or numerous communication channels, in order to reduce the risks that the implementer will mistakenly omit a check in a single code path.

## Related attack patterns (CAPEC)
- [CAPEC-162](https://capec.mitre.org/data/definitions/162.html)
- [CAPEC-202](https://capec.mitre.org/data/definitions/202.html)
- [CAPEC-207](https://capec.mitre.org/data/definitions/207.html)
- [CAPEC-208](https://capec.mitre.org/data/definitions/208.html)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-383](https://capec.mitre.org/data/definitions/383.html)
- [CAPEC-384](https://capec.mitre.org/data/definitions/384.html)
- [CAPEC-385](https://capec.mitre.org/data/definitions/385.html)
- [CAPEC-386](https://capec.mitre.org/data/definitions/386.html)
- [CAPEC-387](https://capec.mitre.org/data/definitions/387.html)
- [CAPEC-388](https://capec.mitre.org/data/definitions/388.html)

## Related weaknesses
- CWE-693 (ChildOf)
- CWE-471 (CanPrecede)
- CWE-290 (PeerOf)
- CWE-300 (PeerOf)

## Observed examples (CVE)
- **CVE-2024-50653**: Chain: e-commerce product has a "front-end restriction" for coupon use (CWE-602), but the server does not restrict the number of requests for the same coupon (CWE-799)
- **CVE-2022-33139**: SCADA system only uses client-side authentication, allowing adversaries to impersonate other users.
- **CVE-2006-6994**: ASP program allows upload of .asp files by bypassing client-side checks.
- **CVE-2007-0163**: steganography products embed password information in the carrier file, which can be extracted from a modified client.
- **CVE-2007-0164**: steganography products embed password information in the carrier file, which can be extracted from a modified client.
- **CVE-2007-0100**: client allows server to modify client's configuration and overwrite arbitrary files.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/602.html
