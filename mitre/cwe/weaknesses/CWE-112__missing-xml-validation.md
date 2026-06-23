---
cwe_id: CWE-112
name: Missing XML Validation
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-230, CAPEC-231]
url: https://cwe.mitre.org/data/definitions/112.html
tags: [mitre-cwe, weakness, CWE-112]
---

# CWE-112 - Missing XML Validation

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-112](https://cwe.mitre.org/data/definitions/112.html)

## Description
The product accepts XML from an untrusted source but does not validate the XML against the proper schema.

## Extended description
Most successful attacks begin with a violation of the programmer's assumptions. By accepting an XML document without validating it against a DTD or XML schema, the programmer leaves a door open for attackers to provide unexpected, unreasonable, or malicious input.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Architecture and Design**: Always validate XML input against a known XML Schema or DTD. It is not possible for an XML parser to validate all aspects of a document's content because a parser cannot understand the complete semantics of the data. However, a parser can do a complete and thorough job of checking the document's structure and therefore guarantee to the code that processes the document that the content is well-formed.

## Related attack patterns (CAPEC)
- [CAPEC-230](https://capec.mitre.org/data/definitions/230.html)
- [CAPEC-231](https://capec.mitre.org/data/definitions/231.html)

## Related weaknesses
- CWE-1286 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/112.html
