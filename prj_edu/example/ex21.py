from flask import Flask, request, Response, redirect, make_response, url_for, jsonify


app = Flask(__name__)


def index():
    return "Hello, Flask !!!"

app.add_url_rule("/", "", index)

app.secret_key = "bhlee12340!"

def reindex():
    res = make_response("<h1> Hello, Flask!!! </h>")
    return res

app.add_url_rule("/reindex", "reindex", reindex)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session["username"] = request.format["username"]
        return redirect(url_for("index"))
    return "<h2>로그인</h2>" \
           "<form method='post'>" \
            "<p><input type='text' name='username'></p>" \
            "<p><input type='submit' value='login'></p>" \
           "</form>"


works = [
    {"id":100,
     "title":"식품구매",
     "description":"우유, 치즈, 과일, 피자",
     "done":False
     },
    {"id": 200,
     "title": "플라스크배우기",
     "description": "웹프로그래밍",
     "done": False
     }
]

@app.route("/json", methods=["GET"])
def get_works():
    return jsonify(works)

@app.route("/req")
def res():
    return "/req"


@app.before_first_request
def before_first_request():
    print("앱이 실행하고 나서 첫번째 HTTP 요청에만 응답한다.")


@app.before_request
def before_request():
    print("매번 HTTP 요청이 처리되기 전에 실행된다.")


@app.after_request
def after_request():
    print("매번 HTTP 요청이 처리되고 나서 실행된다.")
    return

if __name__ == "__main__":
    app.run(debug=True)