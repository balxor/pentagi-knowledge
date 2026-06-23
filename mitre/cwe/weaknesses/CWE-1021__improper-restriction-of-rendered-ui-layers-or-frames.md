---
cwe_id: CWE-1021
name: Improper Restriction of Rendered UI Layers or Frames
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: [CAPEC-103, CAPEC-181, CAPEC-222, CAPEC-504, CAPEC-506, CAPEC-587, CAPEC-654]
url: https://cwe.mitre.org/data/definitions/1021.html
tags: [mitre-cwe, weakness, CWE-1021]
---

# CWE-1021 - Improper Restriction of Rendered UI Layers or Frames

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1021](https://cwe.mitre.org/data/definitions/1021.html)

## Description
The web application does not restrict or incorrectly restricts frame objects or UI layers that belong to another application or domain.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Application Data, Modify Application Data

## Potential mitigations
- **Implementation**: The use of X-Frame-Options allows developers of web content to restrict the usage of their application within the form of overlays, frames, or iFrames. The developer can indicate from which domains can frame the content. The concept of X-Frame-Options is well documented, but implementation of this protection mechanism is in development to cover gaps. There is a need for allowing frames from multiple domains.
- **Implementation**: A developer can use a "frame-breaker" script in each page that should not be framed. This is very helpful for legacy browsers that do not support X-Frame-Options security feature previously mentioned. It is also important to note that this tactic has been circumvented or bypassed. Improper usage of frames can persist in the web application through nested frames. The "frame-breaking" script does not intuitively account for multiple nested frames that can be presented to the user.
- **Implementation**: This defense-in-depth technique can be used to prevent the improper usage of frames in web applications. It prioritizes the valid sources of data to be loaded into the application through the usage of declarative policies. Based on which implementation of Content Security Policy is in use, the developer should use the "frame-ancestors" directive or the "frame-src" directive to mitigate this weakness. Both directives allow for the placement of restrictions when it comes to allowing embedded content.
- **Implementation**: In addition to frames or iframes as previously mentioned, the web application is expected to place restrictions on whether it is allowed to be rendered within objects, embed, or applet elements.

## Related attack patterns (CAPEC)
- [CAPEC-103](https://capec.mitre.org/data/definitions/103.html)
- [CAPEC-181](https://capec.mitre.org/data/definitions/181.html)
- [CAPEC-222](https://capec.mitre.org/data/definitions/222.html)
- [CAPEC-504](https://capec.mitre.org/data/definitions/504.html)
- [CAPEC-506](https://capec.mitre.org/data/definitions/506.html)
- [CAPEC-587](https://capec.mitre.org/data/definitions/587.html)
- [CAPEC-654](https://capec.mitre.org/data/definitions/654.html)

## Related weaknesses
- CWE-441 (ChildOf)
- CWE-610 (ChildOf)
- CWE-451 (ChildOf)

## Observed examples (CVE)
- **CVE-2017-7440**: E-mail preview feature in a desktop application allows clickjacking attacks via a crafted e-mail message
- **CVE-2017-5697**: Hardware/firmware product has insufficient clickjacking protection in its web user interface
- **CVE-2017-4015**: Clickjacking in data-loss prevention product via HTTP response header.
- **CVE-2016-2496**: Tapjacking in permission dialog for mobile OS allows access of private storage using a partially-overlapping window.
- **CVE-2015-1241**: Tapjacking in web browser related to page navigation and touch/gesture events.
- **CVE-2017-0492**: System UI in mobile OS allows a malicious application to create a UI overlay of the entire screen to gain privileges.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1021.html
