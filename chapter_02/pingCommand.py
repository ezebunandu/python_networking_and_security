import subprocess
import sys
import shlex

p = subprocess.Popen(
    shlex.split("/sbin/ping -c 1 www.google.com"),
    shell=False,
    stderr=subprocess.PIPE,
)
out = p.stderr.read(1)
sys.stdout.write(str(out.decode("utf-8")))
sys.stdout.flush()
