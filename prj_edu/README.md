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
  > pip install flask
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
  > 예제 : ex12.py, ex13.py
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
      + URL 변수에 기본값 할당하기
        @app.route("/aaa', defaults={'page':'index'})
        @app.route("/aaa/<page>")
        브라우저에서 /aaa/를 호출한 경우에는 /aaa/index 형태의 주소를 호출한 것과 같다.
- redirect_to
  > @app.route('/aaa', redirect_to='/new_aaa')
  > redirect_to 옵션에 다른 url이 아닌 함수를 전달하는 방법
    * 함수를 전달하기 위해서는 미리 함수를 정의 해둬야 한다.
    * 정의된 함수의 첫번째 인자는 adapter이어야 한다.
    
    url adapter -> 
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
- Jinja2에서 사용할 수 있는 전역 객체
  > config : 현재 어플리케이션에 등록된 설정 객체(flask.config)
  > request : 현재 요청된 객체(flask.request)
  > session : 현재 유지되고 있는 세션 객체(flask.session)
  > g : 전역변수로 사용되는 요청과 연결된 전역 객체(flask.g)
  > url_for : 함수에 대한 URL을 얻기 위해 사용하는 함수(flask.url_for)
  > get_flashed_messages : 뷰함수에서 flash함수를 사용해서 저장한 메시지를 얻어오는 함수(flask.get_flashed_message())
```
> 7.Request 객체 사용하기
```
- 예제 : ex14.py
- HTTP메시지 (request 메시지, response 메시지)
- HTTP 메시지는 평문 형태로 되어 있으며, 헤더와 바디로 구성되어 있다.
  이때 헤더와 바디의 구분은 빈줄로구분한다.
  > HTTP 메시지는 웹서버와 웹브라저간의 문자열 타입으로만 데이터를 주고 받는다.
- Flask에서 HTTP요청과 응답을 처리하기 위해서는 Request 객체와 Response 객체를 사용한다.
  > request.args에서 args는 GET 방식으로 전달된 데이터만 접근할 수 있다.
  > request의 value 속성은 GET 또는 POST 메서드로 데이터를 보냈을때 HTTP 메서드 타입에 상관없이 데이터를 읽을 수 있다.
    여기서 주의할 점은 GET, POST 가 동일한 변수명을 사용했을 경우 value 속성은 GET 메서드로 보낸 데이터를 우선으로 한다.
    주의!!!. 브라우저로부터 변수가 넘어오지 않을 경우 오류가 발생한다. 따라서 기본값을 설정한다.
    default 인자를 사용할수 있으며, 생략이 가능하다.
  > 프로그래머가 프로그래머가 반환 타입을 int객체로 변환하여 반환한다.
    ex) return request.values.get('name', 100, type=int) -> int 객체로 변환
    type의 값으로 파이썬에서 제공하는 기본 타입 이외에도 함수나 클래스(인스턴스)를 사용할 수 있다.
    즉, 사용자 정의 데이터 타입을 사용.
- 사용자 정의 타입이 클래스인 경우
  > get 메소스에서 datetime 객체를 사용하기 위해서는 __call__ 메소드를 정의 해야 한다.
- Flask 모듈에서 request 클래스를 가져온다.
- 같은 변수에 여러개의 값이 넘어오는 경우에는 리스트 타입으로 반환 해주면 된다.
  이때 사용하는 메소드는 getlist 이다. getlist 메소드는 default 인자를 사용하지 않는다.
```
> 8.MultiDict
```
- ex) ex15.py
- MultiDict 데이터타입 : GET과 POST 메서드로 넘어온 데이터(키, 값) 튜플 형태의 리스트타입d이다.
- MultiDict 타입에서 제공하는 메서드
- 명령어
  get, getlist, add, setlist, setdefault, setlistdefault, clear, copy, deepcopy, pop, poplist, update
  > add : MultiDit에 키와 값을 추가하는 메소드
  > setdefault : add메소드와 거의 비슷하게 동작하지만, 변수가 있을때는 그 변수의 값을 리턴하고
                 설정하고자 하는 변수가 없을때 default 값으로 데이터를 추가한다.
  > copy(얕은복사) : MultiDict 데이터의 변수값이 리스트 타입으로 있는 경우, 그 리스트 타입의 메모리 주소를 복사
  > deepcopy(깊은복사) : 리스트타입의 메모리 주소가 아니라, 그 데이터를 복사.
  > pop : get메소드와 유사한 동작을 하지만 기능적인 차이가 있다. (잘라내기)
          get메소드는 MultiDict 데이터 변수에서 특정 변수 키의 키값을 메모리에서 복사해서 프로그램에 리턴을 하는 반면에
          pop은 변수의 키 값을 복사하는 것이 아니라 MultiDict 데이터 변수에서 키를 제거하고 그 값을 리턴한다.
  > poplist : pop 메소드와 같은 동작을 하지만 같은 이름의 변수 키로 여러 값이 들어 올때 이 값들을 꺼내올때
              사용한다. getlist와 차이점은 값들을 꺼내온 뒤에 MultiDict 변수 키를 제거한다.
  > update : 기존의 MultiDict 타입의 변수에 다른 MultiDict 타입 변수의 내용을 삽입할때 사용
```
> 9.WSGI 표준 환경변수
```
- ex) ex16.py
- REQUEST_METHOD : 웹브라우저가 보낸 요청의 처리 방식에 대한 문자열 포함.
- SCRIT_NAME : 보통 생략한다. (FLASK에서는 보통 공란이다.)
               스크립트 파일명 표현  (Flask에서는 빈값으로 출력)
- PATH_INFO : URL 경로 ex) http://www.aaa.com/ccc/main -> PATH_INFO : /ccc/main
- CONTENT_TYPE : 웹브라우저가 보낸 HTTP 요청메시지의 바디에 포함되는 컨텐츠의 형태 저장
                 HTTP 헤더에 보면 Content-Type 값을 확인한다.
- SERVER_NAME : 서버의 도메인 주소(IP주소)가 저장. ex) http://www.aaa.com/ccc/main -> SERVER_NAME : www.aaa.com
- SERVER_PORT : 웹 어플리케이션이 동작하고 있는 서버 포트번호가 저장.
                ex) http://www.aaa.com:5000/env -> 5000번 저장, 도메인주소에 포트가 없으면 80 저장
- SERVER_PROTOCOL : 웹 어플리케이션이 동작하는 서버 프로토콜 버전 표시 (보통 Version HTTP/1.1
- QUERY_STRING : URL 끝에 보면 ? 문자 뒤에 오는 문자열 Query String이라고 한다. (보통 키 = 값) 형태로 지정
                키값이 두개 이상일때는 키사이에 &문자로 구분한다.
```
> 10.request
```
- ex16.py, ex17.py
- request의 environ 속성 : HTTP 통신에 사용하는 환경변수를 담고 있는 사전 (wsgi 전용 환경변수도 포함)
- wsgi 전용 환경변수
  > wsgi.version : WSGI 버전을 튜플 형태로 반환(1.0)
  > wsgi.url_scheme :  URL 스킴의 종류, 웹서버인 경우는 http를 반환한다.                
- request URL 관련 속성
  > path : url 경로(환경변수 PATH_INFO 와 같음)
  > url : 전체 URL 모두 표시
  > base_url : 쿼리 스트링을 제외한 URL
  > url_root : 환경변수 SERVER_NAME 와 같다.
```
> 11.response
```
- ex) ex18.py
- Response 객체를 이용한 웹브라우저에 응답하기
- from flask import Flask, Response 처럼 앞의 'R'이 대문자.
- flask에서 웹브라우저에 응답 할 때 모든 데이터는 Response 객체를 이용한다.
- Response 객체를 이용하여 사용자 정보를 유지하기 위하여 쿠키를 설정하기도 한다.
- Response 객체를 생성할때 사용하는 인자. (생략가능, 최대 6개 지원)
  > reponse : 웹브라우저에게 응답할 데이터 
  > status : HTTP 상태코드 200 - OK, 그 상태에 해당하는 코드 
  > headers : 웹브라우저에 응답할 헤더
  > minmetype : image/jpeg, text/html 과 같이 HTTP 메세지 바디가 어떤 mime type 데이터인지를 지정.
  > content_type : 웹브라우저에 응답하는 컨텐츠 타입을 지정, mimetype 과 같은 역할을 한다.
  > direct_pssthrough : True / False 설정
- Response Class의 속성
  > headers : 웹브라우저에 응답할 헤더의 데이터가 들어 있음. 이 속성의 테이터 타입은 headers 타입으로
              headers의 메소드를 이용해서 응답할 헤더를 변경할 수 있다.
  > status : 웹브라우저가 수신할 HTTP 상태 코드와 상태 메시지 값을 합친 문자열 데이터.
             이 데이터는 웨브라우저에 보내기전에 변경 가능하다.
  > status_code : 웹브라우저가 받을 HTTP 상태코드 값을 반환한다.
                  정확한 상태 메시지를 모를 경우 상태 코드 값만 지정하면 플라스크에서 자동으로 상태 메시지를 만들어 준다.
  > data : 웹 브라우저가 표시할 데이터를 포함 한다. get_date, set_data 메소드를 이용하여 데이터를 변경한다.
  > mimetype : 웹 브라우저에 응답할 때는 일반적으로 text/html 설정한다
- Response 객체에서 HTTP 메시지를 바디와 쿠키를 설정하는 메소드
  > get_data : 브라우저에 응답할 데이터를 반환한다. (data 속성에 있는 값을 얻어온다.)
  > set_data : 브라우저에 응답할 데이터를 변경할때 사용한다.
  > set_cookie : client 쿠키를 설정한다.
```
> 12.Cookie
```
- ex) ex19.py
- 쿠키는 기본적으로 쿠키 이름과 쿠키 값으로 구분.
- 쿠키는 정해진 시간동안 유지.
- 쿠키는 지정된 웨사이트의 경로에 영향을 미친다. (default : 루트디렉토리)
- 쿠키는 지정된 도메인 주소에 영향을 미친다.
- set_cookie의 인자
  > key : 쿠키 이름(쿠키를 설정할때는 반드시 이름을 지정해야 한다.)
  > value : 쿠키 값, 기본값은 빈 문자열
  > max_age : 쿠키 유지시간(초단위)(지속시간) (기본값 : None : 브라우저 종료시 자동으로 쿠키 제거)
              시간단위는 초단위의 시간 값으로 전달된다. 시간이 설정되면 초단위이 시간이 지나면 해당 쿠키가 삭제된다.
  > domain : 쿠키의 여향력이 미치는 도메인 주소, 기본값은 None 이다.
  > path : 쿠키의 여햘력이 미치는 웹사이트의 경로( 기본값은 루트이다.)
- 쿠키의 생성/삭제/확인  
```
> 13.Session
```
- ex) ex20.py
- 쿠키가 클라이언트에 저장되다보니 보안상 위험하다. ㄸ라서 서버에 데이터를 저장하는 방식인 세션이 많이 사용되는 추세
- flask 모둘에 session 객체를 이용하여 세션을 설정한다.
- flask에서 제공하는 세션 관련 키
  > 대문자는 대부분 환경설정 변수이다.
  > SECRET_KEY : 비밀키
  > SESSION_COOKIE_NAME : 세션 쿠키 이름. (기본값은 session)
  > SESSION_COOKIE_DOMAIN : 세션 쿠키가 동작할 도메인 주소
                            설정하지 않았을 경우 SERVER_NAME에 있는 도메인에서 동작
  > SESSION_COOKIE_PATH : 세션 쿠키가 동작할 URL 경로 (기본값은 루트)
  > SESSION_COOKIE_HTTPONLY : 웹 어플리케이션이 HTTP 프로토콜로 동작할 때만 세션 쿠키를 웹 어플리케이션에 전송.
                              기본 설정값은 True
  > SESSION_COOKIE_SECURE : 웹 어플리케이션이 HTTPS 프로토콜로 동작할 때만 세션 쿠키를 웹어플리케이션에 전송.
                            기본 설정값은 False
  > PERMANENT_SESSION_LIFETIME : 세션의 유효시간을 설정. (기본값은 31일로 되어 있다.)                            
```
> 14.Etc
````
- ex) ex21.py, ex22.py
- add_url_rule 메소드
  > route 데코레이터 대신에 사용하는 메소드
    (url, endpoint, view function)
- make_response 메소드
  > Response를 만들기 위한 메소드
- reponse를 json으로 만들기
- Request 후킹
  > HTTP 요청 전후에 대한 핸들어
  > Flask에서는 HTTP 요청 전후에 사용할 수 있는 데코레이터를 제공하고 있다.
    * before_first_request : 웹 프로그램이 실행된 이후 가장 처음에 들어오는 http 요청에서만 실행.
    * before_request : 매번 http 요청(request) 이 들어올때 마다 실행.
    * after_request : 매번 http 요청이 끝나고 브라우저에 응답하기전에 실행. (웹브라우저에 보이전)
    * teardown_request : http 요청의 결과가 브라우저에 보내진 다음에 실행.
    * teardown_appcontext : http 요청이 완전히 완료되면 실행 (application context내에서 실행)
- Flask Context 전역 변수
  > request를 처리하기 위해 제공되는 객체
    * 어플리케이션과 관련된 객체
      > current_app : 현재 활성화되어 있는 appilcation 객체 (인스턴스)
      > g : request 를 처리하는 동안 어플리케이션 임시 저장 정보를 사용할 수 있는 객체
            g는 Flask 인스턴스 객체의 app_ctx_globals_class 의 인스턴스 변수이다.
            from flask import g
    * Request Context
      > request : Client에 의해 송신된 HTTP request의 contents를 관리하는 객체
      > session  :  사용자 session, 어플리케이션 request 사이의 정보를 저장에서 사용하는 dict 타입 객체     
````
> 15.메시지 플래싱(Message Flashing)
```
- ex) ex24.py
- 플라스크에서 제공하는 플래싱 시스템
- 요청의 끝에 메시지를 기록하고 그 다음 요청에서만 그 메시지를 접근할 수 있도록 하는 기능.
```

> 16.Project
```
- 트윗 어플리케이션
- 구현 기능
  > 사용자 등록 기능
  > 로그인 / 로그아웃
  > 트윗 글 등록
  > 팔로우 / 언팔로우
  > 글 목록(사용자, 공용)
- 기술요소
  > 데이터베이스 (Mysql) 이용
  > gravatar 이용
  > 비밀번호 해싱
  > jinja2 템플릿 엔진

- 설치 package
  > pip flask
  > pip install MySQL-python  
```