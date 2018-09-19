from flask import Flask, request

app = Flask(__name__)

@app.route("/example/environ", methods=['GET', 'POST'])
def example():
    return ("path : %s<br/>"
            "url : %s<br/>"
            "base_url : %s<br/>"
            "url_root : %s<br/>"
            )% (request.path, request.url, request.base_url, request.url_root)


@app.route("/test/test", methods=['GET', 'POST'])
def test():
    return request.endpoint


if __name__ == "__main__":
    app.run(debug=True)