import time

welcome = '''\033[1;34;1m
------------Welcome To FTP System---------------
{tim}


Tip:type 'help' for help.
\033[0m
'''.format(tim=time.strftime("%Y-%m-%d %H:%M",time.localtime()))

help_menu= '''\033[1;33;1m
"ls "   This command is use to show directory.
        -c refers to client,default.
        -s is server
        eg:ls -c
"upload"   This command must run with a file path,which refers to upload
        file to server.
        eg: upd test.txt
"download"   same as "upd",but refers to download.
"useradd"  add a user ,user name must be given!
        eg: useradd alex
"logout" logout current account
\033[0m
'''