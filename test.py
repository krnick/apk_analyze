import subprocess

output = subprocess.check_output("md5sum README.md |awk '{print $1}'",shell=True).strip()
output = str(output, encoding = "utf-8")

print(output)
