from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout2.html", title="Home", mybody="메인페이지")

@app.route("/home")
def home():
    return render_template("layout2.html", title="Home", mybody="메인페이지")


@app.route("/about")
def about():
    return render_template("layout2.html", title="About", mybody="회사 소개")

@app.route("/contact")
def contact():
    return render_template("layout2.html", title="Contact Us", mybody="문의 페이지")

if __name__ == "__main__":
    app.run(debug=True)