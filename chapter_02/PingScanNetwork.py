import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description="Ping Scan Network")
parser.add_argument(
    "-network",
    dest="network",
    help="Network segment [for example 192.168.1]",
    required=True,
)
parser.add_argument(
    "-machines", dest="machines", help="Number of machines", type=int, required=True
)
args = parser.parse_args()

for ip in range(1, args.machines + 1):
    ip_address = f"{args.network}.{ip}"
    print(f"scanning {ip_address}")
    if sys.platform.startswith("linux"):
        output = subprocess.Popen(
            ["/bin/ping", "-c 1", ip_address], stdout=subprocess.PIPE
        ).communicate()[0]
    elif sys.platform.startswith("win"):
        output = subprocess.Popen(
            ["ping", ip_address],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()[0]
    elif sys.platform.startswith("darwin"):
        output = subprocess.Popen(
            ["ping", "-c 1", ip_address], stdout=subprocess.PIPE
        ).communicate()[0]
    output = output.decode("utf-8")
    if "Lost 0" in output or "bytes from" in output:
        print(f"The ip address {ip} has responded with an ECHO_REPLY!")
