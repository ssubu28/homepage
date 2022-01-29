def page_builder(file_content):
    template = open('./templates/base.html').read()
    # rename result here with appropriate variable name
    result = template.replace('{{content}}', file_content)

    return result


def page_identifier(page_title, page_filename, page_output):

    if page_title == 'Tech Projects':
        index_file_read = open(page_filename).read()
        index = page_builder(index_file_read)
        # index =  base_template.replace('{{content}}', index_file_read)
        open(page_output, 'w+').write(index)

    elif page_title == 'About':
        about_file_read = open(page_filename).read()
        # about = base_template.replace('{{content}}', about_file_read)
        about = page_builder(about_file_read)
        open(page_output, 'w+').write(about)

    elif page_title == 'Photography':
        blog_file_read = open(page_filename).read()
        #blog = base_template.replace('{{content}}', blog_file_read)
        blog = page_builder(blog_file_read)
        open(page_output, 'w+').write(blog)

    elif page_title == 'Resume':
        resume_file_read = open(page_filename).read()
        # resume = base_template.replace('{{content}}', resume_file_read)
        resume = page_builder(resume_file_read)
        open(page_output, 'w+').write(resume)

    else:
        print('ERROR! - Invalid Page.')



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

    # Templates
    # top = open('./templates/top.html').read()
    # bottom = open('./templates/bottom.html').read()

    # Part of new template builder function
    # base_template = open('./templates/base.html').read()


    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
        page_identifier(page_title, page_filename, page_output)

    # *** WILL need IF-ELSE HERE! CHECK TITLE and then proceed with other code.  *** 

        """ 
        if page['title'] == 'Tech Projects':
            index_file_read = open(page_filename).read()
            index = page_builder(index_file_read)
            # index =  base_template.replace('{{content}}', index_file_read)
            open(page_output, 'w+').write(index)

        elif page['title'] == 'About':
            about_file_read = open(page_filename).read()
            # about = base_template.replace('{{content}}', about_file_read)
            about = page_builder(about_file_read)
            open(page_output, 'w+').write(about)

        elif page['title'] == 'Photography':
            blog_file_read = open(page_filename).read()
            #blog = base_template.replace('{{content}}', blog_file_read)
            blog = page_builder(blog_file_read)
            open(page_output, 'w+').write(blog)

        elif page['title'] == 'Resume':
            resume_file_read = open(page_filename).read()
            # resume = base_template.replace('{{content}}', resume_file_read)
            resume = page_builder(resume_file_read)
            open(page_output, 'w+').write(resume)

        else:
            print('ERROR! - Invalid Page.') 
        """

    

    #Index page
    # index_file_read = open('./content/index.html').read()
    # index = top + index_file_read + bottom
    # open('./docs/index.html', 'w+').write(index)

    #About page
    # about_file_read = open('./content/about.html').read()
    # about = top + about_file_read + bottom
    # open('./docs/about.html', 'w+').write(about)

    # #Resume page
    # resume_file_read = open('./content/resume.html').read()
    # resume = top + resume_file_read + bottom
    # open('./docs/resume.html', 'w+').write(resume)

    #Blog page
    # blog_file_read = open('./content/blog.html').read()
    # blog = top + blog_file_read + bottom
    # open('./docs/blog.html', 'w+').write(blog)



# move into main ?
""" 
pages = [
    {
        'title': 'Tech Projects',
        'filename': './content/index.html',
        'output': './docs/index.html'
    },
    {
        'title': 'About',
        'filename': './content/about.html',
        'output': '/docs/about.html'
    },
    {
        'title': 'Photography',
        'filename': './content/blog.html',
        'output': '/docs/blog.html'
    },
    {
        'title': 'Resume',
        'filename': './content/resume.html',
        'output': '/docs/resume.html'
    }
] 
"""


main()