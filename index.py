#!/usr/local/bin/python3
from view import getList

import cgi
form = cgi.FieldStorage()

if 'id' in form:
    title = form["id"].value
    description = open('data/' + title, 'r').read()
    update_link = '''
        <form action="update.py">
            <input type="hidden" name="id" value={_id}>
            <input type="submit" value=update>
        </form>
    '''.format(_id=title)
    delete_link = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value={_id}>
            <input type="submit" value="delete">
        </form>
    '''.format(_id=title)
else:
    title = "Hello~~"
    description = "WEB~!~!";
    update_link = ''
    delete_link = ''












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
        {_list}
    </ol>
    <div id="article">
        {_update_link}
        {_delete_link}
        <h2>{_title}</h2>
        <p>{_description}</p>
    </div>
  </div>
</body>

</html>
'''.format(_update_link=update_link,
           _delete_link=delete_link,
           _list=getList(),
           _title=title,
           _description=description)
           )
