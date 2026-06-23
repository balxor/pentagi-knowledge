---
cwe_id: CWE-927
name: Use of Implicit Intent for Sensitive Communication
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Mobile]
related_capec: []
url: https://cwe.mitre.org/data/definitions/927.html
tags: [mitre-cwe, weakness, CWE-927]
---

# CWE-927 - Use of Implicit Intent for Sensitive Communication

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-927](https://cwe.mitre.org/data/definitions/927.html)

## Description
The Android application uses an implicit intent for transmitting sensitive data to other applications.

## Extended description
Since an implicit intent does not specify a particular application to receive the data, any application can process the intent by using an Intent Filter for that intent. This can allow untrusted applications to obtain sensitive data. There are two variations on the standard broadcast intent, ordered and sticky. Ordered broadcast intents are delivered to a series of registered receivers in order of priority as declared by the Receivers. A malicious receiver can give itself a high priority and cause a denial of service by stopping the broadcast from propagating further down the chain. There is also the possibility of malicious data modification, as a receiver may also alter the data within the Intent before passing it on to the next receiver. The downstream components have no way of asserting that the data has not been altered earlier in the chain. Sticky broadcast intents remain accessible after the initial broadcast. An old sticky intent will be broadcast again to any new receivers that register for it in the future, greatly increasing the chances of information exposure over time. Also, sticky broadcasts cannot be protected by permissions that may apply to other kinds of intents. In addition, any broadcast intent may include a URI that references data that the receiving component does not normally have the privileges to access. The sender of the intent can include special privileges that grant the receiver read or write access to the specific URI included in the intent. A malicious receiver that intercepts this intent will also gain those privileges and be able to read or write the resource at the specified URI.

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Varies by Context

## Potential mitigations
- **Implementation**: If the application only requires communication with its own components, then the destination is always known, and an explicit intent could be used.

## Related weaknesses
- CWE-285 (ChildOf)
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-4903**: An Android application does not use FLAG_IMMUTABLE when creating a PendingIntent.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/927.html
