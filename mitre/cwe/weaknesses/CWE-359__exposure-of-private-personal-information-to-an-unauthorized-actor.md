---
cwe_id: CWE-359
name: Exposure of Private Personal Information to an Unauthorized Actor
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Mobile]
related_capec: [CAPEC-464, CAPEC-467, CAPEC-498, CAPEC-508]
url: https://cwe.mitre.org/data/definitions/359.html
tags: [mitre-cwe, weakness, CWE-359]
---

# CWE-359 - Exposure of Private Personal Information to an Unauthorized Actor

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-359](https://cwe.mitre.org/data/definitions/359.html)

## Description
The product does not properly prevent a person's private, personal information from being accessed by actors who either (1) are not explicitly authorized to access the information or (2) do not have the implicit consent of the person about whom the information is collected.

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Requirements**: Identify and consult all relevant regulations for personal privacy. An organization may be required to comply with certain federal and state regulations, depending on its location, the type of business it conducts, and the nature of any private data it handles. Regulations may include Safe Harbor Privacy Framework [REF-340], Gramm-Leach Bliley Act (GLBA) [REF-341], Health Insurance Portability and Accountability Act (HIPAA) [REF-342], General Data Protection Regulation (GDPR) [REF-1047], California Consumer Privacy Act (CCPA) [REF-1048], and others.
- **Architecture and Design**: Carefully evaluate how secure design may interfere with privacy, and vice versa. Security and privacy concerns often seem to compete with each other. From a security perspective, all important operations should be recorded so that any anomalous activity can later be identified. However, when private data is involved, this practice can in fact create risk. Although there are many ways in which private data can be handled unsafely, a common risk stems from misplaced trust. Programmers often trust the operating environment in which a program runs, and therefore believe that it is acceptable store private information on the file system, in the registry, or in other locally-controlled resources. However, even if access to certain resources is restricted, this does not guarantee that the individuals who do have access can be trusted.
- **Implementation, Operation**: Some tools can automatically analyze documents to redact, strip, or "sanitize" private information, although some human review might be necessary. Tools may vary in terms of which document formats can be processed. When calling an external program to automatically generate or convert documents, invoke the program with any available options that avoid generating sensitive metadata. Some formats have well-defined fields that could contain private data, such as Exchangeable image file format (Exif), which can contain potentially sensitive metadata such as geolocation, date, and time [REF-1515] [REF-1516].

## Related attack patterns (CAPEC)
- [CAPEC-464](https://capec.mitre.org/data/definitions/464.html)
- [CAPEC-467](https://capec.mitre.org/data/definitions/467.html)
- [CAPEC-498](https://capec.mitre.org/data/definitions/498.html)
- [CAPEC-508](https://capec.mitre.org/data/definitions/508.html)

## Related weaknesses
- CWE-200 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-29850**: Library management product does not strip Exif data from images
- **CVE-2020-26220**: Customer relationship management (CRM) product does not strip Exif data from images
- **CVE-2005-0406**: Some image editors modify a JPEG image, but the original EXIF thumbnail image is left intact within the JPEG. (Also an interaction error).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/359.html
