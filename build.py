def main(pages):
    # Python script to generate a static page

    # Templates
    # top = open('./templates/top.html').read()
    # bottom = open('./templates/bottom.html').read()

    base_template = open('./templates/base.html').read()


    for page in pages:
        page_filename = page['filename']
        page_output = page['output']

    # *** WILL need IF-ELSE HERE! CHECK TITLE and then proceed with other code.  *** 

        if page['title'] == 'Tech Projects':
            index_file_read = open(page_filename).read()
            index =  base_template.replace('{{content}}', index_file_read)
            open(page_output, 'w+').write(index)

        # elif page['title'] == 'About':
        #     about_file_read = open(page_filename).read()
        #     about = top + about_file_read + bottom
        #     open(page_output, 'w+').write(about)

        # elif page['title'] == 'Photography':
        #     blog_file_read = open(page_filename).read()
        #     blog = top + blog_file_read + bottom
        #     open(page_output, 'w+').write(blog)

        # elif page['title'] == 'Resume':
        #     resume_file_read = open(page_filename).read()
        #     resume = top + resume_file_read + bottom
        #     open(page_output, 'w+').write(resume)

        else:
            print('ERROR! - Invalid Page.')

    

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


main(pages)