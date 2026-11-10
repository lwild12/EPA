# `<COMPANY>` network: step-by-step build (Packet Tracer)

One step at a time. Each step ends with a **Check**. Do not move on until the check passes.
All addresses are PLACEHOLDERS. If your brief gives addressing or VLANs, use those instead.

## The plan (read once)

```
[Cell tower]--[Central Office Server]         (ISP side)
                    |
                 ISP-R1 g0/0 ---- g0/0 <COMPANY>-CORE g0/1 (trunk) ---- g0/1 SW1 (access ports)
              203.0.113.1/30   203.0.113.2/30                              |
                                                                  PCs / laptops / servers
```

| VLAN | Name | Subnet | Gateway (core) | Who |
|---|---|---|---|---|
| 10 | STAFF | 10.10.10.0/24 | 10.10.10.1 | Office laptops |
| 20 | CLINICAL | 10.10.20.0/24 | 10.10.20.1 | Mobile / care staff devices |
| 30 | SERVERS | 10.10.30.0/24 | 10.10.30.1 | `<COMPANY>` app / API servers |
| 40 | GUEST | 10.10.40.0/24 | 10.10.40.1 | Visitors, no internal access |
| 99 | MGMT | 10.10.99.0/24 | 10.10.99.1 | Admin access to devices |

Link to ISP: 203.0.113.0/30. Core = .2, ISP = .1.

Why this design (one line for your write-up): segmentation limits spread if one device is lost or compromised, and the servers only accept HTTPS from the groups that need it.

---

## Part A: Switch (SW1)

**A1. Name it and create VLANs.**

```
enable
configure terminal
hostname SW1
vlan 10
 name STAFF
vlan 20
 name CLINICAL
vlan 30
 name SERVERS
vlan 40
 name GUEST
vlan 99
 name MGMT
exit
```

Check: `show vlan brief` lists all five.

**A2. Make the uplink to the core a trunk.**

```
interface g0/1
 description Trunk to <COMPANY>-CORE
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,99
 switchport nonegotiate
 no shutdown
exit
```

Check: `show interfaces trunk` shows g0/1 trunking with the five VLANs.

**A3. Put the device ports in the right VLANs.** Change port numbers to match your cables.

```
interface range f0/1 - 4
 description STAFF
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
exit
interface range f0/5 - 8
 description CLINICAL
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 spanning-tree bpduguard enable
exit
interface range f0/9 - 10
 description SERVERS
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
exit
interface range f0/11 - 12
 description GUEST
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast
 spanning-tree bpduguard enable
exit
```

Check: `show vlan brief` shows each port under the right VLAN.

**A4. Switch management address (VLAN 99).**

```
interface vlan 99
 ip address 10.10.99.2 255.255.255.0
 no shutdown
exit
ip default-gateway 10.10.99.1
```

**A5. Shut down unused ports.** Replace the range with your unused ports.

```
interface range f0/13 - 24
 shutdown
 switchport mode access
 switchport access vlan 999
exit
```

(VLAN 999 does not exist yet. Packet Tracer will create it. This parks unused ports on a dead VLAN.)

**A6. Save.** `end` then `write memory`.

---

## Part B: Core router (`<COMPANY>-CORE`)

**B1. Name it and bring up the ISP link.**

```
enable
configure terminal
hostname <COMPANY>-CORE
interface g0/0
 description Link to ISP-R1
 ip address 203.0.113.2 255.255.255.252
 no shutdown
exit
```

Check: `ping 203.0.113.1` replies (ISP side must be configured, see packet_tracer_setup.md).

**B2. Turn on the trunk interface, no IP on it.**

```
interface g0/1
 description Trunk to SW1
 no ip address
 no shutdown
exit
```

**B3. Create one subinterface per VLAN (router-on-a-stick).**

```
interface g0/1.10
 description STAFF
 encapsulation dot1Q 10
 ip address 10.10.10.1 255.255.255.0
exit
interface g0/1.20
 description CLINICAL
 encapsulation dot1Q 20
 ip address 10.10.20.1 255.255.255.0
exit
interface g0/1.30
 description SERVERS
 encapsulation dot1Q 30
 ip address 10.10.30.1 255.255.255.0
exit
interface g0/1.40
 description GUEST
 encapsulation dot1Q 40
 ip address 10.10.40.1 255.255.255.0
exit
interface g0/1.99
 description MGMT
 encapsulation dot1Q 99
 ip address 10.10.99.1 255.255.255.0
exit
```

Check: `show ip interface brief` shows all five subinterfaces up/up.
If down: the trunk on SW1 is not up, or `no shutdown` is missing on g0/1.

**B4. DHCP for the user VLANs (servers get static addresses).**

```
ip dhcp excluded-address 10.10.10.1 10.10.10.20
ip dhcp excluded-address 10.10.20.1 10.10.20.20
ip dhcp excluded-address 10.10.40.1 10.10.40.20
ip dhcp pool STAFF
 network 10.10.10.0 255.255.255.0
 default-router 10.10.10.1
 dns-server 8.8.8.8
ip dhcp pool CLINICAL
 network 10.10.20.0 255.255.255.0
 default-router 10.10.20.1
 dns-server 8.8.8.8
ip dhcp pool GUEST
 network 10.10.40.0 255.255.255.0
 default-router 10.10.40.1
 dns-server 8.8.8.8
```

Check: set a PC to DHCP. It gets an address in its VLAN. `show ip dhcp binding` lists it.
Servers: set static IPs, e.g. 10.10.30.10, mask 255.255.255.0, gateway 10.10.30.1.

**B5. Default route to the ISP and NAT out.**

```
ip route 0.0.0.0 0.0.0.0 203.0.113.1
access-list 1 permit 10.10.0.0 0.0.255.255
interface g0/0
 ip nat outside
exit
interface range g0/1.10 , g0/1.20 , g0/1.30 , g0/1.40
 ip nat inside
exit
ip nat inside source list 1 interface g0/0 overload
```

Check: PC in STAFF pings an ISP-side host. `show ip nat translations` shows entries.
Do this BEFORE the ACLs in Part C, so you know connectivity works first.

**B6. Save.** `end` then `write memory`.

---

## Part C: Segmentation rules (ACLs) on the core

Apply these only after Part B works. Test after each one.

Rules in plain English:
- GUEST: internet only, nothing internal.
- STAFF: can use the servers over HTTPS only, plus the internet.
- CLINICAL: servers over HTTPS only, plus DNS and the internet.
- SERVERS: replies only. They do not start connections to users.

**C1. GUEST (VLAN 40).**

```
ip access-list extended ACL-GUEST-IN
 permit udp any eq bootpc any eq bootps
 deny ip 10.10.40.0 0.0.0.255 10.10.0.0 0.0.255.255
 permit ip any any
exit
interface g0/1.40
 ip access-group ACL-GUEST-IN in
exit
```

Check: a guest PC can ping 203.0.113.1 but NOT 10.10.10.x or 10.10.30.x.

**C2. STAFF (VLAN 10).**

```
ip access-list extended ACL-STAFF-IN
 permit udp any eq bootpc any eq bootps
 permit tcp 10.10.10.0 0.0.0.255 10.10.30.0 0.0.0.255 eq 443
 deny ip 10.10.10.0 0.0.0.255 10.10.0.0 0.0.255.255
 permit ip any any
exit
interface g0/1.10
 ip access-group ACL-STAFF-IN in
exit
```

Check: a staff PC opens the server over HTTPS. Ping to the server fails (that is expected).

**C3. CLINICAL (VLAN 20).**

```
ip access-list extended ACL-CLINICAL-IN
 permit udp any eq bootpc any eq bootps
 permit tcp 10.10.20.0 0.0.0.255 10.10.30.0 0.0.0.255 eq 443
 deny ip 10.10.20.0 0.0.0.255 10.10.0.0 0.0.255.255
 permit ip any any
exit
interface g0/1.20
 ip access-group ACL-CLINICAL-IN in
exit
```

**C4. SERVERS (VLAN 30): stop servers starting connections to users.**

```
ip access-list extended ACL-SERVERS-IN
 permit tcp 10.10.30.0 0.0.0.255 any established
 deny ip 10.10.30.0 0.0.0.255 10.10.0.0 0.0.255.255
 permit ip any any
exit
interface g0/1.30
 ip access-group ACL-SERVERS-IN in
exit
```

Check: HTTPS from staff to the server still works (return traffic is `established`).

**C5. Save and screenshot** `show access-lists` after running the tests (hit counts prove the rules work).

---

## Part D: Lock down management

**D1. Basic hardening.** Replace the example secrets with your own.

```
no ip http server
no ip http secure-server
service password-encryption
enable secret <STRONG-SECRET>
ip domain-name <COMPANY>.local
username admin secret <STRONG-SECRET>
crypto key generate rsa modulus 2048
ip ssh version 2
banner motd # Authorised use only #
```

**D2. SSH only, and only from the management VLAN.**

```
access-list 10 permit 10.10.99.0 0.0.0.255
line vty 0 4
 login local
 transport input ssh
 access-class 10 in
 exec-timeout 5 0
exit
line console 0
 login local
 exec-timeout 5 0
exit
```

Check: from a PC in VLAN 99, `ssh -l admin 10.10.99.1` works. From STAFF it fails.

**D3. Logging and time (resilience and detection).**

```
service timestamps log datetime msec
logging host 10.10.30.50
ntp server 203.0.113.1
```

Use your syslog server's address. NTP only works if the ISP side has an NTP source configured.

**D4. Save.** `write memory`.

---

## Part E: Final test table (screenshot each)

| # | Test | Expected |
|---|---|---|
| 1 | Core pings ISP 203.0.113.1 | Success |
| 2 | Staff PC gets DHCP address | 10.10.10.x |
| 3 | Staff PC reaches server on HTTPS | Success |
| 4 | Staff PC pings server | Fails (blocked) |
| 5 | Guest PC reaches ISP host | Success |
| 6 | Guest PC reaches 10.10.30.x | Fails (blocked) |
| 7 | SSH from VLAN 99 | Success |
| 8 | SSH from STAFF | Fails |
| 9 | `show access-lists` | Hit counts on permit and deny lines |
| 10 | `show ip nat translations` | Entries present |

## Common mistakes

- Subinterface down: SW1 trunk missing, or `no shutdown` missing on g0/1.
- DHCP fails after adding an ACL: the `permit udp ... bootpc ... bootps` line is missing or is not the first line.
- Servers cannot answer clients: the SERVERS ACL blocks return traffic. Keep the `established` line.
- NAT not working: `ip nat inside` or `ip nat outside` missing on an interface.
- Ping to the server fails but you expected success: the ACL allows HTTPS only. Test with a browser or the PC's web client.
- Saved nothing: run `write memory` or you lose config on reload.
