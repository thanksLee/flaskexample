# flaskexample
Python Flask Example
```
- Flask 정리 - 1
```

#### 윈도우에 Python 설치
***
> 1.windows에서 python 개발
```
- https://www.python.org/downloads/release/python-370/
- python 설치 : 3.7
- pip install --upgrade setuptools
- pip install virtualenv
```

#### Flask 내용 정리
***
> 1.pip 명령어
```
- PyPI(python Package Index) : 파이썬 패키지를 설치하는 프로그램(주로 커맨드 창이나 쉘에서 사용)
```
> 2.Flask 전체적인 흐름
```
- User 호출 -> Flask Framework (route) -> View 함수 -> Business Logic 처리 -> Jinja2 Template -> User에게 전달
```
> 3.라우팅
```
- 라우팅 : 복잡한 URI를 쉽게 처리하도록하는 기능
- Flask에서는 route() 데코레이터(@)를 사용한다.  
- @app.route("/hello") vs @app.route("/hello/") 차이점
  > 예제 :  ex02.py
  > 전자 : @app.route("/hello")
    http://127.0.0.1:5000/hello   -> 정상 출력
    http://127.0.0.1:5000/hello/  -> Not Found 404 Error
  > 후자 : @app.route("/hello/")
    http://127.0.0.1:5000/hello   -> 정상 출력
    http://127.0.0.1:5000/hello/  -> 정상 출력
  즉, 뒤에 '/' 이 있고 없고에 따라서 Not Found 춮력

- uri 변수 처리
  > 예제 :  ex03.py, ex04.py
  > @app.route("/user/<userName>")
  > @app.route("/post/<int:post_id>")
```
> 4.templates 사용
```
- render_template
  > 예제 : ex05.py
    * templates 디렉토리를 생성하여 html을 넣어 사용한다.
    * 하위에 디렉토를 생성하면 해당 디렉토리/파일명 하면 된다.
- teste_request_context() : Flask에 있는 메소드이며, HTTP요청을 테스트 할 수 있는 메소드
- url_for() 메소드 이용
  > 예제 : ex06.py
  > url_for(메소드명)
```
> 5.웹프로그램의 통신
```
- 모든 웹프로그램은 사용자가 웹 브라우저를 이용해서 웹프로그램이 가지고 있는
  자원(상품정보, 강좌 목록(동영상)..) 을 요청하면 웨브라우저가 이해할 수 있는
  형태로 재가공하거나, 자원 그대로 웹프라우저에게 반환해준다.
  > Client(Web Browser) <-> Web Server(Apache, Tomcat) <-> Web Programming(Jsp, PHP) <-> database
- 웹서버와 웹브라우저간에 발생하는 자원 반환 단계에서는 웹서버가 콘텐츠 협상(contents negitiation) 이라는
  단계를 거천 후에 웹브라우저에 결과를 반환한다.
  이 단계는 웹브라우저가 무엇을 처리할 수 있는지 웹서버와 협상하는 단계
  이 단계는 3가지로 분류 할 수 있다. 
  1) 서버 기반의 협상 
     > 웹서버가 웹프라우저에 반환할 데이터의 형태를 직접 결정
  2) 에이전트(캐시서버) 기반의 협상
     > 웹 서버가 응답할 데이터 처리 형태를 결정하기 위하여 첫번째 수신을 처리한 에이전트에 의해 형태를 결정.
  3) 투명한 협상(1, 2를 혼합한 협상)
- 협상에 필요한 HTTP 메시지 헤더
  > Accept : 브라우저가 처리할 수 있는 데이터의 형태, 선호도
             text/html
  > Accept-Language : 브라우저가 수용할 수 있는 응답결과의 언어와 선호도
  > Accept_Encoding : 브라우저가 수용할 수 있는 응답 인코딩 형태와 선호도.  
  > Key : Value 형태로 관리.
```