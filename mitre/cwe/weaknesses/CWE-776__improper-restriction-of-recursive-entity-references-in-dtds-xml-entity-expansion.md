---
cwe_id: CWE-776
name: Improper Restriction of Recursive Entity References in DTDs ('XML Entity Expansion')
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, XML, Not Technology-Specific]
related_capec: [CAPEC-197]
url: https://cwe.mitre.org/data/definitions/776.html
tags: [mitre-cwe, weakness, CWE-776]
---

# CWE-776 - Improper Restriction of Recursive Entity References in DTDs ('XML Entity Expansion')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-776](https://cwe.mitre.org/data/definitions/776.html)

## Description
The product uses XML documents and allows their structure to be defined with a Document Type Definition (DTD), but it does not properly control the number of recursive definitions of entities.

## Extended description
If the DTD contains a large number of nested or recursive entities, this can lead to explosive growth of data when parsed, causing a denial of service.

## Applicable platforms / languages
Not Language-Specific, XML, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (Other)

## Potential mitigations
- **Operation**: If possible, prohibit the use of DTDs or use an XML parser that limits the expansion of recursive DTD entities.
- **Implementation**: Before parsing XML files with associated DTDs, scan for recursive entity declarations and do not continue parsing potentially explosive content.

## Related attack patterns (CAPEC)
- [CAPEC-197](https://capec.mitre.org/data/definitions/197.html)

## Related weaknesses
- CWE-674 (ChildOf)
- CWE-674 (ChildOf)
- CWE-405 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-3281**: XEE in XML-parsing library.
- **CVE-2011-3288**: XML bomb / XEE in enterprise communication product.
- **CVE-2011-1755**: "Billion laughs" attack in XMPP server daemon.
- **CVE-2009-1955**: XML bomb in web server module
- **CVE-2003-1564**: Parsing library allows XML bomb

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/776.html
