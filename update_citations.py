from scholarly import scholarly
import re

author = scholarly.search_author_id("u78blqIAAAAJ")
author = scholarly.fill(author, sections=['indices'])

citations = author['citedby']

# Update README.md
with open("README.md", "r") as f:
    readme = f.read()

new_readme = re.sub(r"Citations-\d+", f"Citations-{citations}", readme)

with open("README.md", "w") as f:
    f.write(new_readme)
