# Python script to generate a static site

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



# Function to check which page to build
def page_identifier(page_title, page_filename, page_output, page_navigate):

    if page_title == 'Tech Projects':
        index_file_read = open(page_filename).read()
        index_base_page = page_builder(index_file_read, page_title)
        index_final = navlink_activator(page_navigate, index_base_page)
        open(page_output, 'w+').write(index_final)

    elif page_title == 'About':
        about_file_read = open(page_filename).read()
        about_base_page = page_builder(about_file_read, page_title)
        about_final = navlink_activator(page_navigate, about_base_page)
        open(page_output, 'w+').write(about_final)

    elif page_title == 'Photography':
        blog_file_read = open(page_filename).read()
        blog_base_page = page_builder(blog_file_read, page_title)
        blog_final = navlink_activator(page_navigate, blog_base_page)
        open(page_output, 'w+').write(blog_final)

    elif page_title == 'Resume':
        resume_file_read = open(page_filename).read()
        resume_base_page = page_builder(resume_file_read, page_title)
        resume_final = navlink_activator(page_navigate, resume_base_page)
        open(page_output, 'w+').write(resume_final)

    else:
        print('ERROR! - Invalid Page.')



def main():

    pages = [
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

    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
        page_navigate = page['navigate']
        page_identifier(page_title, page_filename, page_output, page_navigate)

    

if __name__ == "__main__":
    main()