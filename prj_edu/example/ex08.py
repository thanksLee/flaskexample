from jinja2 import Template

template = Template("Hello {{ somethinng }} !")
print(template.render(somethine = "bhlee"))

template1 = Template("number : {% for n in range(1, 10) %} {{ n }} {% endfor %}")
print(template1.render())