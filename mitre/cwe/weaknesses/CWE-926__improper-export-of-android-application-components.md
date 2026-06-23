---
cwe_id: CWE-926
name: Improper Export of Android Application Components
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Mobile]
related_capec: []
url: https://cwe.mitre.org/data/definitions/926.html
tags: [mitre-cwe, weakness, CWE-926]
---

# CWE-926 - Improper Export of Android Application Components

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-926](https://cwe.mitre.org/data/definitions/926.html)

## Description
The Android application exports a component for use by other applications, but does not properly restrict which applications can launch the component or access the data it contains.

## Extended description
The attacks and consequences of improperly exporting a component may depend on the exported component: If access to an exported Activity is not restricted, any application will be able to launch the activity. This may allow a malicious application to gain access to sensitive information, modify the internal state of the application, or trick a user into interacting with the victim application while believing they are still interacting with the malicious application. If access to an exported Service is not restricted, any application may start and bind to the Service. Depending on the exposed functionality, this may allow a malicious application to perform unauthorized actions, gain access to sensitive information, or corrupt the internal state of the application. If access to a Content Provider is not restricted to only the expected applications, then malicious applications might be able to access the sensitive data. Note that in Android before 4.2, the Content Provider is automatically exported unless it has been explicitly declared as NOT exported.

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Availability, Integrity**: Unexpected State, DoS: Crash, Exit, or Restart, DoS: Instability, Varies by Context
- **Availability, Integrity**: Unexpected State, Gain Privileges or Assume Identity, DoS: Crash, Exit, or Restart, DoS: Instability, Varies by Context
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Potential mitigations
- **Build and Compilation**: If they do not need to be shared by other applications, explicitly mark components with android:exported="false" in the application manifest.
- **Build and Compilation**: If you only intend to use exported components between related apps under your control, use android:protectionLevel="signature" in the xml manifest to restrict access to applications signed by you.
- **Build and Compilation, Architecture and Design**: Limit Content Provider permissions (read/write) as appropriate.
- **Build and Compilation, Architecture and Design**: Limit Content Provider permissions (read/write) as appropriate.

## Related weaknesses
- CWE-285 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/926.html
