# Function to build a single page.
def page_builder(file_content, page_title):
    template = open('./templates/base.html').read()
    content_page = template.replace('{{content}}', file_content)
    full_page = content_page.replace('{{title}}', page_title)
    return full_page



# Function to check which page to build
def page_identifier(page_title, page_filename, page_output):
    
    # *** WILL need IF-ELSE HERE! CHECK TITLE and then proceed with other code.  *** 

    if page_title == 'Tech Projects':
        index_file_read = open(page_filename).read()
        index = page_builder(index_file_read, page_title)
        open(page_output, 'w+').write(index)

    elif page_title == 'About':
        about_file_read = open(page_filename).read()
        about = page_builder(about_file_read, page_title)
        open(page_output, 'w+').write(about)

    elif page_title == 'Photography':
        blog_file_read = open(page_filename).read()
        blog = page_builder(blog_file_read, page_title)
        open(page_output, 'w+').write(blog)

    elif page_title == 'Resume':
        resume_file_read = open(page_filename).read()
        resume = page_builder(resume_file_read, page_title)
        open(page_output, 'w+').write(resume)

    else:
        print('ERROR! - Invalid Page.')


# Main function
def main():
    # Python script to generate a static page

    pages = [
        {
            'title': 'Tech Projects',
            'filename': './content/index.html',
            'output': './docs/index.html'
        },
        {
            'title': 'About',
            'filename': './content/about.html',
            'output': './docs/about.html'
        },
        {
            'title': 'Photography',
            'filename': './content/blog.html',
            'output': './docs/blog.html'
        },
        {
            'title': 'Resume',
            'filename': './content/resume.html',
            'output': './docs/resume.html'
        }
    ]

    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
        page_identifier(page_title, page_filename, page_output)

    
main()