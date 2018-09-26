from flask import Flask, request, Response, redirect, make_response, url_for, jsonify, render_template, current_app, g


app = Flask(__name__)


@app.route("/")
def cont():
    aa = dir(current_app)
    return "Hello Flask!! <br/>" + "<br/>". join(aa)

@app.route("/hi")
def hi() :
    return "Hi!!!" + g.test

@app.before_request
def before_request():
    g.test = "before request"
    print("before request")


@app.teardown_request
def teardown_request(exception):
    print(app.app_context()) # app_context() 메소드는 application context를 반환하는 메소드
    print("end request")


if __name__ == "__main__":
    app.run(debug=True)
