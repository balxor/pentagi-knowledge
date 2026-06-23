---
cwe_id: CWE-1300
name: Improper Protection of Physical Side Channels
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-189, CAPEC-699]
url: https://cwe.mitre.org/data/definitions/1300.html
tags: [mitre-cwe, weakness, CWE-1300]
---

# CWE-1300 - Improper Protection of Physical Side Channels

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1300](https://cwe.mitre.org/data/definitions/1300.html)

## Description
The device does not contain sufficient protection mechanisms to prevent physical side channels from exposing sensitive information due to patterns in physically observable phenomena such as variations in power consumption, electromagnetic emissions (EME), or acoustic emissions.

## Extended description
An adversary could monitor and measure physical phenomena to detect patterns and make inferences, even if it is not possible to extract the information in the digital domain. Physical side channels have been well-studied for decades in the context of breaking implementations of cryptographic algorithms or other attacks against security features. These side channels may be easily observed by an adversary with physical access to the device, or using a tool that is in close proximity. If the adversary can monitor hardware operation and correlate its data processing with power, EME, and acoustic measurements, the adversary might be able to recover of secret keys and data.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data

## Potential mitigations
- **Architecture and Design**: Apply blinding or masking techniques to implementations of cryptographic algorithms.
- **Implementation**: Add shielding or tamper-resistant protections to the device to increase the difficulty of obtaining measurements of the side-channel.

## Related attack patterns (CAPEC)
- [CAPEC-189](https://capec.mitre.org/data/definitions/189.html)
- [CAPEC-699](https://capec.mitre.org/data/definitions/699.html)

## Related weaknesses
- CWE-203 (ChildOf)
- CWE-203 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-35888**: Power side-channels leak secret information from processor
- **CVE-2021-3011**: electromagnetic-wave side-channel in security-related microcontrollers allows extraction of private key
- **CVE-2019-14353**: Crypto hardware wallet's power consumption relates to total number of pixels illuminated, creating a side channel in the USB connection that allows attackers to determine secrets displayed such as PIN numbers and passwords
- **CVE-2020-27211**: Chain: microcontroller system-on-chip contains uses a register value stored in flash to set product protection state on the memory bus but does not contain protection against fault injection (CWE-1319), which leads to an incorrect initialization of the memory bus (CWE-1419) leading the product to be in an unprotected state.
- **CVE-2013-4576**: message encryption software uses certain instruction sequences that allows RSA key extraction using a chosen-ciphertext attack and acoustic cryptanalysis
- **CVE-2020-28368**: virtualization product allows recovery of AES keys from the guest OS using a side channel attack against a power/energy monitoring interface.
- **CVE-2019-18673**: power consumption varies based on number of pixels being illuminated in a display, allowing reading of secrets such as the PIN by using the USB interface to measure power consumption

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1300.html
