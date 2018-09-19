from flask import Flask, request

app = Flask(__name__)

@app.route("/test/environ", methods=['GET', 'POST'])
def test():
    # request의 environ 속성 : HTTP 통신에 사용하는 환경변수를 담고 있는 사전 (wsgi 전용 환경변수도 포함)
    strVal = ( "REQUEST_METHOD : %(REQUEST_METHOD)s<br/>"
               "PATH_INFO : %(PATH_INFO)s<br/>"
               "QUERY_STRING : %(QUERY_STRING)s<br/>"
               #"CONTENT_TYPE : %(CONTENT_TYPE)s<br/>"
               "SERVER_NAME : %(SERVER_NAME)s<br/>"
               "SERVER_PORT : %(SERVER_PORT)s<br/>"
               "SERVER_PROTOCOL : %(SERVER_PROTOCOL)s<br/>"
               "wsgi.version : %(wsgi.version)s<br/>"
               "wsgi.url_scheme : %(wsgi.url_scheme)s"
               )% request.environ

    return strVal

@app.route("/bhlee")
def exam():
    return request.method

if __name__ == "__main__":
    app.run(debug=True)