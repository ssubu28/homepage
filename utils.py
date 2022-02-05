import glob
from os import path
from jinja2 import Template


#Generating new page. 
def newpage_generator():
    new_content = """<h1>New Content!</h1>\n<p>New content...</p>"""
    open("./content/new_content_page.html", "w+").write(new_content)


# Function to check which page to build. Refactored.
def page_identifier(pages, page_title, page_filename, page_output):  
    file_html = open(page_filename).read() 
    template = Template(open("./templates/base.html").read()) 
    results = template.render(
        pages=pages,                    # added pages list for templating
        title=page_title,
        content=file_html,              #  Try using dictionary
    )
    open(page_output, 'w+').write(results)


# Resume page showing up as first tab even though opened page is index.html

def list_generate():  
    pages = []

    # Photography title to be replaced by blog. 
    
    all_html_files = glob.glob("content/*.html")

    for file_path in all_html_files:
        file_name = path.basename(file_path)
        name_only, file_extension = path.splitext(file_name)
        output_path = './docs/' + file_name
          
        if name_only == 'index':
            name_only = 'Tech blog'

        pages.append({
            'title': str(name_only.capitalize()),
            'filename': file_path,
            'output': output_path,
        })

    return pages



def main():

    pages = list_generate()

    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
        page_identifier(pages, page_title, page_filename, page_output)
