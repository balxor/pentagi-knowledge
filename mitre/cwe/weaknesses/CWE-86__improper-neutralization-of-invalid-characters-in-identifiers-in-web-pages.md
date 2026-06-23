---
cwe_id: CWE-86
name: Improper Neutralization of Invalid Characters in Identifiers in Web Pages
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-247, CAPEC-73, CAPEC-85]
url: https://cwe.mitre.org/data/definitions/86.html
tags: [mitre-cwe, weakness, CWE-86]
---

# CWE-86 - Improper Neutralization of Invalid Characters in Identifiers in Web Pages

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-86](https://cwe.mitre.org/data/definitions/86.html)

## Description
The product does not neutralize or incorrectly neutralizes invalid characters or byte sequences in the middle of tag names, URI schemes, and other identifiers.

## Extended description
Some web browsers may remove these sequences, resulting in output that may have unintended control implications. For example, the product may attempt to remove a "javascript:" URI scheme, but a "java%00script:" URI may bypass this check and still be rendered as active javascript by some browsers, allowing XSS or other attacks.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability**: Read Application Data, Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: Use and specify an output encoding that can be handled by the downstream component that is reading the output. Common encodings include ISO-8859-1, UTF-7, and UTF-8. When an encoding is not specified, a downstream component may choose a different encoding, either by assuming a default encoding or automatically inferring which encoding is being used, which can be erroneous. When the encodings are inconsistent, the downstream component might treat some character or byte sequences as special, even if they are not special in the original encoding. Attackers might then be able to exploit this discrepancy and conduct injection attacks; they even might be able to bypass protection mechanisms that assume the original encoding is also being used by the downstream component. The problem of inconsistent output encodings often arises in web pages. If an encoding is not specified in an HTTP header, web browsers often guess about which encoding is being used. This can open up the browser to subtle XSS attacks.
- **Implementation**: To help mitigate XSS attacks against the user's session cookie, set the session cookie to be HttpOnly. In browsers that support the HttpOnly feature (such as more recent versions of Internet Explorer and Firefox), this attribute can prevent the user's session cookie from being accessible to malicious client-side scripts that use document.cookie. This is not a complete solution, since HttpOnly is not supported by all browsers. More importantly, XmlHttpRequest and other powerful browser technologies provide read access to HTTP headers, including the Set-Cookie header in which the HttpOnly flag is set.

## Related attack patterns (CAPEC)
- [CAPEC-247](https://capec.mitre.org/data/definitions/247.html)
- [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
- [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)

## Related weaknesses
- CWE-79 (ChildOf)
- CWE-184 (PeerOf)
- CWE-436 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-0595**: XSS filter doesn't filter null characters before looking for dangerous tags, which are ignored by web browsers. Multiple Interpretation Error (MIE) and validate-before-cleanse.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/86.html
