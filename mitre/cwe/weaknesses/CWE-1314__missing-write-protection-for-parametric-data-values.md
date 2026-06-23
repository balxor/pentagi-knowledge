---
cwe_id: CWE-1314
name: Missing Write Protection for Parametric Data Values
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Sensor Hardware]
related_capec: [CAPEC-1]
url: https://cwe.mitre.org/data/definitions/1314.html
tags: [mitre-cwe, weakness, CWE-1314]
---

# CWE-1314 - Missing Write Protection for Parametric Data Values

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1314](https://cwe.mitre.org/data/definitions/1314.html)

## Description
The device does not write-protect the parametric data values for sensors that scale the sensor value, allowing untrusted software to manipulate the apparent result and potentially damage hardware or cause operational failure.

## Extended description
Various sensors are used by hardware to detect any devices operating outside of the design limits. The threshold limit values are set by hardware fuses or trusted software such as the BIOS. These limits may be related to thermal, power, voltage, current, and frequency. Hardware mechanisms may be used to protect against alteration of the threshold limit values by untrusted software. The limit values are generally programmed in standard units for the type of value being read. However, the hardware-sensor blocks may report the settings in different units depending upon sensor design and operation. The raw sensor output value is converted to the desired units using a scale conversion based on the parametric data programmed into the sensor. The final converted value is then compared with the previously programmed limits. While the limit values are usually protected, the sensor parametric data values may not be. By changing the parametric data, safe operational limits may be bypassed.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Sensor Hardware

## Common consequences
- **Availability**: Quality Degradation, DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design**: Access controls for sensor blocks should ensure that only trusted software is allowed to change threshold limits and sensor parametric data.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)

## Related weaknesses
- CWE-862 (ChildOf)
- CWE-1299 (PeerOf)

## Observed examples (CVE)
- **CVE-2017-8252**: Kernel can inject faults in computations during the execution of TrustZone leading to information disclosure in Snapdragon Auto, Snapdragon Compute, Snapdragon Connectivity, Snapdragon Consumer Electronics Connectivity, Snapdragon Consumer IOT, Snapdragon Industrial IOT, Snapdragon IoT, Snapdragon Mobile, Snapdragon Voice and Music, Snapdragon Wearables, Snapdragon Wired Infrastructure and Networking.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1314.html
