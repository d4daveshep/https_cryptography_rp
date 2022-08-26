from flask import Flask

MESSAGE = "shhhh, this is secret"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return MESSAGE + "\n"

if __name__ == "__main__":
    app.run(port=5684)  # run the flask dev server - don't use in production



