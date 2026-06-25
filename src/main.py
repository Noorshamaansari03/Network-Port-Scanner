"""
Project: TCP Port Scanner
Author: Noorshama Ansari
"""

import socket
import time
from colorama import init, Fore

init(autoreset=True)

SERVICES = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP Proxy"
}


def banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "              TCP PORT SCANNER v1.0")
    print(Fore.CYAN + "         Network Reconnaissance Utility")
    print(Fore.CYAN + "=" * 60)


def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    result = scanner.connect_ex((target, port))
    scanner.close()

    if result == 0:
        service = SERVICES.get(port, "Unknown Service")
        return port, service

    return None


def main():

    while True:

        banner()

        target = input("\nEnter Target IP Address: ")

        start_port = int(input("Enter Start Port: "))
        end_port = int(input("Enter End Port: "))

        print(Fore.YELLOW + "\nScanning...\n")

        start_time = time.time()

        open_ports = []

        for port in range(start_port, end_port + 1):

            result = scan_port(target, port)

            if result:
                open_ports.append(result)

                print(
                    Fore.GREEN +
                    f"[✔] Port {result[0]:<5} {result[1]}"
                )

        end_time = time.time()

        print(Fore.CYAN + "\n" + "-" * 60)

        print(f"Open Ports Found : {len(open_ports)}")
        print(f"Scan Time        : {end_time - start_time:.2f} seconds")

        if len(open_ports) == 0:
            print(Fore.RED + "\nNo open ports found.")

        with open("report.txt", "w") as report:

            report.write("TCP PORT SCANNER REPORT\n")
            report.write("=" * 50 + "\n")
            report.write(f"Target IP : {target}\n")
            report.write(f"Port Range : {start_port}-{end_port}\n\n")

            if open_ports:
                report.write("Open Ports\n")
                report.write("-" * 30 + "\n")

                for port, service in open_ports:
                    report.write(f"Port {port:<5} {service}\n")

            else:
                report.write("No open ports found.\n")

            report.write("\n")
            report.write(f"Total Open Ports : {len(open_ports)}\n")
            report.write(f"Scan Time : {end_time - start_time:.2f} seconds\n")

        print(Fore.GREEN + "\nResults saved to report.txt")

        choice = input("\nScan another host? (Y/N): ").strip().upper()

        if choice != "Y":
            print(Fore.CYAN + "\n" + "=" * 60)
            print(Fore.GREEN + "Thank you for using TCP Port Scanner.")
            print(Fore.GREEN + "Stay Safe! 🔒")
            print(Fore.CYAN + "=" * 60)
            break

        print("\n")


if __name__ == "__main__":
    main()