---
cwe_id: CWE-346
name: Origin Validation Error
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: [CAPEC-111, CAPEC-141, CAPEC-142, CAPEC-160, CAPEC-21, CAPEC-384, CAPEC-385, CAPEC-386, CAPEC-387, CAPEC-388, CAPEC-510, CAPEC-59, CAPEC-60, CAPEC-75, CAPEC-76, CAPEC-89]
url: https://cwe.mitre.org/data/definitions/346.html
tags: [mitre-cwe, weakness, CWE-346]
---

# CWE-346 - Origin Validation Error

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-346](https://cwe.mitre.org/data/definitions/346.html)

## Description
The product does not properly verify that the source of data or communication is valid.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Access Control, Other**: Gain Privileges or Assume Identity, Varies by Context

## Related attack patterns (CAPEC)
- [CAPEC-111](https://capec.mitre.org/data/definitions/111.html)
- [CAPEC-141](https://capec.mitre.org/data/definitions/141.html)
- [CAPEC-142](https://capec.mitre.org/data/definitions/142.html)
- [CAPEC-160](https://capec.mitre.org/data/definitions/160.html)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-384](https://capec.mitre.org/data/definitions/384.html)
- [CAPEC-385](https://capec.mitre.org/data/definitions/385.html)
- [CAPEC-386](https://capec.mitre.org/data/definitions/386.html)
- [CAPEC-387](https://capec.mitre.org/data/definitions/387.html)
- [CAPEC-388](https://capec.mitre.org/data/definitions/388.html)
- [CAPEC-510](https://capec.mitre.org/data/definitions/510.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
- [CAPEC-75](https://capec.mitre.org/data/definitions/75.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)
- [CAPEC-89](https://capec.mitre.org/data/definitions/89.html)

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-345 (ChildOf)
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-1218**: DNS server can accept DNS updates from hosts that it did not query, leading to cache poisoning
- **CVE-2018-6074**: Browser does not set Mark-of-the-Web (MotW) for a downloaded .EXE file if the name is close to the maximum path length, preventing recording of a zone identifier in the filename
- **CVE-2025-0411**: Zip file extraction program does not propagate Mark-of-the-Web (MotW) metadata to files that are extracted from an Internet-downloaded Zip file
- **CVE-2025-46652**: Zip file extraction program does not propagate Mark-of-the-Web (MotW) metadata to files that are extracted from an Internet-downloaded Zip file
- **CVE-2005-0877**: DNS server can accept DNS updates from hosts that it did not query, leading to cache poisoning
- **CVE-2001-1452**: DNS server caches glue records received from non-delegated name servers
- **CVE-2005-2188**: user ID obtained from untrusted source (URL)
- **CVE-2003-0174**: LDAP service does not verify if a particular attribute was set by the LDAP server
- **CVE-1999-1549**: product does not sufficiently distinguish external HTML from internal, potentially dangerous HTML, allowing bypass using special strings in the page title. Overlaps special elements.
- **CVE-2003-0981**: product records the reverse DNS name of a visitor in the logs, allowing spoofing and resultant XSS.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/346.html
