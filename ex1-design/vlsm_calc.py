#!/usr/bin/env python3
"""VLSM subnet calculator for EPA Exercise 1.

Usage:
    python3 vlsm_calc.py 192.168.0.0/22 "Staff=120" "Students=250" "Servers=30" "Guest=60"

Each requirement is NAME=HOSTS. Hosts are the number of usable host addresses
needed (add growth headroom yourself, or use --growth 0.25 for 25%).
Subnets are allocated largest first, which avoids fragmentation.
Point-to-point WAN links: use NAME=2 (gets a /30).
"""
import argparse
import ipaddress
import math
import sys


def prefix_for_hosts(hosts: int) -> int:
    # usable hosts = 2^(32-p) - 2 ; /31 point-to-point is not used here
    needed = hosts + 2
    bits = max(2, math.ceil(math.log2(needed)))
    return 32 - bits


def allocate(network: ipaddress.IPv4Network, reqs, growth: float = 0.0):
    reqs = sorted(reqs, key=lambda r: r[1], reverse=True)
    cursor = int(network.network_address)
    end = int(network.broadcast_address)
    out = []
    for name, hosts in reqs:
        sized = math.ceil(hosts * (1 + growth))
        prefix = prefix_for_hosts(sized)
        size = 2 ** (32 - prefix)
        # align cursor to block size
        if cursor % size:
            cursor += size - (cursor % size)
        if cursor + size - 1 > end:
            raise ValueError(f"Out of space allocating {name} ({sized} hosts, /{prefix}) in {network}")
        sub = ipaddress.ip_network((cursor, prefix))
        usable = size - 2
        out.append({
            "name": name,
            "requested": hosts,
            "sized_for": sized,
            "network": sub,
            "mask": sub.netmask,
            "wildcard": sub.hostmask,
            "first": sub.network_address + 1,
            "last": sub.broadcast_address - 1,
            "broadcast": sub.broadcast_address,
            "gateway": sub.network_address + 1,
            "usable": usable,
            "spare": usable - hosts,
        })
        cursor += size
    used = cursor - int(network.network_address)
    return out, used, network.num_addresses


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("network", help="Parent block, e.g. 192.168.0.0/22")
    ap.add_argument("reqs", nargs="+", help='NAME=HOSTS, e.g. "Staff=120"')
    ap.add_argument("--growth", type=float, default=0.0, help="growth headroom, e.g. 0.25")
    ap.add_argument("--markdown", action="store_true", help="print a markdown table for your write-up")
    args = ap.parse_args()

    try:
        net = ipaddress.ip_network(args.network, strict=True)
        reqs = []
        for r in args.reqs:
            n, h = r.split("=")
            reqs.append((n.strip(), int(h)))
        rows, used, total = allocate(net, reqs, args.growth)
    except Exception as e:  # noqa: BLE001
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.markdown:
        print("| Subnet | Hosts needed | Network | Mask | Gateway | Range | Broadcast | Spare |")
        print("|---|---|---|---|---|---|---|---|")
        for r in rows:
            print(f"| {r['name']} | {r['requested']} | {r['network']} | {r['mask']} | {r['gateway']} | "
                  f"{r['first']} - {r['last']} | {r['broadcast']} | {r['spare']} |")
    else:
        hdr = f"{'Name':<14}{'Need':>6}{'Network':>20}{'Mask':>18}{'Gateway':>16}{'Broadcast':>16}{'Spare':>7}"
        print(hdr)
        print("-" * len(hdr))
        for r in rows:
            print(f"{r['name']:<14}{r['requested']:>6}{str(r['network']):>20}{str(r['mask']):>18}"
                  f"{str(r['gateway']):>16}{str(r['broadcast']):>16}{r['spare']:>7}")
    print(f"\nUsed {used} of {total} addresses in {net} ({used / total:.0%}); "
          f"{total - used} left for growth.")


if __name__ == "__main__":
    main()
