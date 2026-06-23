---
cwe_id: CWE-835
name: Loop with Unreachable Exit Condition ('Infinite Loop')
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/835.html
tags: [mitre-cwe, weakness, CWE-835]
---

# CWE-835 - Loop with Unreachable Exit Condition ('Infinite Loop')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-835](https://cwe.mitre.org/data/definitions/835.html)

## Description
The product contains an iteration or loop with an exit condition that cannot be reached, i.e., an infinite loop.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Amplification

## Related weaknesses
- CWE-834 (ChildOf)
- CWE-834 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-32399**: Chain: library for implementing Profinet devices does not check an input for a loop condition (CWE-606), allowing an infinite loop (CWE-835) via a crafted RPC packet
- **CVE-2022-22224**: Chain: an operating system does not properly process malformed Open Shortest Path First (OSPF) Type/Length/Value Identifiers (TLV) (CWE-703), which can cause the process to enter an infinite loop (CWE-835)
- **CVE-2022-25304**: A Python machine communication platform did not account for receiving a malformed packet with a null size, causing the receiving function to never update the message buffer and be caught in an infinite loop.
- **CVE-2011-1027**: Chain: off-by-one error (CWE-193) leads to infinite loop (CWE-835) using invalid hex-encoded characters.
- **CVE-2011-1142**: Chain: self-referential values in recursive definitions lead to infinite loop.
- **CVE-2011-1002**: NULL UDP packet is never cleared from a queue, leading to infinite loop.
- **CVE-2006-6499**: Chain: web browser crashes due to infinite loop - "bad looping logic [that relies on] floating point math [CWE-1339] to exit the loop [CWE-835]"
- **CVE-2010-4476**: Floating point conversion routine cycles back and forth between two different values.
- **CVE-2010-4645**: Floating point conversion routine cycles back and forth between two different values.
- **CVE-2010-2534**: Chain: improperly clearing a pointer in a linked list leads to infinite loop.
- **CVE-2013-1591**: Chain: an integer overflow (CWE-190) in the image size calculation causes an infinite loop (CWE-835) which sequentially allocates buffers without limits (CWE-1325) until the stack is full.
- **CVE-2008-3688**: Chain: A denial of service may be caused by an uninitialized variable (CWE-457) allowing an infinite loop (CWE-835) resulting from a connection to an unresponsive server.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/835.html
