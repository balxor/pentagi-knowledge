---
cwe_id: CWE-425
name: Direct Request ('Forced Browsing')
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-127, CAPEC-143, CAPEC-144, CAPEC-668, CAPEC-87]
url: https://cwe.mitre.org/data/definitions/425.html
tags: [mitre-cwe, weakness, CWE-425]
---

# CWE-425 - Direct Request ('Forced Browsing')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-425](https://cwe.mitre.org/data/definitions/425.html)

## Description
The web application does not adequately enforce appropriate authorization on all restricted URLs, scripts, or files.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Read Application Data, Modify Application Data, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Operation**: Apply appropriate access control authorizations for each access to all restricted URLs, scripts or files.
- **Architecture and Design**: Consider using MVC based frameworks such as Struts.

## Related attack patterns (CAPEC)
- [CAPEC-127](https://capec.mitre.org/data/definitions/127.html)
- [CAPEC-143](https://capec.mitre.org/data/definitions/143.html)
- [CAPEC-144](https://capec.mitre.org/data/definitions/144.html)
- [CAPEC-668](https://capec.mitre.org/data/definitions/668.html)
- [CAPEC-87](https://capec.mitre.org/data/definitions/87.html)

## Related weaknesses
- CWE-862 (ChildOf)
- CWE-862 (ChildOf)
- CWE-288 (ChildOf)
- CWE-424 (ChildOf)
- CWE-471 (CanPrecede)
- CWE-98 (CanPrecede)

## Observed examples (CVE)
- **CVE-2022-29238**: Access-control setting in web-based document collaboration tool is not properly implemented by the code, which prevents listing hidden directories but does not prevent direct requests to files in those directories.
- **CVE-2004-2144**: Bypass authentication via direct request.
- **CVE-2005-1892**: Infinite loop or infoleak triggered by direct requests.
- **CVE-2004-2257**: Bypass auth/auth via direct request.
- **CVE-2005-1688**: Direct request leads to infoleak by error.
- **CVE-2005-1697**: Direct request leads to infoleak by error.
- **CVE-2005-1698**: Direct request leads to infoleak by error.
- **CVE-2005-1685**: Authentication bypass via direct request.
- **CVE-2005-1827**: Authentication bypass via direct request.
- **CVE-2005-1654**: Authorization bypass using direct request.
- **CVE-2005-1668**: Access privileged functionality using direct request.
- **CVE-2002-1798**: Upload arbitrary files via direct request.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/425.html
