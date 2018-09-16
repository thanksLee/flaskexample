from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("super.html", mystring="템플릿 테스트ㅣㅣㅣㅣㅣㅣ", my_list=[11, 22, 33, 55, 666, 44])

if __name__ == "__main__":
    app.run(debug=True)

