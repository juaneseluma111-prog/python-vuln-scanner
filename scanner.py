#!/usr/bin/env python3
"""
Network Vulnerability Scanner
Author: Juan Esteban Umana Machado
Portfolio: github.com/juaneseluma111-prog
"""

import nmap, sys, json
from datetime import datetime

HIGH_RISK = {
    445: "SMB - ransomware vector",
    3389: "RDP - brute force target",
    23: "Telnet - unencrypted",
    21: "FTP - plaintext credentials"
}
MED_RISK = {
    80: "HTTP - unencrypted",
    8080: "HTTP Alt",
}

def scan(target):
    nm = nmap.PortScanner()
    print(f"\n[*] Scanning {target}... please wait\n")
    nm.scan(hosts=target, ports="21,22,23,25,80,443,445,3389,8080",
            arguments="-sV -T4")
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                if nm[host][proto][port]['state'] == 'open':
                    svc = nm[host][proto][port]['name']
                    ver = nm[host][proto][port]['version']
                    risk = "HIGH" if port in HIGH_RISK else "MEDIUM" if port in MED_RISK else "LOW"
                    desc = HIGH_RISK.get(port, MED_RISK.get(port, "Review exposure"))
                    results.append({
                        "port": port,
                        "service": svc,
                        "version": ver,
                        "risk": risk,
                        "desc": desc
                    })
    return results

def report(target, results):
    icons = {"HIGH": "[!!!]", "MEDIUM": "[ ! ]", "LOW": "[   ]"}
    print("=" * 55)
    print(f"  SCAN REPORT — {target}")
    print(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 55)
    if not results:
        print("  No open ports found.")
    for p in results:
        print(f"  {icons[p['risk']]} Port {p['port']} - {p['service']} {p['version']}")
        print(f"         {p['risk']}: {p['desc']}")
    fname = f"report_{target.replace('.','_')}.json"
    with open(fname, "w") as f:
        json.dump({"target": target, "results": results}, f, indent=2)
    print(f"\n[+] JSON report saved: {fname}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <IP>")
        sys.exit(1)
    r = scan(sys.argv[1])
    report(sys.argv[1], r)
