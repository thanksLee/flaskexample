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
- routing 옵션
  > HTTP 메서드 중 GET, POST가 대표적이다.
  > GET, POST이외에도 PUT, DELETE, HED, OPTIONS 메서드가 있는데, 이러한 타입들은 REST API개발시에 주로 사용된다.
  > 웹 프로그램에 지원을 요청하는 대표적인 방법은 GET 방식이다. 
    * GET 형식은 웹브라우저의 주소 입력란에 전달하고자 하는 정보가 노출되기때문에 중요한 정보 전달을 할때는 사용하지 않는다.
    * POST 형식은 HTTP 메시지의 BODY에 데이터를 포함해서 전달한다. 따라서 많은 양의 데이터를 전달을 할때 사용하며,
      HTTPS를 사용하는 웹서버는 전달하는 데이터가 중요하기때문에 암호화 처리되어 전달.
    * 사용
      @app.route("/aurl", methods=['GET']) 일반적으로 GET방식은 생략
      @app.route("/burl", methods=['POST'])
      @app.route("/curl", methods=['GET', POST'])
      
      + route 데코레이터에 methods 인자가 없으면 뷰함수는 GET 요청만 처리된다.
      + 
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
- 예제 : ex08.py, ex09.py,  ex10.py, ex11.py, ex12.py
- Flask 설치할 때 같이 설치되기 때문에 추가 설치 할 필요가 없다.
- Flask의 템플릿 파일들은 기본적으로 /templates/ 폴더에 저장한다.
- Jinja2는 탭, 공백문자, 개행문자를 제거하지 않고 그대로 둔다.
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
    * 블록을 여러개 사용할때 endblock에 이름을 줄 수 있다.
      단, block의 명과 endblock의 명은 같아야 한다.
- Super block
  > super를 호출하여 부모 블록의 내용을 렌더링 하는 블록, 부모블록의 결과를 반환한다.
    즉, 부보가 갖고 있는 block을 호출하여 사용한다.
- 공백 제거
  > {% block %} 블록 선언의 % 에 {%- 공백제거, -%} 공백제거 를 한다. 
    - {% - (X), {%- (0) 사이에 공백이 있으면 안된다.!!! 
- escape
  > 어떤 조건이나 환경에서 특별한 구문이나 의미로 해석되는 문자열로부터 그 의미를 제거하여
    일반적인 문자열로 처리하는 것
  > Jinja2에서는 홑따옴표를 이용하여 escape처리를 한다.
    ex) {{ '}}' }}
  > 큰 범위를 escape처리를 하고자 할경우는 raw 구문을 이용.
    템플릿 코드를 예제로 만들어서 보여주고자 할 경우는 raw를 이용하여 작성한다.ㄴ
- macro
    > 일반적인 프로그래밍 어어의 함수와 같다.
      <p><input type = "text" name = "username" value="" size = "30"></p>    
      <p><input type = "password" name = "password" value="" size = "30"></p>
      위의 템플릿 코드를 아래와 같이 매크로로 만들어서 필요한 곳에 호출하여 사용한다.
    > 일반적인 매크로의 구문
    > {%  macro <매크로 이름>(매크로 인자, ...) %}
         <실행코드> 
      {% endmacro %}
    > macro를 정의한 템플릿과 macro를 사용하는 템플릿이 서로다를경우에는 import 명을 이용하여 불러온다.
      1) {% from "macro.html" import input %}
         * python import 처럼 사용 가능
      2) {% import 'macro.html' as input_macro %}
         <p> {{ input_macro.input('username') }} </p>
         <p> {{ input_macro.input('password', type='password') }} </p>
         * alias를 사용하여 사용 가능
    > macro의 특별 변수
      * varargs : macro가 추가로 받은 가변 인자를 참조할때 사용하며, 리스트 형태의 인자.
      * kwargs : macro가 추가로 받은 키워드 인자를 참조할때 사용하면 사전 형태의 인자
      * caller : macro를 호출한 call 블록을 호충하기 위해서 사용하며 macro가 call 블록에서
                 호출 되었을때만 사용가능
    > macro에서 제공하는 meta 정보(객체속성)
      매크로 바디에서 매크로 객체를 참조할때는 매크로 이름을 이용하여 참조한다.
      * name : 매크로 객체의 이름
      * arguments : 매크로에 선언되어 있는 파라미터 목록(튜플로 반환)
      * default : 매크로 인자가 받는 기본값 목록(튜플로 반환)
      * catch_kwargs : 매크로 바디에서 키워드 인자를 참조하면 True를 반환하고, 참조하지 않으면 False로 반환
      * catch_varargs : 매크로 바디에서 가변 인자를 참조하면 True를 반환하고, 참조하지 않으면 False를 반환
      * caller : 매크로를 호출한 영역이 call 블록이면 True를 반환하고, 그렇지 않으면 False를 반환
- call block  : call 명령을 이용해서 매크로를 호출한 경우 해당 블록을 call 블록이라 한다.
  {% call 매크로 %}
     매크로를 호출했을때 포함할 내용
  {% endcall %}
  매크로 내부에서 {{ caller() }} 기술한다.
  이때 caller()블록 바디에 있는 내용을 가져온다.
  > 인자를 받는 call 블록 선어하기
    {% call(args) 매크로명 %}
        call이 받은 인자를 처리한다.
    {% endcall %}
```