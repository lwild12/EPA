# Cisco IOS hardening templates (Exercise 1)

Paste into Packet Tracer and change the `<PLACEHOLDERS>`. For each block, write one line in your
write-up saying **what threat it reduces** (that is what the Merit/Distinction criteria look for).

## 1. Base device hardening
```
enable secret <STRONG_SECRET>
service password-encryption
no ip domain-lookup
banner motd # Authorised access only. Activity is monitored. #
security passwords min-length 12
login block-for 120 attempts 3 within 60
hostname <NAME>
ip domain-name <domain.local>
crypto key generate rsa modulus 2048
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3
username admin secret <STRONG_SECRET>
```
Threat: credential theft from configs, brute force, clear-text management (Telnet).

## 2. Lock down management lines
```
line console 0
 login local
 exec-timeout 5 0
 logging synchronous
line vty 0 4
 login local
 transport input ssh
 exec-timeout 5 0
 access-class MGMT_ONLY in
no ip http server
no ip http secure-server
```

## 3. Management ACL
```
ip access-list standard MGMT_ONLY
 permit <MGMT_SUBNET> <WILDCARD>
 deny any log
```

## 4. Switch port security and L2 hardening
```
interface range fa0/1 - 24
 switchport mode access
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security mac-address sticky
 spanning-tree portfast
 spanning-tree bpduguard enable
interface range fa0/25 - 48
 shutdown
 switchport mode access
 switchport access vlan 999
vlan 999
 name BLACKHOLE
interface <TRUNK>
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan <LIST>
 switchport nonegotiate
```
Threat: MAC flooding, rogue switches, VLAN hopping, unused-port access.

## 5. VLANs and inter-VLAN routing (router-on-a-stick)
```
vlan 10
 name STAFF
vlan 20
 name STUDENTS
vlan 30
 name SERVERS
interface g0/0.10
 encapsulation dot1Q 10
 ip address <GW10> <MASK>
interface g0/0.20
 encapsulation dot1Q 20
 ip address <GW20> <MASK>
interface g0/0
 no shutdown
```

## 6. Segmentation ACL (students cannot reach servers except web)
```
ip access-list extended STUDENT_IN
 permit tcp <STU_NET> <STU_WILD> host <WEB_SERVER> eq 443
 permit udp <STU_NET> <STU_WILD> host <DNS_SERVER> eq 53
 deny   ip  <STU_NET> <STU_WILD> <SERVER_NET> <SERVER_WILD> log
 permit ip  <STU_NET> <STU_WILD> any
interface g0/0.20
 ip access-group STUDENT_IN in
```
Threat: lateral movement from the least-trusted VLAN to servers. `log` gives evidence for Ex3.

## 7. DHCP snooping and Dynamic ARP Inspection
```
ip dhcp snooping
ip dhcp snooping vlan 10,20
interface <UPLINK_TO_DHCP>
 ip dhcp snooping trust
ip arp inspection vlan 10,20
interface <UPLINK_TO_DHCP>
 ip arp inspection trust
```
Threat: rogue DHCP server, ARP spoofing / man-in-the-middle.
(Some Packet Tracer versions do not support DAI. If rejected, say so and describe it instead.)

## 8. Logging, time and SNMP
```
service timestamps log datetime msec
logging host <SYSLOG_IP>
logging trap informational
ntp server <NTP_IP>
no snmp-server community public
```

## 9. Basic NAT / outside edge
```
ip access-list standard NAT_INSIDE
 permit <INSIDE_NET> <WILD>
ip nat inside source list NAT_INSIDE interface g0/1 overload
interface g0/0
 ip nat inside
interface g0/1
 ip nat outside
```

## Verification commands (screenshot these as evidence)
```
show running-config
show vlan brief
show ip interface brief
show ip route
show access-lists
show port-security interface fa0/1
show ip ssh
show ip dhcp snooping
```
