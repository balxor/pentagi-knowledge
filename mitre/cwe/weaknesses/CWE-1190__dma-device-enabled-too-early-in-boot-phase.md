---
cwe_id: CWE-1190
name: DMA Device Enabled Too Early in Boot Phase
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, System on Chip]
related_capec: [CAPEC-180]
url: https://cwe.mitre.org/data/definitions/1190.html
tags: [mitre-cwe, weakness, CWE-1190]
---

# CWE-1190 - DMA Device Enabled Too Early in Boot Phase

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1190](https://cwe.mitre.org/data/definitions/1190.html)

## Description
The product enables a Direct Memory Access (DMA) capable device before the security configuration settings are established, which allows an attacker to extract data from or gain privileges on the product.

## Extended description
DMA is included in a number of devices because it allows data transfer between the computer and the connected device, using direct hardware access to read or write directly to main memory without any OS interaction. An attacker could exploit this to access secrets. Several virtualization-based mitigations have been introduced to thwart DMA attacks. These are usually configured/setup during boot time. However, certain IPs that are powered up before boot is complete (known as early boot IPs) may be DMA capable. Such IPs, if not trusted, could launch DMA attacks and gain access to assets that should otherwise be protected.

## Applicable platforms / languages
Not Language-Specific, System on Chip

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Modify Memory

## Potential mitigations
- **Architecture and Design**: Utilize an IOMMU to orchestrate IO access from the start of the boot process.

## Related attack patterns (CAPEC)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)

## Related weaknesses
- CWE-696 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1190.html
