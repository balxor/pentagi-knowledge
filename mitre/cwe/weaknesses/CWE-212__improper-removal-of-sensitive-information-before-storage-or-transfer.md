---
cwe_id: CWE-212
name: Improper Removal of Sensitive Information Before Storage or Transfer
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-168]
url: https://cwe.mitre.org/data/definitions/212.html
tags: [mitre-cwe, weakness, CWE-212]
---

# CWE-212 - Improper Removal of Sensitive Information Before Storage or Transfer

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-212](https://cwe.mitre.org/data/definitions/212.html)

## Description
The product stores, transfers, or shares a resource that contains sensitive information, but it does not properly remove that information before the product makes the resource available to unauthorized actors.

## Extended description
Resources that may contain sensitive data include documents, packets, messages, databases, etc. While this data may be useful to an individual user or small set of users who share the resource, it may need to be removed before the resource can be shared outside of the trusted group. The process of removal is sometimes called cleansing or scrubbing. For example, a product for editing documents might not remove sensitive data such as reviewer comments or the local pathname where the document is stored. Or, a proxy might not remove an internal IP address from headers before making an outgoing request to an Internet site.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Files or Directories, Read Application Data

## Potential mitigations
- **Requirements**: Clearly specify which information should be regarded as private or sensitive, and require that the product offers functionality that allows the user to cleanse the sensitive information from the resource before it is published or exported to other parties.
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- **Implementation, Operation**: Some tools can automatically analyze documents to redact, strip, or "sanitize" private information, although some human review might be necessary. Tools may vary in terms of which document formats can be processed. When calling an external program to automatically generate or convert documents, invoke the program with any available options that avoid generating sensitive metadata. Some formats have well-defined fields that could contain private data, such as Exchangeable image file format (Exif), which can contain potentially sensitive metadata such as geolocation, date, and time [REF-1515] [REF-1516].
- **Implementation**: Use naming conventions and strong types to make it easier to spot when sensitive data is being used. When creating structures, objects, or other complex entities, separate the sensitive and non-sensitive data as much as possible.
- **Implementation**: Avoid errors related to improper resource shutdown or release (CWE-404), which may leave the sensitive data within the resource if it is in an incomplete state.

## Related attack patterns (CAPEC)
- [CAPEC-168](https://capec.mitre.org/data/definitions/168.html)

## Related weaknesses
- CWE-669 (ChildOf)
- CWE-669 (ChildOf)
- CWE-201 (CanPrecede)

## Observed examples (CVE)
- **CVE-2023-1974**: product does not remove EXIF data from images, which can include GPS coordinates
- **CVE-2020-26220**: Customer relationship management (CRM) product does not strip Exif data from images
- **CVE-2019-3733**: Cryptography library does not clear heap memory before release
- **CVE-2005-0406**: Some image editors modify a JPEG image, but the original EXIF thumbnail image is left intact within the JPEG. (Also an interaction error).
- **CVE-2002-0704**: NAT feature in firewall leaks internal IP addresses in ICMP error messages.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/212.html
