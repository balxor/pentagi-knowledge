---
cwe_id: CWE-836
name: Use of Password Hash Instead of Password for Authentication
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-644, CAPEC-652]
url: https://cwe.mitre.org/data/definitions/836.html
tags: [mitre-cwe, weakness, CWE-836]
---

# CWE-836 - Use of Password Hash Instead of Password for Authentication

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-836](https://cwe.mitre.org/data/definitions/836.html)

## Description
The product records password hashes in a data store, receives a hash of a password from a client, and compares the supplied hash to the hash obtained from the data store.

## Extended description
Some authentication mechanisms rely on the client to generate the hash for a password, possibly to reduce load on the server or avoid sending the password across the network. However, when the client is used to generate the hash, an attacker can bypass the authentication by obtaining a copy of the hash, e.g. by using SQL injection to compromise a database of authentication credentials, or by exploiting an information exposure. The attacker could then use a modified client to replay the stolen hash without having knowledge of the original password. As a result, the server-side comparison against a client-side hash does not provide any more security than the use of passwords without hashing.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Related attack patterns (CAPEC)
- [CAPEC-644](https://capec.mitre.org/data/definitions/644.html)
- [CAPEC-652](https://capec.mitre.org/data/definitions/652.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-602 (PeerOf)

## Observed examples (CVE)
- **CVE-2009-1283**: Product performs authentication with user-supplied password hashes that can be obtained from a separate SQL injection vulnerability (CVE-2009-1282).
- **CVE-2005-3435**: Product allows attackers to bypass authentication by obtaining the password hash for another user and specifying the hash in the pwd argument.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/836.html
