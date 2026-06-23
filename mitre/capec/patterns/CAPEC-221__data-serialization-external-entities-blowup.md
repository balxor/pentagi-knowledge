---
capec_id: CAPEC-221
name: Data Serialization External Entities Blowup
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-611]
related_attack: []
url: https://capec.mitre.org/data/definitions/221.html
tags: [mitre-capec, attack-pattern, CAPEC-221]
---

# CAPEC-221 - Data Serialization External Entities Blowup

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-221](https://capec.mitre.org/data/definitions/221.html)

## Description
This attack takes advantage of the entity replacement property of certain data serialization languages (e.g., XML, YAML, etc.) where the value of the replacement is a URI. A well-crafted file could have the entity refer to a URI that consumes a large amount of resources to create a denial of service condition. This can cause the system to either freeze, crash, or execute arbitrary code depending on the URI.

## Prerequisites
- A server that has an implementation that accepts entities containing URI values.

## Consequences
- **Availability**: Resource Consumption, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Find target web service: The adversary must first find a web service that takes input data in the form of a serialized language such as XML or YAML. Experiment Host malicious file on a server: The adversary will create a web server that contains a malicious file. This file will be extremely large, so that if a web service were to try to load it, the service would most likely hang. Craft malicious data: Using the serialization language that the web service takes as input, the adversary will craft data that links to the malicious file using an external entity reference to the URL of the file. Exploit Send serialized data containing URI: The adversary will send specially crafted serialized data to the web service. When the web service loads the input, it will attempt to download the malicious file. Depending on the amount of memory the web service has, this could either crash the service or cause it to hang, resulting in a Denial of Service attack.

## Mitigations
- This attack may be mitigated by tweaking the XML parser to not resolve external entities. If external entities are needed, then implement a custom XmlResolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.
- This attack may be mitigated by tweaking the serialized data parser to not resolve external entities. If external entities are needed, then implement a custom resolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.

## Related weaknesses (CWE)
- [CWE-611](https://cwe.mitre.org/data/definitions/611.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/221.html
