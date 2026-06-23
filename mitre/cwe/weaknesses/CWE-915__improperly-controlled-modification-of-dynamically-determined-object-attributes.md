---
cwe_id: CWE-915
name: Improperly Controlled Modification of Dynamically-Determined Object Attributes
type: weakness
abstraction: Base
status: Incomplete
languages: [Ruby, ASP.NET, PHP, Python, Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/915.html
tags: [mitre-cwe, weakness, CWE-915]
---

# CWE-915 - Improperly Controlled Modification of Dynamically-Determined Object Attributes

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-915](https://cwe.mitre.org/data/definitions/915.html)

## Description
The product receives input from an upstream component that specifies multiple attributes, properties, or fields that are to be initialized or updated in an object, but it does not properly control which attributes can be modified.

## Extended description
If the object contains attributes that were only intended for internal use, then their unexpected modification could lead to a vulnerability. This weakness is sometimes known by the language-specific mechanisms that make it possible, such as mass assignment, autobinding, or object injection.

## Applicable platforms / languages
Ruby, ASP.NET, PHP, Python, Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity**: Modify Application Data
- **Integrity**: Execute Unauthorized Code or Commands
- **Other, Integrity**: Varies by Context, Alter Execution Logic

## Potential mitigations
- **Implementation**: If available, use features of the language or framework that allow specification of allowlists of attributes or fields that are allowed to be modified. If possible, prefer allowlists over denylists. For applications written with Ruby on Rails, use the attr_accessible (allowlist) or attr_protected (denylist) macros in each class that may be used in mass assignment.
- **Architecture and Design, Implementation**: If available, use the signing/sealing features of the programming language to assure that deserialized data has not been tainted. For example, a hash-based message authentication code (HMAC) could be used to ensure that data has not been modified.
- **Implementation**: For any externally-influenced input, check the input against an allowlist of internal object attributes or fields that are allowed to be modified.
- **Implementation, Architecture and Design**: Refactor the code so that object attributes or fields do not need to be dynamically identified, and only expose getter/setter functionality for the intended attributes.

## Related weaknesses
- CWE-913 (ChildOf)
- CWE-502 (PeerOf)

## Observed examples (CVE)
- **CVE-2024-3283**: Application for using LLMs allows modification of a sensitive variable using mass assignment.
- **CVE-2012-2054**: Mass assignment allows modification of arbitrary attributes using modified URL.
- **CVE-2012-2055**: Source version control product allows modification of trusted key using mass assignment.
- **CVE-2008-7310**: Attackers can bypass payment step in e-commerce product.
- **CVE-2013-1465**: Use of PHP unserialize function on untrusted input allows attacker to modify application configuration.
- **CVE-2012-3527**: Use of PHP unserialize function on untrusted input in content management system might allow code execution.
- **CVE-2012-0911**: Use of PHP unserialize function on untrusted input in content management system allows code execution using a crafted cookie value.
- **CVE-2012-0911**: Content management system written in PHP allows unserialize of arbitrary objects, possibly allowing code execution.
- **CVE-2011-4962**: Content management system written in PHP allows code execution through page comments.
- **CVE-2009-4137**: Use of PHP unserialize function on cookie value allows remote code execution or upload of arbitrary files.
- **CVE-2007-5741**: Content management system written in Python interprets untrusted data as pickles, allowing code execution.
- **CVE-2011-2520**: Python script allows local users to execute code via pickled data.
- **CVE-2005-2875**: Python script allows remote attackers to execute arbitrary code using pickled objects.
- **CVE-2013-0277**: Ruby on Rails allows deserialization of untrusted YAML to execute arbitrary code.
- **CVE-2011-2894**: Spring framework allows deserialization of objects from untrusted sources to execute arbitrary code.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/915.html
