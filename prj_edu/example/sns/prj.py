from flask import Flask, render_template, request, session, url_for, redirect, g, flash
import MySQLdb as mysql
from contextlib import closing

SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return mysql.connect(host="localhost", user="devsns", passwd="devsns0!", db="db_sns")

#one=False : 로우를 몇개 가져올꺼냐에 대한 셋팅
def query_db(query, args = (), one=False):
   cur = g.db.execute(query, args)
   rv = [dict((cur.description[idx][0], value) for idx, value in  enumerate(row)) for row in cur.fetchall()]
   return (rv[0] if rv else None) if one else rv

#데이터베이스 초기화
#def init_db():
#    with closing(connect_db) as db: #with closing 블록이 끝나면 인자로 받은 객체를 닫거나 제거한다.
#        with app.open_resource()

def init_db():
    with closing(connect_db()) as db:
        db.commit()

# S : 후킹 처리

@app.before_request
def before_request():
    g.db = connect_db()
    g.user = None
    print("-- before_request")
    if "user_id" in session:
        g.user = query_db("select * from user where user_id = ?", [session["user_id"]], one=True)


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# E : 후킹 처리



@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    return render_template("register.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)