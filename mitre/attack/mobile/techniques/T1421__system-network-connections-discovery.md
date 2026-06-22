---
attack_id: T1421
name: System Network Connections Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1421
tags: [mitre-attack, technique, T1421]
---

# T1421 - System Network Connections Discovery

**Tactic(s):** Discovery  -  **Platforms:** Android  -  **ATT&CK:** [T1421](https://attack.mitre.org/techniques/T1421)

## Summary
Adversaries may attempt to get a listing of network connections to or from the compromised device they are currently accessing or from remote systems by querying for information over the network. 

 

This is typically accomplished by utilizing device APIs to collect information about nearby networks, such as Wi-Fi, Bluetooth, and cellular tower connections. On Android, this can be done by querying the respective APIs: 

 

* `WifiInfo` for information about the current Wi-Fi connection, as well as nearby Wi-Fi networks. Querying the `WiFiInfo` API requires the application to hold the `ACCESS_FINE_LOCATION` permission. 

* `BluetoothAdapter` for information about Bluetooth devices, which also requires the application to hold several permissions granted by the user at runtime. 

* For Android versions prior to Q, applications can use the `TelephonyManager.getNeighboringCellInfo()` method. For Q and later, applications can use the `TelephonyManager.getAllCellInfo()` method. Both methods require the application hold the `ACCESS_FINE_LOCATION` permission.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1421
