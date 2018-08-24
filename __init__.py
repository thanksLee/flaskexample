from flask import Flask, render_template, flash, request, url_for, redirect
from source.content_management import content

TOPIC_DIC = content()

app = Flask(__name__)

#builtins.RuntimeError - 아래의 에러 발생시 config에 secert_key 를 추가
#RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
app.config["SECRET_KEY"] = "hard to guess string"

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/dashboard/")
def dashboard():
    #flash("1 flash test!!!!!!!!!!!!!!!!")
    return render_template("dashboard.html", TOPIC_DIC=TOPIC_DIC)

@app.route("/slashboard/")
def slashboard():
    try:
        return render_template("slashboard.html", TOPIC_DIC=TOPIC_DIC)
    except Exception as e:
        return render_template("error/500.html", error=e)

# mehods를 제거하면 405 에러가 발생
@app.route("/login/", methods=["GET", "POST"])
def login_page():
    lv_error = ""
    lv_username = ""
    lv_password = ""
    try:
        if request.method == "POST":
            lv_username = request.form["username"]
            lv_password = request.form["password"]

            flash(lv_username)
            flash(lv_password)

            if lv_username == "admin" and lv_password == "password":
                return redirect(url_for("dashboard"))
            else:
                lv_error = "Invalid credentials. Try Again."
        return render_template("login.html", error=lv_error)
    except Exception as e:
        lv_error = e
        flash(lv_error)
        return render_template("login.html", error=lv_error)

# S : 에러 처리
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html")

@app.errorhandler(405)
def method_not_found(e):
    return render_template("error/405.html")

# E : 에러 처리

if __name__ == "__main__":
    app.run(debug=True)
