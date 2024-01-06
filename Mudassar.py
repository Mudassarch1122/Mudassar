import os,platform
os.system('git pull')
os.system("clear")
xyz=platform.architecture()[0]
if xyz=="32bit":
    __import__("P32")
elif xyz=="64bit":
    __import__("P64")