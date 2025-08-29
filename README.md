# port-scanner 🔍
A fast multi-threaded TCP port scanner built with Python.

## Features
- Multi-threaded for faster scans
- Custom port ranges
- Simple CLI usage
- Lightweight and dependency-free

## Installation
Clone the repository:
```bash
git clone https://github.com/<your-username>/portscan.git
cd portscan
```
## Usage 
```bash
python3 portscan.py <host> -p <start-end> -t <threads>
```
## Examples
```bash
# Scan default ports (1-1024)
python3 portscan.py example.com

# Custom range
python3 portscan.py 192.168.1.1 -p 20-100

# Increase threads
python3 portscan.py google.com -p 1-5000 -t 200
```
## Disclaimer ⚠️
This tool is created for educational and ethical purposes only.
Do not use it against targets you don’t have permission to scan.
