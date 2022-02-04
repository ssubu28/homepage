# Python script to generate a static site

import glob
from os import path

# Function to build a page - replace content and title
def page_builder(file_content, page_title):
    template = open('./templates/base.html').read()
    # Titletag replacement
    titletag_page = template.replace('{{title}}', page_title)
    # Content replacement
    content_page = titletag_page.replace('{{content}}', file_content)
    return content_page     


# Activating navigation links 
def navlink_activator(replacement_text, base_page):
    final_page=base_page.replace(replacement_text, 'active')
    return final_page


# Function to check which page to build. Refactored.
def page_identifier(page_title, page_filename, page_output, page_navigate):
    file_read = open(page_filename).read()
    base_page = page_builder(file_read, page_title)
    write_page = navlink_activator(page_navigate, base_page)
    open(page_output, 'w+').write(write_page)


def list_generate():
    pages = []

    # ** For index will have to check and perform a replace or something.  - DONE using if statement
    # Photography title to be replaced by blog. 
    # Navigation correction  - DONE
    
    all_html_files = glob.glob("content/*.html")

    for file in all_html_files:
        file_path = file
        file_name = path.basename(file_path)
        name_only, file_extension = path.splitext(file_name)
        output_path = './docs/' + file_name
          
        if name_only == 'index':
            name_only = 'Tech blog'

        # elif name_only == 'blog':
        #     name_only = 'Photography'

        pages.append({
            'title': str(name_only.capitalize()),
            'filename': file_path,
            'output': output_path,
            'navigate': '{{Active ' + str(name_only.title()) + '}}'
        })

    return pages



def main():

    pages = list_generate()

    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
        page_navigate = page['navigate']
        page_identifier(page_title, page_filename, page_output, page_navigate)

    

if __name__ == "__main__":
    main()
    





""" 
    pages_old = [
        {
            'title': 'Tech Projects',
            'filename': './content/index.html',
            'output': './docs/index.html',
            'navigate': '{{Active Tech Blog}}'
        },
        {
            'title': 'About',
            'filename': './content/about.html',
            'output': './docs/about.html',
            'navigate': '{{Active About}}'
        },
        {
            'title': 'Photography',
            'filename': './content/blog.html',
            'output': './docs/blog.html',
            'navigate': '{{Active Blog}}'
        },
        {
            'title': 'Resume',
            'filename': './content/resume.html',
            'output': './docs/resume.html',
            'navigate': '{{Active Resume}}'
        }
    ]

    print("\n\n")
    for p_old in pages_old:
        print(p_old) """