# Python Network Vulnerability Scanner

Automated network reconnaissance and vulnerability assessment tool.
Part of my cybersecurity portfolio.

## Features
- Automated port scanning using Nmap
- Risk classification (HIGH/MEDIUM/LOW) per open port
- Service and version fingerprinting
- JSON report generation

## Requirements
- Python 3.8+
- Nmap installed (nmap.org)
- python-nmap library

## Installation
pip install -r requirements.txt

## Usage
python scanner.py <target_ip>
python scanner.py 192.168.56.102

## Example Output
[!!!] Port 3389 - ms-wbt-server
      HIGH: RDP - brute force target
[!!!] Port 445 - microsoft-ds
      HIGH: SMB - ransomware vector

## Screenshots
![Scan Result](screenshots/scan-result.png)
![Windows Server Scan](screenshots/windows-scan.png)

## Skills Demonstrated
- Python scripting for security automation
- Network security concepts
- Risk assessment methodology
- Tool development and documentation

*Juan Esteban Umana Machado — linkedin.com/in/juanesumaa11*