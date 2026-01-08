import os
import random

with open("data/keywords.txt", "r", encoding="utf-8") as f:
    keywords = [k.strip() for k in f.readlines() if k.strip()]

with open("templates/page.html", "r", encoding="utf-8") as f:
    template = f.read()

os.makedirs("output", exist_ok=True)

def generate_content(keyword):
    fixes = [
        "check your syntax carefully",
        "verify variable types",
        "review official documentation",
        "restart your environment",
        "update dependencies",
    ]
    return (
        f"The error '{keyword}' is a common issue encountered by developers.\n\n"
        f"This error usually occurs due to incorrect usage or misconfiguration.\n\n"
        f"To fix {keyword}, you should {random.choice(fixes)}.\n\n"
        f"Understanding why {keyword} happens will help prevent it in the future."
    )

for keyword in keywords:
    slug = keyword.replace(" ", "-")
    title = f"{keyword.title()} – Meaning, Causes, and Fix"
    description = f"Learn what {keyword} means, why it happens, and how to fix it step by step."
    content = generate_content(keyword)

    page = template.replace("{{TITLE}}", title)
    page = page.replace("{{DESCRIPTION}}", description)
    page = page.replace("{{H1}}", title)
    page = page.replace("{{CONTENT}}", content)

    with open(f"output/{slug}.html", "w", encoding="utf-8") as f:
        f.write(page)

print(f"Generated {len(keywords)} pages.")
