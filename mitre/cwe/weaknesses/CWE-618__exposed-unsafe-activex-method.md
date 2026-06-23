---
cwe_id: CWE-618
name: Exposed Unsafe ActiveX Method
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/618.html
tags: [mitre-cwe, weakness, CWE-618]
---

# CWE-618 - Exposed Unsafe ActiveX Method

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-618](https://cwe.mitre.org/data/definitions/618.html)

## Description
An ActiveX control is intended for use in a web browser, but it exposes dangerous methods that perform actions that are outside of the browser's security model (e.g. the zone or domain).

## Extended description
ActiveX controls can exercise far greater control over the operating system than typical Java or javascript. Exposed methods can be subject to various vulnerabilities, depending on the implemented behaviors of those methods, and whether input validation is performed on the provided arguments. If there is no integrity checking or origin validation, this method could be invoked by attackers.

## Applicable platforms / languages
Not Language-Specific, Web Based

## Common consequences
- **Other**: Other

## Potential mitigations
- **Implementation**: If you must expose a method, make sure to perform input validation on all arguments, and protect against all possible vulnerabilities.
- **Architecture and Design**: Use code signing, although this does not protect against any weaknesses that are already in the control.
- **Architecture and Design, System Configuration**: Where possible, avoid marking the control as safe for scripting.

## Related weaknesses
- CWE-749 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-1120**: download a file to arbitrary folders.
- **CVE-2006-6838**: control downloads and executes a url in a parameter
- **CVE-2007-0321**: resultant buffer overflow

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/618.html
