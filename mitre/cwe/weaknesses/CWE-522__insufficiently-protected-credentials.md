---
cwe_id: CWE-522
name: Insufficiently Protected Credentials
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based, ICS/OT]
related_capec: [CAPEC-102, CAPEC-474, CAPEC-50, CAPEC-509, CAPEC-551, CAPEC-555, CAPEC-560, CAPEC-561, CAPEC-600, CAPEC-644, CAPEC-645, CAPEC-652, CAPEC-653]
url: https://cwe.mitre.org/data/definitions/522.html
tags: [mitre-cwe, weakness, CWE-522]
---

# CWE-522 - Insufficiently Protected Credentials

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-522](https://cwe.mitre.org/data/definitions/522.html)

## Description
The product transmits or stores authentication credentials, but it uses an insecure method that is susceptible to unauthorized interception and/or retrieval.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, ICS/OT

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Use an appropriate security mechanism to protect the credentials.
- **Architecture and Design**: Make appropriate use of cryptography to protect the credentials.
- **Implementation**: Use industry standards to protect the credentials (e.g. LDAP, keystore, etc.).

## Related attack patterns (CAPEC)
- [CAPEC-102](https://capec.mitre.org/data/definitions/102.html)
- [CAPEC-474](https://capec.mitre.org/data/definitions/474.html)
- [CAPEC-50](https://capec.mitre.org/data/definitions/50.html)
- [CAPEC-509](https://capec.mitre.org/data/definitions/509.html)
- [CAPEC-551](https://capec.mitre.org/data/definitions/551.html)
- [CAPEC-555](https://capec.mitre.org/data/definitions/555.html)
- [CAPEC-560](https://capec.mitre.org/data/definitions/560.html)
- [CAPEC-561](https://capec.mitre.org/data/definitions/561.html)
- [CAPEC-600](https://capec.mitre.org/data/definitions/600.html)
- [CAPEC-644](https://capec.mitre.org/data/definitions/644.html)
- [CAPEC-645](https://capec.mitre.org/data/definitions/645.html)
- [CAPEC-652](https://capec.mitre.org/data/definitions/652.html)
- [CAPEC-653](https://capec.mitre.org/data/definitions/653.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-287 (ChildOf)
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30018**: A messaging platform serializes all elements of User/Group objects, making private information available to adversaries
- **CVE-2022-29959**: Initialization file contains credentials that can be decoded using a "simple string transformation"
- **CVE-2022-35411**: Python-based RPC framework enables pickle functionality by default, allowing clients to unpickle untrusted data.
- **CVE-2022-29519**: Programmable Logic Controller (PLC) sends sensitive information in plaintext, including passwords and session tokens.
- **CVE-2022-30312**: Building Controller uses a protocol that transmits authentication credentials in plaintext.
- **CVE-2022-31204**: Programmable Logic Controller (PLC) sends password in plaintext.
- **CVE-2022-30275**: Remote Terminal Unit (RTU) uses a driver that relies on a password stored in plaintext.
- **CVE-2007-0681**: Web app allows remote attackers to change the passwords of arbitrary users without providing the original password, and possibly perform other unauthorized actions.
- **CVE-2000-0944**: Web application password change utility doesn't check the original password.
- **CVE-2005-3435**: product authentication succeeds if user-provided MD5 hash matches the hash in its database; this can be subjected to replay attacks.
- **CVE-2005-0408**: chain: product generates predictable MD5 hashes using a constant value combined with username, allowing authentication bypass.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/522.html
