import os

# only run once
# file open modes w r a wb, write read append writeinbytes
# w mode always clears entire file, a mode is appends to end existing file
# w or a mode creates new file if does not exist
# with keyword in fileopen automatically will close the file after doing the operation
salt = os.urandom(16)
print(salt)

with open("salt.key", "wb") as key:
    key.write(salt)