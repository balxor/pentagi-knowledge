---
cwe_id: CWE-113
name: Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Request/Response Splitting')
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-105, CAPEC-31, CAPEC-34, CAPEC-85]
url: https://cwe.mitre.org/data/definitions/113.html
tags: [mitre-cwe, weakness, CWE-113]
---

# CWE-113 - Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Request/Response Splitting')

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-113](https://cwe.mitre.org/data/definitions/113.html)

## Description
The product receives data from an HTTP agent/component (e.g., web server, proxy, browser, etc.), but it does not neutralize or incorrectly neutralizes CR and LF characters before the data is included in outgoing HTTP headers.

## Extended description
HTTP agents or components may include a web server, load balancer, reverse proxy, web caching proxy, application firewall, web browser, etc. Regardless of the role, they are expected to maintain coherent, consistent HTTP communication state across all components. However, including unexpected data in an HTTP header allows an attacker to specify the entirety of the HTTP message that is rendered by the client HTTP agent (e.g., web browser) or back-end HTTP agent (e.g., web server), whether the message is part of a request or a response. When an HTTP request contains unexpected CR and LF characters, the server may respond with an output stream that is interpreted as "splitting" the stream into two different HTTP messages instead of one. CR is carriage return, also given by %0d or \r, and LF is line feed, also given by %0a or \n. In addition to CR and LF characters, other valid/RFC compliant special characters and unique character encodings can be utilized, such as HT (horizontal tab, also given by %09 or \t) and SP (space, also given as + sign or %20). These types of unvalidated and unexpected data in HTTP message headers allow an attacker to control the second "split" message to mount attacks such as server-side request forgery, cross-site scripting, and cache poisoning attacks. HTTP response splitting weaknesses may be present when: Data enters a web application through an untrusted source, most frequently an HTTP request. The data is included in an HTTP response header sent to a web user without neutralizing malicious characters that can be interpreted as separator characters for headers.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Integrity, Access Control**: Modify Application Data, Gain Privileges or Assume Identity

## Potential mitigations
- **Implementation**: Construct HTTP headers very carefully, avoiding the use of non-validated input data.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. If an input does not strictly conform to specifications, reject it or transform it into something that conforms. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Use and specify an output encoding that can be handled by the downstream component that is reading the output. Common encodings include ISO-8859-1, UTF-7, and UTF-8. When an encoding is not specified, a downstream component may choose a different encoding, either by assuming a default encoding or automatically inferring which encoding is being used, which can be erroneous. When the encodings are inconsistent, the downstream component might treat some character or byte sequences as special, even if they are not special in the original encoding. Attackers might then be able to exploit this discrepancy and conduct injection attacks; they even might be able to bypass protection mechanisms that assume the original encoding is also being used by the downstream component.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-105](https://capec.mitre.org/data/definitions/105.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-34](https://capec.mitre.org/data/definitions/34.html)
- [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)

## Related weaknesses
- CWE-93 (ChildOf)
- CWE-79 (CanPrecede)
- CWE-20 (ChildOf)
- CWE-436 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-15811**: Chain: Proxy uses a substring search instead of parsing the Transfer-Encoding header (CWE-697), allowing request splitting (CWE-113) and cache poisoning
- **CVE-2021-41084**: Scala-based HTTP interface allows request splitting and response splitting through header names, header values, status reasons, and URIs
- **CVE-2018-12116**: Javascript-based framework allows request splitting through a path option of an HTTP request
- **CVE-2004-2146**: Application accepts CRLF in an object ID, allowing HTTP response splitting.
- **CVE-2004-1656**: Shopping cart allows HTTP response splitting to perform HTML injection via CRLF in a parameter for a url
- **CVE-2005-2060**: Bulletin board allows response splitting via CRLF in parameter.
- **CVE-2004-2512**: Response splitting via CRLF in PHPSESSID.
- **CVE-2005-1951**: e-commerce app allows HTTP response splitting using CRLF in object id parameters

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/113.html
