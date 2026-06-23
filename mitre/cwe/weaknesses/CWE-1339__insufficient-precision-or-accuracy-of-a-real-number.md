---
cwe_id: CWE-1339
name: Insufficient Precision or Accuracy of a Real Number
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1339.html
tags: [mitre-cwe, weakness, CWE-1339]
---

# CWE-1339 - Insufficient Precision or Accuracy of a Real Number

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1339](https://cwe.mitre.org/data/definitions/1339.html)

## Description
The product processes a real number with an implementation in which the number's representation does not preserve required accuracy and precision in its fractional part, causing an incorrect result.

## Extended description
When a security decision or calculation requires highly precise, accurate numbers such as financial calculations or prices, then small variations in the number could be exploited by an attacker. There are multiple ways to store the fractional part of a real number in a computer. In all of these cases, there is a limit to the accuracy of recording a fraction. If the fraction can be represented in a fixed number of digits (binary or decimal), there might not be enough digits assigned to represent the number. In other cases the number cannot be represented in a fixed number of digits due to repeating in decimal or binary notation (e.g. 0.333333...) or due to a transcendental number such as Π or √2. Rounding of numbers can lead to situations where the computer results do not adequately match the result of sufficiently accurate math.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity**: Execute Unauthorized Code or Commands
- **Confidentiality, Availability, Access Control**: Read Application Data, Modify Application Data

## Potential mitigations
- **Implementation, Patching and Maintenance**: The developer or maintainer can move to a more accurate representation of real numbers. In extreme cases, the programmer can move to representations such as ratios of BigInts which can represent real numbers to extremely fine precision. The programmer can also use the concept of an Unum real. The memory and CPU tradeoffs of this change must be examined. Since floating point reals are used in many products and many locations, they are implemented in hardware and most format changes will cause the calculations to be moved into software resulting in slower products.

## Related weaknesses
- CWE-682 (ChildOf)
- CWE-190 (PeerOf)
- CWE-834 (CanPrecede)
- CWE-119 (CanPrecede)

## Observed examples (CVE)
- **CVE-2018-16069**: Chain: series of floating-point precision errors (CWE-1339) in a web browser rendering engine causes out-of-bounds read (CWE-125), giving access to cross-origin data
- **CVE-2017-7619**: Chain: rounding error in floating-point calculations (CWE-1339) in image processor leads to infinite loop (CWE-835)
- **CVE-2021-29529**: Chain: machine-learning product can have a heap-based buffer overflow (CWE-122) when some integer-oriented bounds are calculated by using ceiling() and floor() on floating point values (CWE-1339)
- **CVE-2008-2108**: Chain: insufficient precision (CWE-1339) in random-number generator causes some zero bits to be reliably generated, reducing the amount of entropy (CWE-331)
- **CVE-2006-6499**: Chain: web browser crashes due to infinite loop - "bad looping logic [that relies on] floating point math [CWE-1339] to exit the loop [CWE-835]"

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1339.html
