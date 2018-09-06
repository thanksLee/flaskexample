from flask import Flask

app = Flask(__name__)

@app.route("/user/<userName>")
def get_uriName(userName):
    return "user : " + userName

if __name__ == "__main__":
    app.run(debug=True)