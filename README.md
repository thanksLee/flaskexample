# flaskexample
Python Flask Example
```
- Practical Flask Web Development Tutorials 이 동영상을 참조하여 만듬.
- 유튜브 참조 : https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB
```

#### 윈도우에 Python 설치
***
> 1.windows에서 python 개발
```
- python 설치 : 3.7
- pip install --upgrade setuptools
- pip install virtualenv
- pip install sqlalchemy
- pip install MySQL-python
- MySQL-python 설치하면 오류가 발생 (error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/)
  그러면 이곳에서 다운로드오류 발생시 : https://visualstudio.microsoft.com/ko/vs/older-downloads/?rr=http%3A%2F%2Fneedjarvis.tistory.com%2F224
  만약 안될시 : https://pg.kdtk.net/1770 이곳에서 받는다.
- etc 폴더에 visualcppbuildtools_full.exe.bk -> visualcppbuildtools_full.exe 변경하여 실행
```
> 2.파이썬 가상환경
```
 - virtualenv E:\myproject\MyPython
```
> 3.가상환경으로 셋팅 변경
```
  - cd E:\myproject\MyPython
  - 가상환경으로 접속    : activate
  - 가상환경에서 빠져나옴 : deactivate
```
> 4.가상환경에서 필요한 라이브러리 설치
```
- cd Scripts
- pip install flask
```

### flask template 사용
> 1.extends
```
  - {% extends "파일명" %}
  - 한 html 안에 1개 이상 사용할 수 없다.
  - {% block body %} {% endblock %} 으로 감싸진 것을 변경한다.
  - ex) "extends/ext_header.html" 이렇게 사용할 수있다.
```
> 2.include
  ```
  - {% include "파일명" %}
  - 한 html 안에 1개 이상 사용이 가능하다.
  - ex) "include/inc_header.html" 이렇게 사용할 수있다.
```

### flask Error 대처
> 1.builtins.RuntimeError
```
  - RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
  - python 파일 
     app.config["SECRET_KEY"] = "hard to guess string" 
```