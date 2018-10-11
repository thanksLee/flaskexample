from flask import Flask, render_template, request, session, url_for, redirect, g, flash
#from flaskext.mysql import MySQL
import pymysql
from contextlib import closing
from hashlib import md5
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

#mysql = MySQL()

#app.config["MYSQL_DATABASE_HOST"] = "localhost"
#app.config["MYSQL_DATABASE_PORT"] = 3306
#app.config["MYSQL_DATABASE_DB"] = "db_sns"
#app.config["MYSQL_DATABASE_USER"] = "devsns"
#app.config["MYSQL_DATABASE_PASSWORD"] = "devsns0!"

#mysql.init_app(app)


def get_connect():
    return pymysql.connect(host="localhost", port=3306, db="db_sns", user="devsns", password="devsns0!", charset="utf8")

#one=False : 로우를 몇개 가져올꺼냐에 대한 셋팅
def query_db(query, args = (), one=False):
    g.cur.execute(query, args)
    rows = g.cur.fetchone()
    print(rows)
    return (rows if rows else None) if one else rows

#데이터베이스 초기화
#def init_db():
#    with closing(connect_db) as db: #with closing 블록이 끝나면 인자로 받은 객체를 닫거나 제거한다.
#        with app.open_resource()

def init_db():
    with closing(get_connect()) as db:
        db.commit()

# S : 후킹 처리

@app.before_request
def before_request():
    g.db = get_connect()
    g.cur = g.db.cursor(pymysql.cursors.DictCursor)
    g.user = None
    print("-- before_request")
    if "user_id" in session:
        g.cur.execute("select * from user where user_id = (%s)", [session["user_id"]])
        g.user = g.cur.fetchone()



@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# E : 후킹 처리

def get_user_id(username):
    sql = "select user_id from user where username = (%s)"
    g.cur.execute(sql, username)
    rows = g.cur.fetchone()
    print(rows['user_id'])
    return rows if rows else None

@app.route("/")
def twit_list():
    return render_template("twit_list.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        if not request.form["username"]:
            error = "사용자 이름을 입력하세요."
        elif not request.form["email"] or "@" not in request.form["email"]:
            error = "잘못된 이메일 형식이거나 이메일을 입력하지 않으셨습니다."
        elif not request.form["password"]:
            error = "비밀번호를 입력하세요."
        elif request.form["password"] != request.form["password2"]:
            error = "비밀번호가 일치하지 않습니다."
        elif get_user_id(request.form["username"]) is not None:  # 이미 등록된 사용자가 아닌지 검사하는 코드
            error = "이미 등록된 사용자 입니다."
        else:
            # 데이터베이스에 등록
            userid = datetime.now().strftime('%Y%m%d%H%M%S%f')
            print("userid : " + userid)
            sql = "INSERT INTO user(user_id, username, email, pwd_hash) values((%s), (%s), (%s), password((%s)))"
            # 비밀번호를 DB에 저장할 때 평문이 아닌 암호문으로 저장하기 위한 함수
            # 이때 해시 함수는 벡자이그에서 제공하는 함수이다. -> generate_password_hash()
            #print("pwd : " + generate_password_hash(request.form["password"]))
            #g.cur.execute(sql, [userid, request.form["username"], request.form["email"], generate_password_hash(request.form["password"])])
            g.cur.execute(sql, [userid, request.form["username"], request.form["email"], request.form["password"]])
            g.db.commit()

            flash("사용자 등록이 완료 되었습니다. 로그인을 하실수 있습니다.")
            return redirect(url_for("login"))
    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    if g.user:
        return redirect(url_for("twit_list"))
    error = None
    if request.method == "POST":
        # 유효성 검사
        sql = "select user_id, username, pwd_hash, password(%s) c_pwd from user where username = (%s)"
        user = query_db(sql, [request.form["password"], request.form["username"]], one=True)

        if user is None:
            error = "사용자 이름이 일치하지 않습니다. 다시 확인하세요."
        # check_password_hash() 함수는 해시화된 암호와 사용자가 입력한 평문형태의 암호를 비교하는 함수
        #두개의 값이 서로 일치하면 True, False
        elif not user["pwd_hash"] == user["c_pwd"]:
            error = "비밀번호가 일치하지 않습니다. 다시 확인하세요."
        else:
            flash("로그인 성공")
            session["user_id"] = user["user_id"]
            return redirect(url_for("twit_list"))
    return render_template("login.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)