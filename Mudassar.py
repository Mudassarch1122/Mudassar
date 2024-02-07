import os,platform
os.system('git pull')
os.system("clear")
os.system("pip install pycurl")
os.system('xdg-open https://chat.whatsapp.com/HXqyQgfFnrBBNflwqcW1nj')
xyz=platform.architecture()[0]
if xyz=="32bit":
    __import__("P32")
elif xyz=="64bit":
    __import__("p64")
