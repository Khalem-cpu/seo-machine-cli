import os

BASE_URL = "https://Khalem-cpu.github.io/seo-machine"

pages = []

for file in os.listdir("output"):
    if file.endswith(".html"):
        pages.append(f"{BASE_URL}/output/{file}")

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    f.write(f"<url><loc>{BASE_URL}/</loc></url>\n")
    for page in pages:
        f.write(f"<url><loc>{page}</loc></url>\n")
    f.write("</urlset>")

print(f"Sitemap generated with {len(pages) + 1} URLs.")

