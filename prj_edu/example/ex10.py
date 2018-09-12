from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)
template = env.get_template("hello_world.txt")

person = {}
person['name'] = '홍길복'
person['salary'] = '20000'

colors = ['red', 'yellow', 'blue']

print(template.render(name='홍길동', animal='고양이', data=person, truth=False, colors=colors))
