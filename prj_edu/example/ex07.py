from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hell():
    return "<h1> Hello world </h1>"

@app.route("/user/<username>")
def user(username):
    return render_template("ex02.html", name=username)


if __name__ == "__main__":
    app.run(debug=True)