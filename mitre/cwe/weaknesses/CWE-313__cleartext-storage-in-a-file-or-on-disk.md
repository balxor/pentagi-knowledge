---
cwe_id: CWE-313
name: Cleartext Storage in a File or on Disk
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/313.html
tags: [mitre-cwe, weakness, CWE-313]
---

# CWE-313 - Cleartext Storage in a File or on Disk

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-313](https://cwe.mitre.org/data/definitions/313.html)

## Description
The product stores sensitive information in cleartext in a file, or on disk.

## Extended description
The sensitive information could be read by attackers with access to the file, or with physical or administrator access to the raw disk. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-312 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-1481**: Cleartext credentials in world-readable file.
- **CVE-2005-1828**: Password in cleartext in config file.
- **CVE-2005-2209**: Password in cleartext in config file.
- **CVE-2002-1696**: Decrypted copy of a message written to disk given a combination of options and when user replies to an encrypted message.
- **CVE-2004-2397**: Cleartext storage of private key and passphrase in log file when user imports the key.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/313.html
