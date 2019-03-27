def getList():
    import os
    files = os.listdir('data')

    list = ''
    for item in files:
        list += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

    return list
