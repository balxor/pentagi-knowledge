---
cwe_id: CWE-921
name: Storage of Sensitive Data in a Mechanism without Access Control
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Mobile]
related_capec: []
url: https://cwe.mitre.org/data/definitions/921.html
tags: [mitre-cwe, weakness, CWE-921]
---

# CWE-921 - Storage of Sensitive Data in a Mechanism without Access Control

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-921](https://cwe.mitre.org/data/definitions/921.html)

## Description
The product stores sensitive information in a file system or device that does not have built-in access control.

## Extended description
While many modern file systems or devices utilize some form of access control in order to restrict access to data, not all storage mechanisms have this capability. For example, memory cards, floppy disks, CDs, and USB devices are typically made accessible to any user within the system. This can become a problem when sensitive data is stored in these mechanisms in a multi-user environment, because anybody on the system can read or write this data. On Android devices, external storage is typically globally readable and writable by other applications on the device. External storage may also be easily accessible through the mobile device's USB connection or physically accessible through the device's memory card port.

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories
- **Integrity**: Modify Application Data, Modify Files or Directories

## Related weaknesses
- CWE-922 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/921.html
