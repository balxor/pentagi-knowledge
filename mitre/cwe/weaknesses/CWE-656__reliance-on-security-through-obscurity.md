---
cwe_id: CWE-656
name: Reliance on Security Through Obscurity
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/656.html
tags: [mitre-cwe, weakness, CWE-656]
---

# CWE-656 - Reliance on Security Through Obscurity

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-656](https://cwe.mitre.org/data/definitions/656.html)

## Description
The product uses a protection mechanism whose strength depends heavily on its obscurity, such that knowledge of its algorithms or key data is sufficient to defeat the mechanism.

## Extended description
This reliance on "security through obscurity" can produce resultant weaknesses if an attacker is able to reverse engineer the inner workings of the mechanism. Note that obscurity can be one small part of defense in depth, since it can create more work for an attacker; however, it is a significant risk if used as the primary means of protection.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Other**: Other

## Potential mitigations
- **Architecture and Design**: Always consider whether knowledge of your code or design is sufficient to break it. Reverse engineering is a highly successful discipline, and financially feasible for motivated adversaries. Black-box techniques are established for binary analysis of executables that use obfuscation, runtime analysis of proprietary protocols, inferring file formats, and others.
- **Architecture and Design**: When available, use publicly-vetted algorithms and procedures, as these are more likely to undergo more extensive security analysis and testing. This is especially the case with encryption and authentication.

## Related weaknesses
- CWE-657 (ChildOf)
- CWE-693 (ChildOf)
- CWE-259 (CanPrecede)
- CWE-321 (CanPrecede)
- CWE-472 (CanPrecede)

## Observed examples (CVE)
- **CVE-2006-6588**: Reliance on hidden form fields in a web application. Many web application vulnerabilities exist because the developer did not consider that "hidden" form fields can be processed using a modified client.
- **CVE-2006-7142**: Hard-coded cryptographic key stored in executable program.
- **CVE-2005-4002**: Hard-coded cryptographic key stored in executable program.
- **CVE-2006-4068**: Hard-coded hashed values for username and password contained in client-side script, allowing brute-force offline attacks.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/656.html
