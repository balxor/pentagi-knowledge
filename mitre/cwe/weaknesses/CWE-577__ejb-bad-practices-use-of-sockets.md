---
cwe_id: CWE-577
name: EJB Bad Practices: Use of Sockets
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/577.html
tags: [mitre-cwe, weakness, CWE-577]
---

# CWE-577 - EJB Bad Practices: Use of Sockets

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-577](https://cwe.mitre.org/data/definitions/577.html)

## Description
The product violates the Enterprise JavaBeans (EJB) specification by using sockets.

## Extended description
The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the product violates the following EJB guideline: "An enterprise bean must not attempt to listen on a socket, accept connections on a socket, or use a socket for multicast." The specification justifies this requirement in the following way: "The EJB architecture allows an enterprise bean instance to be a network socket client, but it does not allow it to be a network server. Allowing the instance to become a network server would conflict with the basic function of the enterprise bean-- to serve the EJB clients."

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Architecture and Design, Implementation**: Do not use Sockets when writing EJBs.

## Related weaknesses
- CWE-573 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/577.html
