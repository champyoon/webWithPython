#!/usr/local/bin/python3

import cgi
form = cgi.FieldStorage()

id = form["pageId"].value

#파일 삭제
import os
os.remove('data/' + id)

#Redirection
print("Location: index.py")
print()
