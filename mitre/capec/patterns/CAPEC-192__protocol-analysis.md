---
capec_id: CAPEC-192
name: Protocol Analysis
type: attack-pattern
abstraction: Meta
likelihood: Low
severity: Low
related_cwe: [CWE-326]
related_attack: []
url: https://capec.mitre.org/data/definitions/192.html
tags: [mitre-capec, attack-pattern, CAPEC-192]
---

# CAPEC-192 - Protocol Analysis

**Abstraction:** Meta  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-192](https://capec.mitre.org/data/definitions/192.html)

## Description
An adversary engages in activities to decipher and/or decode protocol information for a network or application communication protocol used for transmitting information between interconnected nodes or systems on a packet-switched data network. While this type of analysis involves the analysis of a networking protocol inherently, it does not require the presence of an actual or physical network.

## Extended description
Although certain techniques for protocol analysis benefit from manipulating live 'on-the-wire' interactions between communicating components, static or dynamic analysis techniques applied to executables as well as to device drivers, such as network interface drivers, can also be used to reveal the function and characteristics of a communication protocol implementation. Depending upon the methods used the process may involve observing, interacting, and modifying actual communications occurring between hosts. The goal of protocol analysis is to derive the data transmission syntax, as well as to extract the meaningful content, including packet or content delimiters used by the protocol. This type of analysis is often performed on closed-specification protocols, or proprietary protocols, but is also useful for analyzing publicly available specifications to determine how particular implementations deviate from published specifications.

## Prerequisites
- Access to a binary executable.
- The ability to observe and interact with a communication channel between communicating processes.

## Skills required
- **High**: Knowlegde of the Open Systems Interconnection model (OSI model), and famililarity with Wireshark or some other packet analyzer.

## Resources required
- Depending on the type of analysis, a variety of tools might be required, such as static code and/or dynamic analysis tools. Alternatively, the effort might require debugging programs such as ollydbg, SoftICE, or disassemblers like IDA Pro. In some instances, packet sniffing or packet analyzing programs such as TCP dump or Wireshark are necessary. Lastly, specific protocol analysis might require tools such as PDB (Protocol Debug), or packet injection tools like pcap or Nemesis.

## Consequences
- **Confidentiality**: Read Data (Successful deciphering of protocol information compromises the confidentiality of future sensitive communications.)
- **Integrity**: Modify Data (Modifying communications after successful deciphering of protocol information compromises integrity.)

## Related weaknesses (CWE)
- [CWE-326](https://cwe.mitre.org/data/definitions/326.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/192.html
