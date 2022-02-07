import glob
from os import path
from jinja2 import Template


#Generating new page. 
def newpage_generator():
    confirmation = input("Do you want to choose your own filename and content to add ? Type 'yes' to confirm and 'no' to use the default: ")
    if confirmation.lower() == "yes":
        input_file_name = input("Enter new file name you of your choice with the html extension: ")
        input_content = input("Enter valid HTML content: ")
        open("./content/" + input_file_name, "w+").write(input_content)
        main() # Building site post new page info
    elif confirmation.lower() == "no":
        new_content = "<h1>New Content!</h1>\n<p>New content...</p>"
        open("./content/new_content_page.html", "w+").write(new_content)
        main() # Building site post new page info
    else:
        print("Please choose 'yes' or 'no'.")


# Function to check which page to build. Refactored.
def page_identifier(pages, page_title, page_filename, page_output):  
    file_html = open(page_filename).read() 
    template = Template(open("./templates/base.html").read()) 
    results = template.render(
        pages=pages,                    # Added pages list for templating
        title=page_title,
        content=file_html,              
    )
    open(page_output, 'w+').write(results)


# Generating pages - list of dictionaries
def list_generate():  
    pages = []
    
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


# main function
def main():

    pages = list_generate()

    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
        page_identifier(pages, page_title, page_filename, page_output)
