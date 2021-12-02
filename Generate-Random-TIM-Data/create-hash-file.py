import hashlib 
import string
import random

COUNT = 10000

hashes = []

for i in range(0, COUNT):
    rand = random.choice(string.ascii_letters) + str(i)
    sha256 = hashlib.sha256(rand.encode()).hexdigest()
    hashes.append(sha256)

with open("hashes.txt", "w") as f:
    f.write("\n".join(hashes))

