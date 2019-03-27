#!/usr/local/bin/python3
from view import getList

import html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

import cgi
form = cgi.FieldStorage()

if 'id' in form:
    title = form["id"].value
    title = sanitizer.sanitizer(title)
    description = open('data/' + title, 'r').read()
    description = sanitizer.sanitizer(description)
else:
    title = "WEB (Default)"
    description = "Hello~! WEB";







print("Content-Type: text/html")

print('''
<!doctype html>
<html>

<head>
  <title>Web Welcome HOME</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <h1><a href="index.py" title="Homepage">WEB</a></h1>

  <div id="grid">
    <ol>
      <a href="create.py">create</a>
      {list}
    </ol>
    <div id="article">
      <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="20" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
      </form>
    </div>
  </div>
</body>

</html>
'''.format(title=title,desc=description,list=getList()))
