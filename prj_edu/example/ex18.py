from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def res():
    res = Response("응답 테스트 하기")
    res.headers.add("WebApp-Name",  "Flask-Test")
    return res

@app.route("/test")
def test():
    res = Response("응답 테스트")
    res.set_data("플라스크 학습하기")
    return res

@app.route("/cookie")
def cookie():
    res = Response("플라스크 학습하기")
    res.set_cookie("id", "Flask Study")
    return res

if __name__ == "__main__":
    app.run(debug=True)