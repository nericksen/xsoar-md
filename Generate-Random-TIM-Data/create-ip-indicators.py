import requests
import ipaddress

# Disable insecure https warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CIDR = "10.2.2.0/28"
BASE_URL = "https://<XSOAR-Base-URL>:443"
API_KEY = "<API_KEY>"

ips = [str(ip) for ip in ipaddress.IPv4Network(CIDR)]

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": API_KEY
}

body = {
    "indicator": {
        "indicator_type": "IP",
        "value": "1.2.3.10",
        "score": 2,
        "CustomFields": {
            "tags": ["api-test-data"],
            "mitretactics": "Test Mitre Tactic",
            "orglevel1": "Test Organization",
            "region": "Some Test Region",
            "registrantcountry": "Some Test Registrant Country",
            "registrantemail": "testregistrantemail@youremail.com",
            "registrantname": "Test Registrant Name",
            "registrantphone": "PhoneNumber",
            "shortdescription": "This is the short description of a test indicator.",
            "trafficlightprotocol": "RED"
        }
    }
}

for ip in ips:
    body["indicator"]["value"] = ip

    try:
        res = requests.post(f"{BASE_URL}/indicator/create", headers=headers, json=body, verify=False)
        if res.ok:
            print(f"Success: {ip} ")
            #print(res.json())
        else:
            print(f"Failure: {ip} Status_Code: {res.status_code}")
    except Exception as e:
        print(f"Failure: {ip} Error: {e}")
        continue
