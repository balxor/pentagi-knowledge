---
cwe_id: CWE-611
name: Improper Restriction of XML External Entity Reference
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, XML, Not Technology-Specific, Web Based]
related_capec: [CAPEC-221]
url: https://cwe.mitre.org/data/definitions/611.html
tags: [mitre-cwe, weakness, CWE-611]
---

# CWE-611 - Improper Restriction of XML External Entity Reference

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-611](https://cwe.mitre.org/data/definitions/611.html)

## Description
The product processes an XML document that can contain XML entities with URIs that resolve to documents outside of the intended sphere of control, causing the product to embed incorrect documents into its output.

## Applicable platforms / languages
Not Language-Specific, XML, Not Technology-Specific, Web Based

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories
- **Integrity**: Bypass Protection Mechanism
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)

## Potential mitigations
- **Implementation, System Configuration**: Many XML parsers and validators can be configured to disable external entity expansion.

## Related attack patterns (CAPEC)
- [CAPEC-221](https://capec.mitre.org/data/definitions/221.html)

## Related weaknesses
- CWE-610 (ChildOf)
- CWE-610 (ChildOf)
- CWE-441 (PeerOf)

## Observed examples (CVE)
- **CVE-2022-42745**: Recruiter software allows reading arbitrary files using XXE
- **CVE-2005-1306**: A browser control can allow remote attackers to determine the existence of files via Javascript containing XML script.
- **CVE-2012-5656**: XXE during SVG image conversion
- **CVE-2012-2239**: XXE in PHP application allows reading the application's configuration file.
- **CVE-2012-3489**: XXE in database server
- **CVE-2012-4399**: XXE in rapid web application development framework allows reading arbitrary files.
- **CVE-2012-3363**: XXE via XML-RPC request.
- **CVE-2012-0037**: XXE in office document product using RDF.
- **CVE-2011-4107**: XXE in web-based administration tool for database.
- **CVE-2010-3322**: XXE in product that performs large-scale data analysis.
- **CVE-2009-1699**: XXE in XSL stylesheet functionality in a common library used by some web browsers.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/611.html
