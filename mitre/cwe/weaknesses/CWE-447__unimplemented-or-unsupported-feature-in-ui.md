---
cwe_id: CWE-447
name: Unimplemented or Unsupported Feature in UI
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/447.html
tags: [mitre-cwe, weakness, CWE-447]
---

# CWE-447 - Unimplemented or Unsupported Feature in UI

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-447](https://cwe.mitre.org/data/definitions/447.html)

## Description
A UI function for a security feature appears to be supported and gives feedback to the user that suggests that it is supported, but the underlying functionality is not implemented.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Other**: Varies by Context, Unexpected State

## Potential mitigations
- **Testing**: Perform functionality testing before deploying the application.

## Related weaknesses
- CWE-446 (ChildOf)
- CWE-671 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-0127**: GUI configuration tool does not enable a security option when a checkbox is selected, although that option is honored when manually set in the configuration file.
- **CVE-2001-0863**: Router does not implement a specific keyword when it is used in an ACL, allowing filter bypass.
- **CVE-2001-0865**: Router does not implement a specific keyword when it is used in an ACL, allowing filter bypass.
- **CVE-2004-0979**: Web browser does not properly modify security setting when the user sets it.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/447.html
