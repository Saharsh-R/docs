import argparse
import datetime

def create_blog_post(title: str  ):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    slug = title.lower().replace(' ', '-')
    file_name = f"blog/{date}-{slug}.md"

    top_matter = f"""---
slug: {slug}
title: {title}
authors: sr
tags: [hackingwithswift, swift]
---

"""

    with open(file_name, 'w') as file:
        file.write(top_matter)

    print(f"Blog post '{file_name}' created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Docusaurus blog post with the given title, authors, tags, and content.")
    parser.add_argument('title', type=str, help="The title of the blog post.")

    args = parser.parse_args()
    create_blog_post(args.title)
