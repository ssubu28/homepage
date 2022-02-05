# Python script to generate a static site

import glob
from os import path
from jinja2 import Template


# Function to check which page to build. Refactored.
def page_identifier(pages, page_title, page_filename, page_output):  # Remove page_navigate

    file_html = open(page_filename).read() # "content/index.html"
    template = Template(open("./templates/base.html").read()) # Replace with  ->  ./templates/base.html 
    results = template.render(
        pages=pages,   # added pages list
        title=page_title,
        content=file_html,   # Navigation too* + try using dictionary
    )
    #print(results)
    open(page_output, 'w+').write(results)



# Resume page showing up as first tab even though opened page is index.html

# **** TEST by adding some dummy html files with new names. ****

def list_generate():  
    pages = []

    # ** For index will have to check and perform a replace or something.  - DONE using if statement
    # Photography title to be replaced by blog. 
    # Navigation correction  - DONE
    
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
            #'navigate': '{{Active ' + str(name_only.title()) + '}}'
        })

    return pages



def main():

    pages = list_generate()

    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
        page_identifier(pages, page_title, page_filename, page_output)

    

if __name__ == "__main__":
    main()