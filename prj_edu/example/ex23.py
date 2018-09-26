from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    #GET 방식으로 요청이 들어 왔을때
    if request.method == "GET":
        return render_template("test_login.html")
    else:
        userEmain = request.form["email"]
        userPwd   = request.form["pwd"]
        # 실전에서는 userEmail, userPwd에 대한 유효성 검사가 필요하다. 여기서는 생략
        return "이메일 : " + userEmain + ", 비밀번호 : " + userPwd


if __name__ == "__main__":
    app.run(debug=True)