from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key="some_secret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/flash_login", methods=["GET", "POST"])
def flash_login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "secret":
            error = "invalid password"
        else:
            flash("로그인 성공")
            return redirect(url_for("index"))
    return render_template("flash_login.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)
