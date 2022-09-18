import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# only run once
password = input("Enter master password: ").encode()

def load_salt() :
    file = open("salt.key", "rb")
    salt = file.read()
    file.close()
    return salt

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=load_salt(),
    iterations=390000,
)

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)

with open("key.key", "wb") as key_file :
    key_file.write(key)
