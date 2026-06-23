---
cwe_id: CWE-666
name: Operation on Resource in Wrong Phase of Lifetime
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/666.html
tags: [mitre-cwe, weakness, CWE-666]
---

# CWE-666 - Operation on Resource in Wrong Phase of Lifetime

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-666](https://cwe.mitre.org/data/definitions/666.html)

## Description
The product performs an operation on a resource at the wrong phase of the resource's lifecycle, which can lead to unexpected behaviors.

## Extended description
A resource's lifecycle includes several phases: initialization, use, and release. For each phase, it is important to follow the specifications outlined for how to operate on the resource and to ensure that the resource is in the expected phase. Otherwise, if a resource is in one phase but the operation is not valid for that phase (i.e., an incorrect phase of the resource's lifetime), then this can produce resultant weaknesses. For example, using a resource before it has been fully initialized could cause corruption or incorrect data to be used.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other

## Potential mitigations
- **Architecture and Design**: Follow the resource's lifecycle from creation to release.

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-5051**: Chain: Signal handler contains too much functionality (CWE-828), introducing a race condition (CWE-362) that leads to a double free (CWE-415).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/666.html
