# libraries
import os
import random
import binascii #conversion library

# variables ⸻ file management
file = "hdd/igprofile.png"
filesize = os.path.getsize(file)
truncsize = int(filesize * (96 / 100)) #4% to truncate
removedweight = int(filesize * (2 / 100)) #2% to add

# code
with open(file, "rb+") as f:
    f.seek(0)
    f.truncate(truncsize) #rm 2% from file total size

print("decompositing")