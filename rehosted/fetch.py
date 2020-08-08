import requests

url = "https://pastebin.com/raw/9XgMYyzY"

r = requests.get(url)

lines = r.text.split('\n')

with open(url.split('/')[-1] + '.md', 'w', encoding="UTF-8") as f:
    f.write(
"""---
layout: rehosted
title: 
type: 
link: %s
---
""" % ("https://pastebin.com/" + url.split('/')[-1]))

    for l in lines:
        if l.strip() != '':
            f.write("<p>" + l.strip() + "</p>\n")
