---
cwe_id: CWE-170
name: Improper Null Termination
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/170.html
tags: [mitre-cwe, weakness, CWE-170]
---

# CWE-170 - Improper Null Termination

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-170](https://cwe.mitre.org/data/definitions/170.html)

## Description
The product does not terminate or incorrectly terminates a string or array with a null character or equivalent terminator.

## Extended description
Null termination errors frequently occur in two different ways. An off-by-one error could cause a null to be written out of bounds, leading to an overflow. Or, a program could use a strncpy() function call incorrectly, which prevents a null terminator from being added at all. Other scenarios are possible.

## Applicable platforms / languages
C, C++

## Common consequences
- **Confidentiality, Integrity, Availability**: Read Memory, Execute Unauthorized Code or Commands
- **Confidentiality, Integrity, Availability**: DoS: Crash, Exit, or Restart, Read Memory, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Integrity, Availability**: Modify Memory, DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability, Access Control, Other**: Alter Execution Logic, Execute Unauthorized Code or Commands

## Potential mitigations
- **Requirements**: Use a language that is not susceptible to these issues. However, be careful of null byte interaction errors (CWE-626) with lower-level constructs that may be written in a language that is susceptible.
- **Implementation**: Ensure that all string functions used are understood fully as to how they append null characters. Also, be wary of off-by-one errors when appending nulls to the end of strings.
- **Implementation**: If performance constraints permit, special code can be added that validates null-termination of string buffers, this is a rather naive and error-prone solution.
- **Implementation**: Switch to bounded string manipulation functions. Inspect buffer lengths involved in the buffer overrun trace reported with the defect.
- **Implementation**: Add code that fills buffers with nulls (however, the length of buffers still needs to be inspected, to ensure that the non null-terminated string is not written at the physical end of the buffer).

## Related weaknesses
- CWE-707 (ChildOf)
- CWE-120 (CanPrecede)
- CWE-126 (CanPrecede)
- CWE-147 (CanAlsoBe)
- CWE-464 (PeerOf)
- CWE-463 (PeerOf)
- CWE-20 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-0312**: Attacker does not null-terminate argv[] when invoking another program.
- **CVE-2003-0777**: Interrupted step causes resultant lack of null termination.
- **CVE-2004-1072**: Fault causes resultant lack of null termination, leading to buffer expansion.
- **CVE-2001-1389**: Multiple vulnerabilities related to improper null termination.
- **CVE-2003-0143**: Product does not null terminate a message buffer after snprintf-like call, leading to overflow.
- **CVE-2009-2523**: Chain: product does not handle when an input string is not NULL terminated (CWE-170), leading to buffer over-read (CWE-125) or heap-based buffer overflow (CWE-122).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/170.html
