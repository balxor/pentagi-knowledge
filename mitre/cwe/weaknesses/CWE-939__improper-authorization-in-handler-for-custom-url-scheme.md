---
cwe_id: CWE-939
name: Improper Authorization in Handler for Custom URL Scheme
type: weakness
abstraction: Base
status: Incomplete
languages: [Mobile]
related_capec: []
url: https://cwe.mitre.org/data/definitions/939.html
tags: [mitre-cwe, weakness, CWE-939]
---

# CWE-939 - Improper Authorization in Handler for Custom URL Scheme

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-939](https://cwe.mitre.org/data/definitions/939.html)

## Description
The product uses a handler for a custom URL scheme, but it does not properly restrict which actors can invoke the handler using the scheme.

## Extended description
Mobile platforms and other architectures allow the use of custom URL schemes to facilitate communication between applications. In the case of iOS, this is the only method to do inter-application communication. The implementation is at the developer's discretion which may open security flaws in the application. An example could be potentially dangerous functionality such as modifying files through a custom URL scheme.

## Applicable platforms / languages
Mobile

## Common consequences
- **Access Control, Other**: Gain Privileges or Assume Identity, Varies by Context, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Utilize a user prompt pop-up to authorize potentially harmful actions such as those modifying data or dealing with sensitive information. When designing functionality of actions in the URL scheme, consider whether the action should be accessible to all mobile applications, or if an allowlist of applications to interface with is appropriate.

## Related weaknesses
- CWE-862 (ChildOf)
- CWE-940 (ChildOf)

## Observed examples (CVE)
- **CVE-2013-5725**: URL scheme has action replace which requires no user prompt and allows remote attackers to perform undesired actions.
- **CVE-2013-5726**: URL scheme has action follow and favorite which allows remote attackers to force user to perform undesired actions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/939.html
