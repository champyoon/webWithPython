#!/usr/local/bin/python3
from view import getList

import cgi
form = cgi.FieldStorage()

if 'id' in form:
    title = form["id"].value
    description = open('data/' + title, 'r').read()
else:
    title = ''
    description = ''




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
      <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value={_title}
        <p><input type="text" name="title" value={_title}></p>
        <p><textarea rows="20" name="description">{_description}</textarea></p>
        <p><input type="submit" value="update"></p>
      </form>
    </div>
  </div>
</body>

</html>
'''.format(_title=title,_description=description,list=getList()))
