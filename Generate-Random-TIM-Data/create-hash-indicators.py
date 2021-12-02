import requests
import hashlib 
import string
import random

# Disable insecure https warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

COUNT = 10
BASE_URL = "https://<xsoar-url>:443"
API_KEY = "<api-key>"


hashes = []

for i in range(0, COUNT):
    rand = random.choice(string.ascii_letters) + str(i)
    sha256 = hashlib.sha256(rand.encode()).hexdigest()
    hashes.append(sha256)


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": API_KEY
}


body = {
    "indicator": {

        "indicator_type": "File",
        "value": "e20f6f09c0361630ae68e5075723c7b3daa6718828d103c8fa1fb7e3c41ae67d",
        "lastSeen": "2021-11-29T18:54:43.784350055Z",
        "firstSeen": "2021-11-29T18:54:43.784350055Z",
        "score": 3,
        "CustomFields": {
            "orglevel1": "Some random org level",
            "orglevel2": "another random org level",
            "orglevel3": "yet again some nonsense",
            "orgunit": "top level",
            "shortdescription": "This is a short description of a hash that has been randomly generated letter and count hashed by some python built in library. yay python!",
            "trafficlightprotocol": "RED",
            "xdrstatus": "enabled"
        },
        "expirationStatus": "active"
    }    
}

session = requests.Session()

success_counter = 0
failure_counter = 0

print("Generating Random Hashes")
for h in hashes:
    body["indicator"]["value"] = h

    try:
        #res = requests.post(f"{BASE_URL}/indicator/create", headers=headers, json=body, verify=False)
        res = session.post(f"{BASE_URL}/indicator/create", headers=headers, json=body, verify=False)
        if res.ok:
            #print(f"Success: {h} ")
            print(".", end="", flush=True)
            success_counter += 1
            continue
            #print(res.json())
        else:
            print(f"Failure: {h} Status_Code: {res.status_code}")
            failure_counter += 1
    except Exception as e:
        print(f"Failure: {h} Error: {e}")
        failure_counter += 1
        continue

print("\n")
print(f"Success: {success_counter}")
print(f"Failed: {failure_counter}")
