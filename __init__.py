from flask import Flask, render_template, flash, request, url_for, redirect, session
from wtforms import Form
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart

from source.content_management import content
from source.dbconnect import connection

import gc

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

# methods를 제거하면 405 에러가 발생
@app.route("/login/", methods=["GET", "POST"])
def login_page():
    lv_error = ""
    lv_username = ""
    lv_password = ""
    try:
        if request.method == "POST":
            lv_username = request.form["username"]
            lv_password = request.form["password"]

            #flash(lv_username)
            #flash(lv_password)

            if lv_username == "admin" and lv_password == "password":
                return redirect(url_for("dashboard"))
            else:
                lv_error = "Invalid credentials. Try Again."
        return render_template("login.html", error=lv_error)
    except Exception as e:
        lv_error = e
        flash(lv_error)
        return render_template("login.html", error=lv_error)

class RegistrationForm(Form):
    username = TextField("Username", [validators.Length(min=4, max=20)])
    email    = TextField("Email", [validators.Length(min=4, max=50)])
    password = PasswordField("Password", [validators.Required(),
                                          validators.EqualTo('confirm', message="Passwords must match.")
                                          ])
    confirm    = PasswordField("Repeat Password")
    accept_tos = BooleanField("I accept the <a href='/tos/'>Terms of Service</a> and the <a href='/privacy/'>Privacy Notice </a>(Last updated Jan 15, 2018)", [validators.required()])


@app.route("/register/", methods=["GET", "POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)
        if request.method == "POST" and form.validate():
            username = form.username.data
            email    = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))

            c, conn = connection()

            x = c.execute("select * from users where username = (%s)", (thwart(username)))

            if int(len(x)) > 0:
                flash("That username is already taken, please choose another")
                return render_template("register.html", form=form)
            else:
                c.execute("insert into users(username, password, email, tracking) values(%s, %s, %s, %)",
                          (thwart(username), thwart(password), thwart(email), thwart("/introduction-to-pyton-programming/")))
                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session["logged_in"]  = True
                session["username"] = username

                return redirect(url_for('dashboard.html'))
        return render_template("register.html", form=form)

    except Exception as e:
        return(str(e))


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
