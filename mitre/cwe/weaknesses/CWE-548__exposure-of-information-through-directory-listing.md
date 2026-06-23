---
cwe_id: CWE-548
name: Exposure of Information Through Directory Listing
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/548.html
tags: [mitre-cwe, weakness, CWE-548]
---

# CWE-548 - Exposure of Information Through Directory Listing

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-548](https://cwe.mitre.org/data/definitions/548.html)

## Description
The product inappropriately exposes a directory listing with an index of all the resources located inside of the directory.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Files or Directories

## Potential mitigations
- **Architecture and Design, System Configuration**: Recommendations include restricting access to important directories or files by adopting a need to know requirement for both the document and server root, and turning off features such as Automatic Directory Listings that could expose private files and provide information that could be utilized by an attacker when formulating or conducting an attack.

## Related weaknesses
- CWE-497 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-37599**: web interface is configured to allow directory listing of a module path

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/548.html
