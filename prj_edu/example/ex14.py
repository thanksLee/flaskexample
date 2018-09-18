from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/aaa")
def aaa():
    return "request 객체를 이용한 변수 name 값은 {} 입니다.".format(request.args.get("name"))

@app.route("/bbb")
def bbb():
    #nameVal = request.args.get("name", "asdfasdfad")
    nameVal = request.args.get("name", "100", int)
    return str(nameVal)

@app.route("/abab")
def abab():
    return request.values.get("name", default="전달된 데이터가 없습니다.")

# 사용자 정의 함수 (특정 날짜 형식을 지정하는 함수)
def userDateType(date_format):
    def changeFormat(date_string):
        # strptime(date_string, format) : format 맞는 date_string을 datetime 객체로 리턴하는 메소드
        return datetime.strptime(date_string, date_format)
    return changeFormat


@app.route("/ccc", methods=['GET', 'POST'])
def ccc():
    print(request.values.get('date', default='2018-05-11', type=userDateType('%Y-%m-%d')))
    return "콘솔을 통해서 확인해보세요"


class userDataType:
    def __init__(self, format):
        self.format = fromat
    # *args : 가변인자, **kwargs : 키워드 인자
    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0], self.format)


@app.route("/ddd", methods=['GET', 'POST'])
def ddd():
    print(request.values.get("date", "2018-09-12", userDateType("%Y-%m-%d")))
    return "콘솔에서 확인 바랍니다."


@app.route("/eee", methods=['GET', 'POST'])
def eee():
    print(request.values.getlist("dates", type=userDateType('%Y-%m-%d')))
    return "콘솔에서 확인 바랍니다."



if __name__ == "__main__":
    app.run(debug=True)
