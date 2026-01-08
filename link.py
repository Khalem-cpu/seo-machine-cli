import os
import random

files = os.listdir("output")

for file in files:
    path = f"output/{file}"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    links = random.sample(files, min(3, len(files)))
    link_html = "<h2>Related Errors</h2><ul>"

    for l in links:
        link_html += f"<li><a href='{l}'>{l.replace('-', ' ').replace('.html','')}</a></li>"

    link_html += "</ul></body>"

    content = content.replace("</body>", link_html)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Internal links added.")
