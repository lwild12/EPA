# Packet Tracer setup: ISP / cell tower + CareLink core router

Small steps. Do them in order. Tick each one before moving on.
Addresses below are PLACEHOLDERS. Use the addressing from your brief if it gives any.

## 0. Rules that fix most problems

- Use the **lightning-bolt (auto) cable** if unsure. It picks a working type.
- Router to router over copper = **crossover** cable. Straight-through stays red.
- Every router port starts **shut down**. Run `no shutdown` on each one in use.
- Both ends of a link must be in the **same subnet** with the **same mask**.
- Save often (Ctrl+S). Packet Tracer crashes lose unsaved work.

## 1. Plan the addresses first (5 minutes)

Write this table before touching a device.

| Link | Side A (device / port / IP) | Side B (device / port / IP) | Subnet |
|---|---|---|---|
| CareLink core to ISP router | CARELINK-CORE g0/0 / 203.0.113.2 | ISP-R1 g0/0 / 203.0.113.1 | 203.0.113.0/30 |
| ISP to cell tower side | ISP-R1 g0/1 / (per your setup) | cell tower / central office server | (per your setup) |

203.0.113.0/24 is a documentation range, which is safe for a lab. A /30 gives exactly two usable addresses, ideal for a router-to-router link.

## 2. Build the physical links

1. Place the CareLink core router and the ISP router.
2. Connect them: **crossover** cable, one free port on each. Note the port names.
3. Wait 10 to 20 seconds. Look at the link dots:
   - **Red** = port shut down, wrong cable, or no power. Go to section 5.
   - **Amber** = still negotiating. Wait.
   - **Green** = link up. Continue.

## 3. Configure the link (both routers)

CareLink core:

```
enable
configure terminal
hostname CARELINK-CORE
interface g0/0
 description Link to ISP-R1
 ip address 203.0.113.2 255.255.255.252
 no shutdown
exit
```

ISP router:

```
enable
configure terminal
hostname ISP-R1
interface g0/0
 description Link to CARELINK-CORE
 ip address 203.0.113.1 255.255.255.252
 no shutdown
exit
```

Check from each router:

```
show ip interface brief
ping 203.0.113.1      (from CareLink)
ping 203.0.113.2      (from ISP)
```

Both interfaces must say `up / up`. If the first ping drops one reply, that is normal (ARP). Ping again.

## 4. Routing so traffic goes through the ISP

CareLink core: send unknown traffic to the ISP.

```
ip route 0.0.0.0 0.0.0.0 203.0.113.1
```

ISP router: needs a route BACK to CareLink's internal networks.

```
ip route <CARELINK-LAN-NETWORK> <MASK> 203.0.113.2
```

Or, if the ISP should not know CareLink's private ranges, do NAT on the CareLink core instead:

```
interface g0/0
 ip nat outside
interface <LAN-INTERFACE>
 ip nat inside
access-list 1 permit <CARELINK-LAN-NETWORK> <WILDCARD>
ip nat inside source list 1 interface g0/0 overload
```

Rule of thumb: a one-way route is the most common reason pings reach the ISP but never come back.

## 5. Troubleshooting ladder (stop at the first problem you find)

1. **Link dot red?**
   - Wrong cable type (use crossover).
   - `no shutdown` missing on one end.
   - Check `show ip interface brief`: status must not be "administratively down".
2. **Interface up/up but ping fails?**
   - Compare the two IPs and masks. Are they in the same /30?
   - `show running-config interface g0/0` on both routers.
3. **Ping works between routers but not from PCs?**
   - PC default gateway set to the router's LAN interface IP?
   - Default route on CareLink core present? `show ip route` should show `S*`.
   - ISP has a route back (or NAT is in place)?
4. **Ping works only one way?**
   - Missing return route on the far router.
5. **Still stuck for 10 minutes?** Write down what you tried, then move on and come back.

Useful commands:

```
show ip interface brief
show ip route
show running-config
show cdp neighbors          (confirms which port connects to which device)
ping <ip>
traceroute <ip>
```

## 6. Cell tower and DHCP part

Placement and wording differ between Packet Tracer versions, so check your own version.

1. Find the **Cell Tower** and **Central Office Server** in the device list (WAN Emulation / network devices area).
2. Connect them with the auto cable. Check the link dots.
3. Put the Central Office Server on the ISP side and give it its address and DHCP pool settings.
4. Cellular end devices (phones, tablets, laptops with a cellular card) pick up service from the tower. If a device shows no signal, check it is in range and its cellular interface is on.
5. For wired DHCP, either use the router as DHCP server:

```
ip dhcp excluded-address <GATEWAY-IP>
ip dhcp pool <NAME>
 network <NETWORK> <MASK>
 default-router <GATEWAY-IP>
 dns-server <DNS-IP>
```

or use a DHCP server device. Set PCs to **DHCP** and check they receive an address.

## 7. Evidence for the write-up

For each requirement, keep one screenshot and one line saying what it proves.

- [ ] `show ip interface brief` on both routers (links up)
- [ ] Ping between the two router link IPs
- [ ] `show ip route` on CareLink core showing the default route
- [ ] Ping from a CareLink PC to an ISP-side host
- [ ] `show cdp neighbors` showing the router-to-router connection
- [ ] Failover test (if the brief requires it): shut the primary link, show traffic using the backup

## 8. Harden after it works, not before

Get connectivity first. Then apply `cisco_hardening.md` and re-test, so you can tell whether a break came from your change.
