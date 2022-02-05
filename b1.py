from jinja2 import Template

index_html = open("content/index.html").read()
template = Template(open("newbase.html").read())
print(template.render(
    title="Homepage",
    content=index_html,
))