import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]
    print(filename)

    if os.path.isfile(filename):
        print(f"[+] {filename} exist")
        exit(0)
    if not os.path.isfile(filename):
        print(f"[+] {filename} does not exist")
        exit(0)
    if not os.access(filename, os.R_OK):
        print(f"[+] {filename} does not exist")
        exit(0)
