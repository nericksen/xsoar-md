import requests
import ipaddress

# Disable insecure https warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CIDR = "10.2.2.0/28"

ips = [str(ip) for ip in ipaddress.IPv4Network(CIDR)]

with open("ips.txt", "a") as f:
    f.write("\n".join(ips))
