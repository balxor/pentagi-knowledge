---
cwe_id: CWE-1297
name: Unprotected Confidential Information on Device is Accessible by OSAT Vendors
type: weakness
abstraction: Base
status: Incomplete
languages: [Verilog, VHDL, Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific]
related_capec: [CAPEC-1, CAPEC-180]
url: https://cwe.mitre.org/data/definitions/1297.html
tags: [mitre-cwe, weakness, CWE-1297]
---

# CWE-1297 - Unprotected Confidential Information on Device is Accessible by OSAT Vendors

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1297](https://cwe.mitre.org/data/definitions/1297.html)

## Description
The product does not adequately protect confidential information on the device from being accessed by Outsourced Semiconductor Assembly and Test (OSAT) vendors.

## Extended description
In contrast to complete vertical integration of architecting, designing, manufacturing, assembling, and testing chips all within a single organization, an organization can choose to simply architect and design a chip before outsourcing the rest of the process to OSAT entities (e.g., external foundries and test houses). In the latter example, the device enters an OSAT facility in a much more vulnerable pre-production stage where many debug and test modes are accessible. Therefore, the chipmaker must place a certain level of trust with the OSAT. To counter this, the chipmaker often requires the OSAT partner to enter into restrictive non-disclosure agreements (NDAs). Nonetheless, OSAT vendors likely have many customers, which increases the risk of accidental sharing of information. There may also be a security vulnerability in the information technology (IT) system of the OSAT facility. Alternatively, a malicious insider at the OSAT facility may carry out an insider attack. Considering these factors, it behooves the chipmaker to minimize any confidential information in the device that may be accessible to the OSAT vendor. Logic errors during design or synthesis could misconfigure the interconnection of the debug components, which could provide improper authorization to sensitive information.

## Applicable platforms / languages
Verilog, VHDL, Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control, Authentication, Authorization, Availability, Accountability, Non-Repudiation**: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Execute Unauthorized Code or Commands, Modify Memory, Modify Files or Directories

## Potential mitigations
- **Architecture and Design**: Ensure that when an OSAT vendor is allowed to access test interfaces necessary for preproduction and returned parts, the vendor only pulls the minimal information necessary. Also, architect the product in such a way that, when an "unlock device" request comes, it only unlocks that specific part and not all the parts for that product line. Ensure that the product's non-volatile memory (NVM) is scrubbed of all confidential information and secrets before handing it over to an OSAT. Arrange to secure all communication between an OSAT facility and the chipmaker.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)

## Related weaknesses
- CWE-285 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1297.html
