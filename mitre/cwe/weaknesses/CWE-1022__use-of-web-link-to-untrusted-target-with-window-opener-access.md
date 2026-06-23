---
cwe_id: CWE-1022
name: Use of Web Link to Untrusted Target with window.opener Access
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, JavaScript, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1022.html
tags: [mitre-cwe, weakness, CWE-1022]
---

# CWE-1022 - Use of Web Link to Untrusted Target with window.opener Access

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1022](https://cwe.mitre.org/data/definitions/1022.html)

## Description
The web application produces links to untrusted external sites outside of its sphere of control, but it does not properly prevent the external site from modifying security-critical properties of the window.opener object, such as the location property.

## Extended description
When a user clicks a link to an external site ("target"), the target="_blank" attribute causes the target site's contents to be opened in a new window or tab, which runs in the same process as the original page. The window.opener object records information about the original page that offered the link. If an attacker can run script on the target page, then they could read or modify certain properties of the window.opener object, including the location property - even if the original and target site are not the same origin. An attacker can modify the location property to automatically redirect the user to a malicious site, e.g. as part of a phishing attack. Since this redirect happens in the original window/tab - which is not necessarily visible, since the browser is focusing the display on the new target page - the user might not notice any suspicious redirection.

## Applicable platforms / languages
Not Language-Specific, JavaScript, Web Based, Web Server

## Common consequences
- **Confidentiality**: Alter Execution Logic

## Potential mitigations
- **Architecture and Design**: Specify in the design that any linked external document must not be granted access to the location object of the calling page.
- **Implementation**: When creating a link to an external document using the <a> tag with a defined target, for example "_blank" or a named frame, provide the rel attribute with a value "noopener noreferrer". If opening the external document in a new window via javascript, then reset the opener by setting it equal to null.
- **Implementation**: Do not use "_blank" targets. However, this can affect the usability of the application.

## Related weaknesses
- CWE-266 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-4927**: Library software does not use rel: "noopener noreferrer" setting, allowing tabnabbing attacks to redirect to a malicious page

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1022.html
