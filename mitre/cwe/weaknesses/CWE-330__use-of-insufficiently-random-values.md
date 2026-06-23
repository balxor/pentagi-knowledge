---
cwe_id: CWE-330
name: Use of Insufficiently Random Values
type: weakness
abstraction: Class
status: Stable
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-112, CAPEC-485, CAPEC-59]
url: https://cwe.mitre.org/data/definitions/330.html
tags: [mitre-cwe, weakness, CWE-330]
---

# CWE-330 - Use of Insufficiently Random Values

**Abstraction:** Class  -  **Status:** Stable  -  **CWE:** [CWE-330](https://cwe.mitre.org/data/definitions/330.html)

## Description
The product uses insufficiently random numbers or values in a security context that depends on unpredictable numbers.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Other**: Other
- **Access Control, Other**: Bypass Protection Mechanism, Other
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Use a well-vetted algorithm that is currently considered to be strong by experts in the field, and select well-tested implementations with adequate length seeds. In general, if a pseudo-random number generator is not advertised as being cryptographically secure, then it is probably a statistical PRNG and should not be used in security-sensitive contexts. Pseudo-random number generators can produce predictable numbers if the generator is known and the seed can be guessed. A 256-bit seed is a good starting point for producing a "random enough" number.
- **Implementation**: Consider a PRNG that re-seeds itself as needed from high quality pseudo-random output sources, such as hardware devices.
- **Architecture and Design, Requirements**: Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C ("Approved Random Number Generators").

## Related attack patterns (CAPEC)
- [CAPEC-112](https://capec.mitre.org/data/definitions/112.html)
- [CAPEC-485](https://capec.mitre.org/data/definitions/485.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)

## Related weaknesses
- CWE-693 (ChildOf)
- CWE-804 (CanPrecede)

## Observed examples (CVE)
- **CVE-2021-3692**: PHP framework uses mt_rand() function (Marsenne Twister) when generating tokens
- **CVE-2020-7010**: Cloud application on Kubernetes generates passwords using a weak random number generator based on deployment time.
- **CVE-2009-3278**: Crypto product uses rand() library function to generate a recovery key, making it easier to conduct brute force attacks.
- **CVE-2009-3238**: Random number generator can repeatedly generate the same value.
- **CVE-2009-2367**: Web application generates predictable session IDs, allowing session hijacking.
- **CVE-2009-2158**: Password recovery utility generates a relatively small number of random passwords, simplifying brute force attacks.
- **CVE-2009-0255**: Cryptographic key created with a seed based on the system time.
- **CVE-2008-5162**: Kernel function does not have a good entropy source just after boot.
- **CVE-2008-4905**: Blogging software uses a hard-coded salt when calculating a password hash.
- **CVE-2008-4929**: Bulletin board application uses insufficiently random names for uploaded files, allowing other users to access private files.
- **CVE-2008-3612**: Handheld device uses predictable TCP sequence numbers, allowing spoofing or hijacking of TCP connections.
- **CVE-2008-2433**: Web management console generates session IDs based on the login time, making it easier to conduct session hijacking.
- **CVE-2008-0166**: SSL library uses a weak random number generator that only generates 65,536 unique keys.
- **CVE-2008-2108**: Chain: insufficient precision causes extra zero bits to be assigned, reducing entropy for an API function that generates random numbers.
- **CVE-2008-2108**: Chain: insufficient precision (CWE-1339) in random-number generator causes some zero bits to be reliably generated, reducing the amount of entropy (CWE-331)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/330.html
