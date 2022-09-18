from cryptography.fernet import Fernet
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def load_salt() :
    fhand = open("salt.key", "rb")
    salt = fhand.read()
    fhand.close()
    return salt

def load_key() :
    fhand = open("key.key", 'rb')
    key = fhand.read()
    fhand.close()
    return key

def pass_key(password) :
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=load_salt(),
        iterations=390000,
    )
    pass_key = base64.urlsafe_b64encode(kdf.derive(password))
    return pass_key

def check(password) :
    return pass_key(password) == load_key()

def fer() :
    f = Fernet(load_key())
    return f

def view() :
    count = 0
    fhand = open("passwords.txt", "r").readlines()
    print("\nnum, account, userid, password")
    for line in fhand :
        count += 1
        account, userid, password = line.split("|")
        password = fer().decrypt(password.encode()).decode()
        print(f"{count}, {account}, {userid}, {password}")
    
def add() :
    account = input("Enter account name: ")
    userid = input("Enter userid: ")
    password = input("Enter password: ")
    password = fer().encrypt(password.encode()).decode()

    # append and not w mode as it will clear existing records
    with open("passwords.txt", "a") as fhand :
        fhand.write(account + "|" + userid + "|" + password + "\n")
    print("\nDetails saved successfully.")
