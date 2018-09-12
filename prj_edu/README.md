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
> 2.Flask
```
- 전체적인 흐름
  > User 호출 -> Flask Framework (route) -> View 함수 -> Business Logic 처리 -> Jinja2 Template -> User에게 전달
- 마이크로 프레임워크 (Micro Framework)
  > 파이썬 : Flask(WSGI 구현체인 Werkzeug와 템플릿 Jinja2), 루비 : 시나트라(Sinatra) - 마이크로플임워크의 원조
  > 웹 프로그래밍에 있어서 가장 핵심적인 요소만을 포함하고 있는 프레임워크
- 풀스택 프레임워크 (Fullstack Framework)
  > Django, Web2py, Turbogear
  > 웹프로그래밍을 할때 필요로하는 모든 것을 종하벅으로 갖추고 있는 프레임워크
    인증과 권한, ORM, 템플릿 라이브러리, 국제화화 지역화, 관리자, 보안 등의 여러요소를 갖춤
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
- HTTP 메시지는 요청(Request)메시지와 응답(Response)메시지로 나눈다.
- HTTP 요청 메시지 : 메서드(GET, POST), HTTP버전(HTTP/1.1), 호스트명, 웹브라우저가 무엇인지(User_Agent 헤더)   
                     어떤 언어(ko_KR, ko:en-US)/자원 형태를 받아들이는지 기록 
- HTTP 응답 메시지 : 첫행에는 HTTP 버전, HTTP 상태코드(200:성공), 상태코드 문자열 OK
                     두번째 행부터는 순서없이 정보를 기술한다. 날짜, 서버의 종류,사용자 정의 헤더도 포함된다.
                     X-로 시작하는 헤더명은 사용자 정의 헤더라고 본다.
                     (사용자 정의 헤더는 웹프로그램과 웹브라우저가 해석할수 있을때 의미있는 정보가 된다.)
- 파이썬을 위한 웹프로그램의 통신규약
  > 웹프로그램은 사용자가 보낸 요청과 요청을 처리한 결과를 웹서버를 경유해서 주고받는다.
    이때 웹서버와 웹프로그램간의 메시지를 주고 받기 위한 약속이 필요한데 이 약속을 CGI (Common Gateway Interface)  규약이라 한다.
  > CGI (Common Gateway Interface) : 환경변수나 표준 입출력을 다룰수 있는 언어라면 모두 사용가능하지만,
                                  실행속도나 개발 편의성을 고려하여 200년대 초까지는 대부분 펄(Perl) 언어를 사용하였다.
  > 소스코드의 보안성을 위해 C, C++, 델파이와 같은 언어를 사용하는 경우도 있는데, 이 언어들은 웹에
    특화된 언어가 아니기에 유지보수나 프로그램작성에 어려움이 있다.
  > 파이썬은 CGI 모듈을 통해 CGI  환경변수와 CGI 표준 입출력에 직접 액세스해서 웹프로그램을 작성할 수 있다.
  > 웹프로그램은 웹서버와는 독립적이어야 하는데 파이썬은 WSGI(Web Server Gateway Interface) 표준을 지켜 독립성을 구현해 준다.
  > WSGI 표준을 따르면 웹서버의 종류와는 상관없이 동작이 된다.
- ** flask는 Werkzeug(벡자이그) 기반으로 작성된다.
- 벡자이그는 WSGI 코어와 URL 라우팅을 지원하고 있다.                         
```
> 6.Jinja2 템플릿 엔진
```
- 예제 : ex08.py, ex09.py,  ex10.py
- Flask 설치할 때 같이 설치되기 때문에 추가 설치 할 필요가 없다.
- Flask의 템플릿 파일들은 기본적으로 /templates/ 폴더에 저장한다.
- Jinja2에서 템플릿 표현식
  > {% : 템플릿에서의 프로그래밍 영역을 넣기 위해 시작하는 기호 - block_start_string, 
  > %} : 템플릿에서의 프로그래밍 영역 기술을 끝내고 프로그래밍 여역을 조료하기 위해 사용하는 기호  - block_end_string (템플릿에서의 프로그래밍 영역을 넣기 위한 기호)
  > {{ : 변수를 출력하기 위해 시작하는 기호 - variable_start_string
  > }} : 변수 출력이 끝난고 나서 사용하는 기호 - variable_end_string
  > {# : 주석을 넣기 위해 시작하는 기호 - comment_start_string
  > #} : 주석을 넣고 종료하기위해 사용하는 기호 - comment_end_string
- 템플릿 상속
  > {% extends "<부모 템플릿 이름>" %}
  > {% block %} <대체할코드> {% endblock %}

```