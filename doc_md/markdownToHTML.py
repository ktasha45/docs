# import sys
# import os
# import markdown

# def markdownToHTML(file_path):
#     with open(file_path, 'r', encoding='UTF8') as f:
#         text = f.read()
#         html = markdown.markdown(text, extensions=['md_in_html'])

#     with open(file_path.split('.')[0] + '.html', 'w', encoding='UTF8') as f:
#         f.write(html)

# if __name__ == '__main__':
#     if len(sys.argv) <= 1:
#         print("please enter the path of markdown file")
#         sys.exit()
    
#     file_path = os.path.relpath(sys.argv[1])
#     print(file_path)

#     markdownToHTML(file_path=file_path)

import sys
import os
from markdown import Markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

file_path = os.path.relpath(sys.argv[1])
with open(file_path, 'r', encoding='UTF8') as f:
    text = f.read()

md = Markdown(extensions=[GithubFlavoredMarkdownExtension()])

html = md.convert(text)
with open(file_path.split('.')[0] + '.html', 'w', encoding='UTF8') as f:
    f.write(html)