from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/cookie_set")
def cookieSet():
    res = Response("Cookie 생성")
    res.set_cookie("cname", "Flask Study")
    return res


@app.route("/cookie_out")
def cookieOut():
    res = Response("Cookie 삭제")
    res.set_cookie("cname",  expires=0)
    return res


@app.route("/cookie_status")
def cookieStatus():
    return "cname 쿠키는 %s 값을 가지고 있습니다."% request.cookies.get('cname', '')


if __name__ == "__main__":
    app.run(debug=True)