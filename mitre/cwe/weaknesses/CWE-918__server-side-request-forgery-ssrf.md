---
cwe_id: CWE-918
name: Server-Side Request Forgery (SSRF)
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Web Based, AI/ML, Web Server]
related_capec: [CAPEC-664]
url: https://cwe.mitre.org/data/definitions/918.html
tags: [mitre-cwe, weakness, CWE-918]
---

# CWE-918 - Server-Side Request Forgery (SSRF)

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-918](https://cwe.mitre.org/data/definitions/918.html)

## Description
The web server receives a URL or similar request from an upstream component and retrieves the contents of this URL, but it does not sufficiently ensure that the request is being sent to the expected destination.

## Applicable platforms / languages
Not Language-Specific, Web Based, AI/ML, Web Server

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Execute Unauthorized Code or Commands
- **Access Control**: Bypass Protection Mechanism

## Related attack patterns (CAPEC)
- [CAPEC-664](https://capec.mitre.org/data/definitions/664.html)

## Related weaknesses
- CWE-441 (ChildOf)
- CWE-610 (ChildOf)

## Observed examples (CVE)
- **CVE-2026-33626**: SSRF in LLM toolkit accesses arbitrary URLs for images, as exploited in the wild in April 2026 to conduct port scanning [REF-1519]
- **CVE-2024-3095**: SSRF in LLM application development framework because the URL retriever allows connections to local addresses using a crafted Location header
- **CVE-2023-32786**: Chain: LLM integration framework has prompt injection (CWE-1427) that allows an attacker to force the service to retrieve data from an arbitrary URL, essentially providing SSRF (CWE-918) and potentially injecting content into downstream tasks.
- **CVE-2021-26855**: Server Side Request Forgery (SSRF) in mail server, as exploited in the wild per CISA KEV.
- **CVE-2021-21973**: Server Side Request Forgery in cloud platform, as exploited in the wild per CISA KEV.
- **CVE-2016-4029**: Chain: incorrect validation of intended decimal-based IP address format (CWE-1286) enables parsing of octal or hexadecimal formats (CWE-1389), allowing bypass of an SSRF protection mechanism (CWE-918).
- **CVE-2002-1484**: Web server allows attackers to request a URL from another server, including other ports, which allows proxied scanning.
- **CVE-2004-2061**: CGI script accepts and retrieves incoming URLs.
- **CVE-2010-1637**: Web-based mail program allows internal network scanning using a modified POP3 port number.
- **CVE-2009-0037**: URL-downloading library automatically follows redirects to file:// and scp:// URLs

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/918.html
