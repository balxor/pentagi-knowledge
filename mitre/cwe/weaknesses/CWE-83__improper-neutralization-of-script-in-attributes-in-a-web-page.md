---
cwe_id: CWE-83
name: Improper Neutralization of Script in Attributes in a Web Page
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-243, CAPEC-244, CAPEC-588]
url: https://cwe.mitre.org/data/definitions/83.html
tags: [mitre-cwe, weakness, CWE-83]
---

# CWE-83 - Improper Neutralization of Script in Attributes in a Web Page

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-83](https://cwe.mitre.org/data/definitions/83.html)

## Description
The product does not neutralize or incorrectly neutralizes "javascript:" or other URIs from dangerous attributes within tags, such as onmouseover, onload, onerror, or style.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability**: Read Application Data, Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: Carefully check each input parameter against a rigorous positive specification (allowlist) defining the specific characters and format allowed. All input should be neutralized, not just parameters that the user is supposed to specify, but all data in the request, including tag attributes, hidden fields, cookies, headers, the URL itself, and so forth. A common mistake that leads to continuing XSS vulnerabilities is to validate only fields that are expected to be redisplayed by the site. We often encounter data from the request that is reflected by the application server or the application that the development team did not anticipate. Also, a field that is not currently reflected may be used by a future developer. Therefore, validating ALL parts of the HTTP request is recommended.
- **Implementation**: Use and specify an output encoding that can be handled by the downstream component that is reading the output. Common encodings include ISO-8859-1, UTF-7, and UTF-8. When an encoding is not specified, a downstream component may choose a different encoding, either by assuming a default encoding or automatically inferring which encoding is being used, which can be erroneous. When the encodings are inconsistent, the downstream component might treat some character or byte sequences as special, even if they are not special in the original encoding. Attackers might then be able to exploit this discrepancy and conduct injection attacks; they even might be able to bypass protection mechanisms that assume the original encoding is also being used by the downstream component. The problem of inconsistent output encodings often arises in web pages. If an encoding is not specified in an HTTP header, web browsers often guess about which encoding is being used. This can open up the browser to subtle XSS attacks.
- **Implementation**: With Struts, write all data from form beans with the bean's filter attribute set to true.
- **Implementation**: To help mitigate XSS attacks against the user's session cookie, set the session cookie to be HttpOnly. In browsers that support the HttpOnly feature (such as more recent versions of Internet Explorer and Firefox), this attribute can prevent the user's session cookie from being accessible to malicious client-side scripts that use document.cookie. This is not a complete solution, since HttpOnly is not supported by all browsers. More importantly, XmlHttpRequest and other powerful browser technologies provide read access to HTTP headers, including the Set-Cookie header in which the HttpOnly flag is set.

## Related attack patterns (CAPEC)
- [CAPEC-243](https://capec.mitre.org/data/definitions/243.html)
- [CAPEC-244](https://capec.mitre.org/data/definitions/244.html)
- [CAPEC-588](https://capec.mitre.org/data/definitions/588.html)

## Related weaknesses
- CWE-79 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-0520**: Bypass filtering of SCRIPT tags using onload in BODY, href in A, BUTTON, INPUT, and others.
- **CVE-2002-1493**: guestbook XSS in STYLE or IMG SRC attributes.
- **CVE-2002-1965**: Javascript in onerror attribute of IMG tag.
- **CVE-2002-1495**: XSS in web-based email product via onmouseover event.
- **CVE-2002-1681**: XSS via script in <P> tag.
- **CVE-2004-1935**: Onload, onmouseover, and other events in an e-mail attachment.
- **CVE-2005-0945**: Onmouseover and onload events in img, link, and mail tags.
- **CVE-2003-1136**: Javascript in onmouseover attribute in e-mail address or URL.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/83.html
