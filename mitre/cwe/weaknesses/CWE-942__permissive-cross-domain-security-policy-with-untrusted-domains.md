---
cwe_id: CWE-942
name: Permissive Cross-domain Security Policy with Untrusted Domains
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/942.html
tags: [mitre-cwe, weakness, CWE-942]
---

# CWE-942 - Permissive Cross-domain Security Policy with Untrusted Domains

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-942](https://cwe.mitre.org/data/definitions/942.html)

## Description
The product uses a web-client protection mechanism such as a Content Security Policy (CSP) or cross-domain policy file, but the policy includes untrusted domains with which the web client is allowed to communicate.

## Extended description
If a cross-domain policy file includes domains that should not be trusted, such as when using wildcards under a high-level domain, then the application could be attacked by these untrusted domains. In many cases, the attack can be launched without the victim even being aware of it.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Read Application Data, Varies by Context

## Potential mitigations
- **Architecture and Design, Operation**: Define a restrictive Content Security Policy [REF-1486] or cross-domain policy file.
- **Architecture and Design, Operation**: Avoid using wildcards in the CSP / cross-domain policy file. Any domain matching the wildcard expression will be implicitly trusted, and can perform two-way interaction with the target server.
- **Architecture and Design, Operation**: For Flash, modify crossdomain.xml to use meta-policy options such as 'master-only' or 'none' to reduce the possibility of an attacker planting extraneous cross-domain policy files on a server.

## Related weaknesses
- CWE-863 (ChildOf)
- CWE-923 (ChildOf)
- CWE-183 (ChildOf)
- CWE-668 (CanPrecede)

## Observed examples (CVE)
- **CVE-2012-2292**: Product has a Silverlight cross-domain policy that does not restrict access to another application, which allows remote attackers to bypass the Same Origin Policy.
- **CVE-2014-2049**: The default Flash Cross Domain policies in a product allows remote attackers to access user files.
- **CVE-2007-6243**: Chain: Adobe Flash Player does not sufficiently restrict the interpretation and usage of cross-domain policy files, which makes it easier for remote attackers to conduct cross-domain and cross-site scripting (XSS) attacks.
- **CVE-2008-4822**: Chain: Adobe Flash Player and earlier does not properly interpret policy files, which allows remote attackers to bypass a non-root domain policy.
- **CVE-2010-3636**: Chain: Adobe Flash Player does not properly handle unspecified encodings during the parsing of a cross-domain policy file, which allows remote web servers to bypass intended access restrictions via unknown vectors.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/942.html
