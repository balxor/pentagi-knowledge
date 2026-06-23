---
cwe_id: CWE-669
name: Incorrect Resource Transfer Between Spheres
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/669.html
tags: [mitre-cwe, weakness, CWE-669]
---

# CWE-669 - Incorrect Resource Transfer Between Spheres

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-669](https://cwe.mitre.org/data/definitions/669.html)

## Description
The product does not properly transfer a resource/behavior to another sphere, or improperly imports a resource/behavior from another sphere, in a manner that provides unintended control over that resource.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data, Unexpected State

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-22909**: Chain: router's firmware update procedure uses curl with "-k" (insecure) option that disables certificate validation (CWE-295), allowing adversary-in-the-middle (AITM) compromise with a malicious firmware image (CWE-494).
- **CVE-2023-5227**: PHP-based FAQ management app does not check the MIME type for uploaded images
- **CVE-2005-0406**: Some image editors modify a JPEG image, but the original EXIF thumbnail image is left intact within the JPEG. (Also an interaction error).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/669.html
