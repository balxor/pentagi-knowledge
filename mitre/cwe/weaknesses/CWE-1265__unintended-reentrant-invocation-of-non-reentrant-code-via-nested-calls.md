---
cwe_id: CWE-1265
name: Unintended Reentrant Invocation of Non-reentrant Code Via Nested Calls
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-74]
url: https://cwe.mitre.org/data/definitions/1265.html
tags: [mitre-cwe, weakness, CWE-1265]
---

# CWE-1265 - Unintended Reentrant Invocation of Non-reentrant Code Via Nested Calls

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1265](https://cwe.mitre.org/data/definitions/1265.html)

## Description
The product invokes code that is believed to be reentrant, but the code performs a call that unintentionally produces a nested invocation of the non-reentrant code.

## Extended description
In a complex product, a single function call may lead to many different possible code paths, some of which may involve deeply nested calls. It may be difficult to foresee all possible code paths that could emanate from a given function call, even if that call is assumed to be reentrant. In some systems, an external actor can manipulate inputs to the system and thereby achieve a wide range of possible control flows. This is frequently a concern in products that execute scripts from untrusted sources. Examples of such products are web browsers and PDF readers. A weakness is present when one of the possible code paths resulting from a function call alters program state that the original caller assumes to be unchanged during the call.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Architecture and Design**: When architecting a system that will execute untrusted code in response to events, consider executing the untrusted event handlers asynchronously (asynchronous message passing) as opposed to executing them synchronously at the time each event fires. The untrusted code should execute at the start of the next iteration of the thread's message loop. In this way, calls into non-reentrant code are strictly serialized, so that each operation completes fully before the next operation begins. Special attention must be paid to all places where type coercion may result in script execution. Performing all needed coercions at the very beginning of an operation can help reduce the chance of operations executing at unexpected junctures.
- **Implementation**: Make sure the code (e.g., function or class) in question is reentrant by not leveraging non-local data, not modifying its own code, and not calling other non-reentrant code.

## Related attack patterns (CAPEC)
- [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)

## Related weaknesses
- CWE-662 (ChildOf)
- CWE-663 (PeerOf)
- CWE-416 (CanPrecede)

## Observed examples (CVE)
- **CVE-2014-1772**: In this vulnerability, by registering a malicious onerror handler, an adversary can produce unexpected re-entrance of a CDOMRange object. [REF-1098]
- **CVE-2018-8174**: This CVE covers several vulnerable scenarios enabled by abuse of the Class_Terminate feature in Microsoft VBScript. In one scenario, Class_Terminate is used to produce an undesirable re-entrance of ScriptingDictionary during execution of that object's destructor. In another scenario, a vulnerable condition results from a recursive entrance of a property setter method. This recursive invocation produces a second, spurious call to the Release method of a reference-counted object, causing a UAF when that object is freed prematurely. This vulnerability pattern has been popularized as "Double Kill". [REF-1099]

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1265.html
