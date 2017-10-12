import re


def ck_command():
    '''
    check command availability. delete whitespace
    :return:
    '''
    choice = input("\033[1;33;1mInput:\033[0m").strip()
    choice = re.sub(" +"," ",choice)
    return choice



