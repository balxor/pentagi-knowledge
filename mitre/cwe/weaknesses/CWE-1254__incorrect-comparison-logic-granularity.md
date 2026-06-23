---
cwe_id: CWE-1254
name: Incorrect Comparison Logic Granularity
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-26]
url: https://cwe.mitre.org/data/definitions/1254.html
tags: [mitre-cwe, weakness, CWE-1254]
---

# CWE-1254 - Incorrect Comparison Logic Granularity

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1254](https://cwe.mitre.org/data/definitions/1254.html)

## Description
The product's comparison logic is performed over a series of steps rather than across the entire string in one operation. If there is a comparison logic failure on one of these steps, the operation may be vulnerable to a timing attack that can result in the interception of the process for nefarious purposes.

## Extended description
Comparison logic is used to compare a variety of objects including passwords, Message Authentication Codes (MACs), and responses to verification challenges. When comparison logic is implemented at a finer granularity (e.g., byte-by-byte comparison) and breaks in the case of a comparison failure, an attacker can exploit this implementation to identify when exactly the failure occurred. With multiple attempts, the attacker may be able to guesses the correct password/response to challenge and elevate their privileges.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Authorization**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: The hardware designer should ensure that comparison logic is implemented so as to compare in one operation instead in smaller chunks.

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)

## Related weaknesses
- CWE-208 (ChildOf)
- CWE-697 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-10482**: Smartphone OS uses comparison functions that are not in constant time, allowing side channels
- **CVE-2019-10071**: Java-oriented framework compares HMAC signatures using String.equals() instead of a constant-time algorithm, causing timing discrepancies
- **CVE-2014-0984**: Password-checking function in router terminates validation of a password entry when it encounters the first incorrect character, which allows remote attackers to obtain passwords via a brute-force attack that relies on timing differences in responses to incorrect password guesses, aka a timing side-channel attack.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1254.html
