import os

from cryptography.fernet import Fernet
from flask import Flask

MESSAGE = "shhhh, this is secret"
app = Flask(__name__)

# SECRET_KEY = os.environb[b"SECRET_KEY"]
SECRET_KEY = b"RD8L40ChkTllQ2Qh5-VhhXnlKYf8Ru1Jkiweb1mlXsA="
my_cipher = Fernet(SECRET_KEY)


@app.route("/")
def get_secret_message():
    binary_message = MESSAGE.encode("ascii")
    return my_cipher.encrypt(binary_message)

if __name__ == "__main__":
    app.run(port=5684)  # run the flask dev server - don't use in production



