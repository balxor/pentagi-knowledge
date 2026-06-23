---
cwe_id: CWE-459
name: Incomplete Cleanup
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/459.html
tags: [mitre-cwe, weakness, CWE-459]
---

# CWE-459 - Incomplete Cleanup

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-459](https://cwe.mitre.org/data/definitions/459.html)

## Description
The product does not properly "clean up" and remove temporary or supporting resources after they have been used.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other, Confidentiality, Integrity**: Other, Read Application Data, Modify Application Data, DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design, Implementation**: Temporary files and other supporting resources should be deleted/released immediately after they are no longer needed.

## Related weaknesses
- CWE-404 (ChildOf)
- CWE-404 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-0552**: World-readable temporary file not deleted after use.
- **CVE-2005-2293**: Temporary file not deleted after use, leaking database usernames and passwords.
- **CVE-2002-0788**: Interaction error creates a temporary file that can not be deleted due to strong permissions.
- **CVE-2002-2066**: Alternate data streams for NTFS files are not cleared when files are wiped (alternate channel / infoleak).
- **CVE-2002-2067**: Alternate data streams for NTFS files are not cleared when files are wiped (alternate channel / infoleak).
- **CVE-2002-2068**: Alternate data streams for NTFS files are not cleared when files are wiped (alternate channel / infoleak).
- **CVE-2002-2069**: Alternate data streams for NTFS files are not cleared when files are wiped (alternate channel / infoleak).
- **CVE-2002-2070**: Alternate data streams for NTFS files are not cleared when files are wiped (alternate channel / infoleak).
- **CVE-2005-1744**: Users not logged out when application is restarted after security-relevant changes were made.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/459.html
