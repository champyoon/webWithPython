#!/usr/local/bin/python3

import cgi
form = cgi.FieldStorage()

pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

#본문 변경
opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()

#파일이름 변경
import os
os.rename('data/' + pageId, 'data/' + title)


#Redirection
print("Location: index.py?id="+title)
print()
