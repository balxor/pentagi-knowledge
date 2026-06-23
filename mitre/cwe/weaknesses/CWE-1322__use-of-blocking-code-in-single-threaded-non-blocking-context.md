---
cwe_id: CWE-1322
name: Use of Blocking Code in Single-threaded, Non-blocking Context
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-25]
url: https://cwe.mitre.org/data/definitions/1322.html
tags: [mitre-cwe, weakness, CWE-1322]
---

# CWE-1322 - Use of Blocking Code in Single-threaded, Non-blocking Context

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1322](https://cwe.mitre.org/data/definitions/1322.html)

## Description
The product uses a non-blocking model that relies on a single threaded process for features such as scalability, but it contains code that can block when it is invoked.

## Extended description
When an attacker can directly invoke the blocking code, or the blocking code can be affected by environmental conditions that can be influenced by an attacker, then this can lead to a denial of service by causing unexpected hang or freeze of the code. Examples of blocking code might be an expensive computation or calling blocking library calls, such as those that perform exclusive file operations or require a successful network operation. Due to limitations in multi-thread models, single-threaded models are used to overcome the resource constraints that are caused by using many threads. In such a model, all code should generally be non-blocking. If blocking code is called, then the event loop will effectively be stopped, which can be undesirable or dangerous. Such models are used in Python asyncio, Vert.x, and Node.js, or other custom event loop code.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU)

## Potential mitigations
- **Implementation**: Generally speaking, blocking calls should be replaced with non-blocking alternatives that can be used asynchronously. Expensive computations should be passed off to worker threads, although the correct approach depends on the framework being used.
- **Implementation**: For expensive computations, consider breaking them up into multiple smaller computations. Refer to the documentation of the framework being used for guidance.

## Related attack patterns (CAPEC)
- [CAPEC-25](https://capec.mitre.org/data/definitions/25.html)

## Related weaknesses
- CWE-834 (ChildOf)
- CWE-835 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1322.html
