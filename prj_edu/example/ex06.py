from flask import Flask, url_for

app = Flask(__name__)

@app.route("/hello/")
def hello():
    return "<h1>Hello, World!!!</h1>"


@app.route("/user/<username>")
def get_user(username):
    return "user : " + username


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for("hello"))
        print(url_for("get_user", username="bhlee"))
