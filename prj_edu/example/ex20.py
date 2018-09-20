from flask import Flask, request, session

app = Flask(__name__)


app.secret_key = "kk1235"

@app.route("/session")
def sessionSet():
    session["ID"] = "Flask Session Test"
    return "세션을 설정했습니다."


@app.route("/session_out")
def sessionOut():
    del session["ID"]
    return "세션을 제거하였습니다."


app.config.update(
    SECRET_KEY="IJJ1234",
    SESSION_COOKIE_NAME="",
    PERMANENT_SESSION_LIFETIME=""
)

if __name__ == "__main__":
    app.run(debug=True)