---
cwe_id: CWE-294
name: Authentication Bypass by Capture-replay
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-102, CAPEC-509, CAPEC-555, CAPEC-561, CAPEC-60, CAPEC-644, CAPEC-645, CAPEC-652, CAPEC-701, CAPEC-94]
url: https://cwe.mitre.org/data/definitions/294.html
tags: [mitre-cwe, weakness, CWE-294]
---

# CWE-294 - Authentication Bypass by Capture-replay

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-294](https://cwe.mitre.org/data/definitions/294.html)

## Description
A capture-replay flaw exists when the design of the product makes it possible for a malicious user to sniff network traffic and bypass authentication by replaying it to the server in question to the same effect as the original message (or with minor changes).

## Extended description
Capture-replay attacks are common and can be difficult to defeat without cryptography. They are a subset of network injection attacks that rely on observing previously-sent valid commands, then changing them slightly if necessary and resending the same commands to the server.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Utilize some sequence or time stamping functionality along with a checksum which takes this into account in order to ensure that messages can be parsed only once.
- **Architecture and Design**: Since any attacker who can listen to traffic can see sequence numbers, it is necessary to sign messages with some kind of cryptography to ensure that sequence numbers are not simply doctored along with content.

## Related attack patterns (CAPEC)
- [CAPEC-102](https://capec.mitre.org/data/definitions/102.html)
- [CAPEC-509](https://capec.mitre.org/data/definitions/509.html)
- [CAPEC-555](https://capec.mitre.org/data/definitions/555.html)
- [CAPEC-561](https://capec.mitre.org/data/definitions/561.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
- [CAPEC-644](https://capec.mitre.org/data/definitions/644.html)
- [CAPEC-645](https://capec.mitre.org/data/definitions/645.html)
- [CAPEC-652](https://capec.mitre.org/data/definitions/652.html)
- [CAPEC-701](https://capec.mitre.org/data/definitions/701.html)
- [CAPEC-94](https://capec.mitre.org/data/definitions/94.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-287 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-3435**: product authentication succeeds if user-provided MD5 hash matches the hash in its database; this can be subjected to replay attacks.
- **CVE-2007-4961**: Chain: cleartext transmission of the MD5 hash of password (CWE-319) enables attacks against a server that is susceptible to replay (CWE-294).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/294.html
