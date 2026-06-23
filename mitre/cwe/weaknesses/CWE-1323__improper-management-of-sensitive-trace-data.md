---
cwe_id: CWE-1323
name: Improper Management of Sensitive Trace Data
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip]
related_capec: [CAPEC-150, CAPEC-167, CAPEC-545]
url: https://cwe.mitre.org/data/definitions/1323.html
tags: [mitre-cwe, weakness, CWE-1323]
---

# CWE-1323 - Improper Management of Sensitive Trace Data

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1323](https://cwe.mitre.org/data/definitions/1323.html)

## Description
Trace data collected from several sources on the System-on-Chip (SoC) is stored in unprotected locations or transported to untrusted agents.

## Extended description
To facilitate verification of complex System-on-Chip (SoC) designs, SoC integrators add specific IP blocks that trace the SoC's internal signals in real-time. This infrastructure enables observability of the SoC's internal behavior, validation of its functional design, and detection of hardware and software bugs. Such tracing IP blocks collect traces from several sources on the SoC including the CPU, crypto coprocessors, and on-chip fabrics. Traces collected from these sources are then aggregated inside trace IP block and forwarded to trace sinks, such as debug-trace ports that facilitate debugging by external hardware and software debuggers. Since these traces are collected from several security-sensitive sources, they must be protected against untrusted debuggers. If they are stored in unprotected memory, an untrusted software debugger can access these traces and extract secret information. Additionally, if security-sensitive traces are not tagged as secure, an untrusted hardware debugger might access them to extract confidential information.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Confidentiality**: Read Memory

## Potential mitigations
- **Implementation**: Tag traces to indicate owner and debugging privilege level (designer, OEM, or end user) needed to access that trace.

## Related attack patterns (CAPEC)
- [CAPEC-150](https://capec.mitre.org/data/definitions/150.html)
- [CAPEC-167](https://capec.mitre.org/data/definitions/167.html)
- [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)

## Related weaknesses
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1323.html
