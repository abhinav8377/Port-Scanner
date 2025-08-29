#!/usr/bin/env python3

"""
portscan - A simple multi-threaded TCP port scanner.
Author: Abhinav
"""

import socket
import argparse
import threading
from queue import Queue

BANNER = r"""
========================================================
|                                                      |
|         [[     PORTSCAN - TCP Port Scanner  ]]       |
|                                                      |
|         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       |
|                                                      |
|                Developed by Abhinav                  |
========================================================
"""

print_lock = threading.Lock()

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception as e:
        pass

def worker(host, q):
    while not q.empty():
        port = q.get()
        scan_port(host, port)
        q.task_done()

def main():
    print(BANNER) 

    parser = argparse.ArgumentParser(description="A simple multi-threaded TCP port scanner")
    parser.add_argument("host", help="Target host to scan (IP or domain)")
    parser.add_argument("-p", "--ports", help="Port range (default 1-1024), e.g., 20-100", default="1-1024")
    parser.add_argument("-t", "--threads", help="Number of threads (default 100)", type=int, default=100)
    
    args = parser.parse_args()

    try:
        start_port, end_port = map(int, args.ports.split("-"))
    except:
        print("[-] Invalid port range format. Example: -p 20-80")
        return

    print(f"\n[+] Starting scan on {args.host}")
    print(f"[+] Ports: {start_port}-{end_port}")
    print(f"[+] Threads: {args.threads}\n")

    q = Queue()
    for port in range(start_port, end_port+1):
        q.put(port)

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=worker, args=(args.host, q))
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()

    print("\n[+] Scan completed.")

if __name__ == "__main__":
    main()