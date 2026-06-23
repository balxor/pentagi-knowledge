---
capec_id: CAPEC-201
name: Serialized Data External Linking
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-829]
related_attack: []
url: https://capec.mitre.org/data/definitions/201.html
tags: [mitre-capec, attack-pattern, CAPEC-201]
---

# CAPEC-201 - Serialized Data External Linking

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-201](https://capec.mitre.org/data/definitions/201.html)

## Description
An adversary creates a serialized data file (e.g. XML, YAML, etc...) that contains an external data reference. Because serialized data parsers may not validate documents with external references, there may be no checks on the nature of the reference in the external data. This can allow an adversary to open arbitrary files or connections, which may further lead to the adversary gaining access to information on the system that they would normally be unable to obtain.

## Prerequisites
- The target must follow external data references without validating the validity of the reference target.

## Skills required
- **Low**: To send serialized data messages with maliciously crafted schema.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Survey the target: Using a browser or an automated tool, an adversary records all instances of web services that process requests with serialized data. Techniques Use an automated tool to record all instances of URLs that process requests with serialized data. Use a browser to manually explore the website and analyze how the application processes serialized data requests. Exploit Craft malicious payload: The adversary crafts malicious data message that contains references to sensitive files. Launch an External Linking attack: Send the malicious crafted message containing the reference to a sensitive file to the target URL.

## Mitigations
- Configure the serialized data processor to only retrieve external entities from trusted sources.

## Related weaknesses (CWE)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/201.html
