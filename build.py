# Function to build a single page.
def page_builder(file_content, page_title):
    template = open('./templates/base.html').read()
    # Title tag replacement
    nav_page = template.replace('{{title}}', page_title)
    # Content replacement
    content_page = nav_page.replace('{{content}}', file_content)
    
    
    """ 
    if page_title == 'Tech Projects':
        full_page = nav_page.replace('{{Active Tech Blog}}', 'active')
    elif page_title == 'About':
        full_page = nav_page.replace('{{Active About}}', 'active')
    elif page_title == 'Photography':
        full_page = nav_page.replace('{{Active Blog}}', 'active')
    elif page_title == 'Resume':
        full_page = nav_page.replace('{{Active Resume}}', 'active')
    else:
        full_page = nav_page  
    """
    
    return content_page      # should be full_page if using above if-else block



def navlink_activator(replacement_text, base_page):
    final_page=base_page.replace(replacement_text, 'active')
    return final_page



# Function to check which page to build
def page_identifier(page_title, page_filename, page_output):
    
    # *** WILL need IF-ELSE HERE! CHECK TITLE and then proceed with other code.  *** 

    if page_title == 'Tech Projects':
        index_file_read = open(page_filename).read()
        index_base_page = page_builder(index_file_read, page_title)
        index_final = navlink_activator('{{Active Tech Blog}}', index_base_page)
        open(page_output, 'w+').write(index_final)

    elif page_title == 'About':
        about_file_read = open(page_filename).read()
        about_base_page = page_builder(about_file_read, page_title)
        about_final = navlink_activator('{{Active About}}', about_base_page)
        open(page_output, 'w+').write(about_final)

    elif page_title == 'Photography':
        blog_file_read = open(page_filename).read()
        blog_base_page = page_builder(blog_file_read, page_title)
        blog_final = navlink_activator('{{Active Blog}}', blog_base_page)
        open(page_output, 'w+').write(blog_final)

    elif page_title == 'Resume':
        resume_file_read = open(page_filename).read()
        resume_base_page = page_builder(resume_file_read, page_title)
        resume_final = navlink_activator('{{Active Resume}}', resume_base_page)
        open(page_output, 'w+').write(resume_final)

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

    

if __name__ == "__main__":
    main()