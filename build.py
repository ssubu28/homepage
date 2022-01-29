def main():
    # Python script to generate a static page

    # Templates
    top = open('./templates/top.html').read()
    bottom = open('./templates/bottom.html').read()

    #Index page
    index_file_read = open('./content/index.html').read()
    index = top + index_file_read + bottom
    open('./docs/index.html','w+').write(index)

    #About page
    about_file_read = open('./content/about.html').read()
    about = top + about_file_read + bottom
    open('./docs/about.html','w+').write(about)

    #Resume page
    resume_file_read = open('./content/resume.html').read()
    resume = top + resume_file_read + bottom
    open('./docs/resume.html','w+').write(resume)

    #Blog page
    blog_file_read = open('./content/blog.html').read()
    blog = top + blog_file_read + bottom
    open('./docs/blog.html','w+').write(blog)


main()