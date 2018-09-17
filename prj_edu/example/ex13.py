from flask import Flask, redirect

app = Flask(__name__)

@app.route("/aaa/<bbs_id>")
@app.route("/aaa", defaults={'bbs_id':100})
def aaa(bbs_id):
    return "aaa 의 {}번 글입니다.". format(bbs_id)

@app.route("/bbb", redirect_to="/new_aaa")
def bbb():
    return "/bbb로 호출한 페이지 입니다. "

@app.route("/new_aaa")
def new_aaa():
    return "/new_aaa로 호출한 페이지 입니다."

def redirect_new_bbb(adapter, p1, p2):
    return "/new_bbb/{0}/{1}".format(p1, p2)

@app.route("/ccc/<p1>/<p2>", redirect_to=redirect_new_bbb)
def re_aaa(p1, p2):
   return "/ccc/p1/p2로 호출되는 페이지 입니다."

@app.route("/new_bbb/<p1>/<p2>")
def new_re_bbb(p1, p2):
    return "/new_re_bbb/{0}/{1}로 호출되는 페이지 입니다. ".format(p1, p2)


if __name__ == "__main__":
    app.run(debug=True)
