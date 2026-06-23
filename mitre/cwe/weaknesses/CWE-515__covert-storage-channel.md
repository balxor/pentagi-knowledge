---
cwe_id: CWE-515
name: Covert Storage Channel
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/515.html
tags: [mitre-cwe, weakness, CWE-515]
---

# CWE-515 - Covert Storage Channel

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-515](https://cwe.mitre.org/data/definitions/515.html)

## Description
A covert storage channel transfers information through the setting of bits by one program and the reading of those bits by another. What distinguishes this case from that of ordinary operation is that the bits are used to convey encoded information.

## Extended description
Covert storage channels occur when out-of-band data is stored in messages for the purpose of memory reuse. Covert channels are frequently classified as either storage or timing channels. Examples would include using a file intended to hold only audit information to convey user passwords--using the name of a file or perhaps status bits associated with it that can be read by all users to signal the contents of the file. Steganography, concealing information in such a manner that no one but the intended recipient knows of the existence of the message, is a good example of a covert storage channel.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity, Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Ensure that all reserved fields are set to zero before messages are sent and that no unnecessary information is included.

## Related weaknesses
- CWE-514 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/515.html
