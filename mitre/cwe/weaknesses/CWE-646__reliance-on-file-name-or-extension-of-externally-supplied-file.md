---
cwe_id: CWE-646
name: Reliance on File Name or Extension of Externally-Supplied File
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Server]
related_capec: [CAPEC-209]
url: https://cwe.mitre.org/data/definitions/646.html
tags: [mitre-cwe, weakness, CWE-646]
---

# CWE-646 - Reliance on File Name or Extension of Externally-Supplied File

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-646](https://cwe.mitre.org/data/definitions/646.html)

## Description
The product allows a file to be uploaded, but it relies on the file name or extension of the file to determine the appropriate behaviors. This could be used by attackers to cause the file to be misclassified and processed in a dangerous fashion.

## Extended description
An application might use the file name or extension of a user-supplied file to determine the proper course of action, such as selecting the correct process to which control should be passed, deciding what data should be made available, or what resources should be allocated. If the attacker can cause the code to misclassify the supplied file, then the wrong action could occur. For example, an attacker could supply a file that ends in a ".php.gif" extension that appears to be a GIF image, but would be processed as PHP code. In extreme cases, code execution is possible, but the attacker could also cause exhaustion of resources, denial of service, exposure of debug or system data (including application source code), or being bound to a particular server side process. This weakness may be due to a vulnerability in any of the technologies used by the web and application servers, due to misconfiguration, or resultant from another flaw in the application itself.

## Applicable platforms / languages
Not Language-Specific, Web Server

## Common consequences
- **Confidentiality**: Read Application Data
- **Availability**: DoS: Crash, Exit, or Restart
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Make decisions on the server side based on file content and not on file name or extension.

## Related attack patterns (CAPEC)
- [CAPEC-209](https://capec.mitre.org/data/definitions/209.html)

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-434 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/646.html
