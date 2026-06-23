---
cwe_id: CWE-323
name: Reusing a Nonce, Key Pair in Encryption
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/323.html
tags: [mitre-cwe, weakness, CWE-323]
---

# CWE-323 - Reusing a Nonce, Key Pair in Encryption

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-323](https://cwe.mitre.org/data/definitions/323.html)

## Description
Nonces should be used for the present occasion and only once.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Implementation**: Refuse to reuse nonce values.
- **Implementation**: Use techniques such as requiring incrementing, time based and/or challenge response to assure uniqueness of nonces.

## Related weaknesses
- CWE-344 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-36289**: social networking app reuses a nonce/key pair, allowing MITM attackers to manipulate direct messages
- **CVE-2024-21530**: Rust package reuses a nonce/key pair when an object is cloned, which resets the random number generation

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/323.html
