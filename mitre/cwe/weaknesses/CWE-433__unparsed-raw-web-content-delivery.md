---
cwe_id: CWE-433
name: Unparsed Raw Web Content Delivery
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/433.html
tags: [mitre-cwe, weakness, CWE-433]
---

# CWE-433 - Unparsed Raw Web Content Delivery

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-433](https://cwe.mitre.org/data/definitions/433.html)

## Description
The product stores raw content or supporting code under the web document root with an extension that is not specifically handled by the server.

## Extended description
If code is stored in a file with an extension such as ".inc" or ".pl", and the web server does not have a handler for that extension, then the server will likely send the contents of the file directly to the requester without the pre-processing that was expected. When that file contains sensitive information such as database credentials, this may allow the attacker to compromise the application or associated components.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Perform a type check before interpreting files.
- **Architecture and Design**: Do not store sensitive information in files which may be misinterpreted.

## Related weaknesses
- CWE-219 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1886**: ".inc" file stored under web document root and returned unparsed by the server
- **CVE-2002-2065**: ".inc" file stored under web document root and returned unparsed by the server
- **CVE-2005-2029**: ".inc" file stored under web document root and returned unparsed by the server
- **CVE-2001-0330**: direct request to .pl file leaves it unparsed
- **CVE-2002-0614**: .inc file
- **CVE-2004-2353**: unparsed config.conf file
- **CVE-2007-3365**: Chain: uppercase file extensions causes web server to return script source code instead of executing the script.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/433.html
