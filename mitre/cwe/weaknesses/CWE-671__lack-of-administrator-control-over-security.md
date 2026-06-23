---
cwe_id: CWE-671
name: Lack of Administrator Control over Security
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/671.html
tags: [mitre-cwe, weakness, CWE-671]
---

# CWE-671 - Lack of Administrator Control over Security

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-671](https://cwe.mitre.org/data/definitions/671.html)

## Description
The product uses security features in a way that prevents the product's administrator from tailoring security settings to reflect the environment in which the product is being used. This introduces resultant weaknesses or prevents it from operating at a level of security that is desired by the administrator.

## Extended description
If the product's administrator does not have the ability to manage security-related decisions at all times, then protecting the product from outside threats - including the product's developer - can become impossible. For example, a hard-coded account name and password cannot be changed by the administrator, thus exposing that product to attacks that the administrator can not prevent.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Related weaknesses
- CWE-657 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-29953**: Condition Monitor firmware has a maintenance interface with hard-coded credentials
- **CVE-2000-0127**: GUI configuration tool does not enable a security option when a checkbox is selected, although that option is honored when manually set in the configuration file.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/671.html
