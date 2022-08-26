import os

import requests
from cryptography.fernet import Fernet

# SECRET_KEY = os.environb[b"SECRET_KEY"]
SECRET_KEY = b"RD8L40ChkTllQ2Qh5-VhhXnlKYf8Ru1Jkiweb1mlXsA="
my_cipher = Fernet(SECRET_KEY)

def get_secret_message():
    response = requests.get("http://127.0.0.1:5684")
    encrypted = response.content

    decrypted = my_cipher.decrypt(encrypted)
    decrypted = decrypted.decode("ascii")
    print(decrypted)

if __name__ == "__main__":
    get_secret_message()
