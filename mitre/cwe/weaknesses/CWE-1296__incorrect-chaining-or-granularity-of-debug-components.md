---
cwe_id: CWE-1296
name: Incorrect Chaining or Granularity of Debug Components
type: weakness
abstraction: Base
status: Incomplete
languages: [Verilog, VHDL, Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific]
related_capec: [CAPEC-121, CAPEC-702]
url: https://cwe.mitre.org/data/definitions/1296.html
tags: [mitre-cwe, weakness, CWE-1296]
---

# CWE-1296 - Incorrect Chaining or Granularity of Debug Components

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1296](https://cwe.mitre.org/data/definitions/1296.html)

## Description
The product's debug components contain incorrect chaining or granularity of debug components.

## Extended description
For debugging and troubleshooting a chip, several hardware design elements are often implemented, including: Various Test Access Ports (TAPs) allow boundary scan commands to be executed. For scanning the internal components of a chip, there are scan cells that allow the chip to be used as a "stimulus and response" mechanism. Chipmakers might create custom methods to observe the internal components of their chips by placing various tracing hubs within their chip and creating hierarchical or interconnected structures among those hubs. Logic errors during design or synthesis could misconfigure the interconnection of the debug components, which could allow unintended access permissions.

## Applicable platforms / languages
Verilog, VHDL, Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control, Authentication, Authorization, Availability, Accountability**: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Execute Unauthorized Code or Commands, Modify Memory, Modify Files or Directories

## Potential mitigations
- **Implementation**: Ensure that debug components are properly chained and their granularity is maintained at different authentication levels.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)
- [CAPEC-702](https://capec.mitre.org/data/definitions/702.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2017-18347**: Incorrect access control in RDP Level 1 on STMicroelectronics STM32F0 series devices allows physically present attackers to extract the device's protected firmware via a special sequence of Serial Wire Debug (SWD) commands because there is a race condition between full initialization of the SWD interface and the setup of flash protection.
- **CVE-2020-1791**: There is an improper authorization vulnerability in several smartphones. The system has a logic-judging error, and, under certain scenarios, a successful exploit could allow the attacker to switch to third desktop after a series of operations in ADB mode. (Vulnerability ID: HWPSIRT-2019-10114).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1296.html
