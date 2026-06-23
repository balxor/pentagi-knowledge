---
cwe_id: CWE-610
name: Externally Controlled Reference to a Resource in Another Sphere
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-219]
url: https://cwe.mitre.org/data/definitions/610.html
tags: [mitre-cwe, weakness, CWE-610]
---

# CWE-610 - Externally Controlled Reference to a Resource in Another Sphere

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-610](https://cwe.mitre.org/data/definitions/610.html)

## Description
The product uses an externally controlled name or reference that resolves to a resource that is outside of the intended control sphere.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data
- **Access Control**: Gain Privileges or Assume Identity

## Related attack patterns (CAPEC)
- [CAPEC-219](https://capec.mitre.org/data/definitions/219.html)

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-3032**: An email client does not block loading of remote objects in a nested document.
- **CVE-2022-45918**: Chain: a learning management tool debugger uses external input to locate previous session logs (CWE-73) and does not properly validate the given path (CWE-20), allowing for filesystem path traversal using "../" sequences (CWE-24)
- **CVE-2018-1000613**: Cryptography API uses unsafe reflection when deserializing a private key
- **CVE-2020-11053**: Chain: Go-based Oauth2 reverse proxy can send the authenticated user to another site at the end of the authentication flow. A redirect URL with HTML-encoded whitespace characters can bypass the validation (CWE-1289) to redirect to a malicious site (CWE-601)
- **CVE-2022-42745**: Recruiter software allows reading arbitrary files using XXE
- **CVE-2004-2331**: Database system allows attackers to bypass sandbox restrictions by using the Reflection API.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/610.html
