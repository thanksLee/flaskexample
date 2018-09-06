from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World</h1>"

# String 타입의 userName 파라메터 (String type은 기본)
@app.route("/user/<userName>")
def show_uwer(userName):
    return "user %s" % userName


# int type의 post_id 파라메터
@app.route("/post/<int:post_id>")
def show_psot(post_id):
    return "Post %d" % post_id

# float type의 pi 파라메터
@app.route("/circle/<float:pi>")
def show_pi(pi):
    return "PI %f" % pi


if __name__ == "__main__":
    app.run(debug=True)
