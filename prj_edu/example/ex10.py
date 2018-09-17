from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)
template = env.get_template("hello_world.txt")

person = {}
person['name'] = '홍길복'
person['salary'] = '20000'

colors = ['red', 'yellow', 'blue']

print(template.render(name='홍길동', animal='고양이', data=person, truth=False, colors=colors))

template = env.get_template("base.html")
print(template.render(title="페이지제목"))

template = env.get_template("child.html")
print(template.render(title="Jinja2연습", body="템플릿 상속 테스트"))

template = env.get_template("whitespace.html")
print(template.render(Truth=True))

template = env.get_template("escape.html")
print(template.render())

template = env.get_template("macro.html")
print(template.render())

template = env.get_template("macro_input.html")
print(template.render())

template = env.get_template("macro_input2.html")
print(template.render())

template = env.get_template("macro_input3.html")
print(template.render())

template = env.get_template("macro_caller.html")
print(template.render())

userData = [  {'user_name':'Hong', 'name':'홍길동', 'job':'개발자'}
            , {'user_name':'kim', 'name':'김매령', 'job':'디자이너'}
            , {'user_name':'lee', 'name':'이병훈', 'job':'DBA'}
            ]

template = env.get_template("macro_caller2.html")
print(template.render(user_list=userData))
