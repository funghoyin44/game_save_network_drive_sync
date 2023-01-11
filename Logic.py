import os
from Database import *
from datetime import datetime
#Uplaod Logic
def upload():
    print("Choose the game you want to upload:")
    print("0. Blue Reflection")
    print("1. Fatal Frame")
    choice = input("Your Choice: ")
    print()
    print("##################################################################")
    print("Please wait while uploading...")
    if choice == "0":
        os.system("xcopy {} {} /h /i /c /e /r /y".format(Blue_Reflection_Path, Blue_Reflection_Remote))
    elif choice == "1":
        os.system("xcopy {} {} /h /i /c /e /r /y".format(Fatal_Frame_Path, Fatal_Frame_Remote))

#Download Logic
def download():
    print("Choose the game you want to download:")
    print("0. Blue Reflection")
    print("1. Fatal Frame")
    choice  = input("Your Choice: ")
    print()
    print("##################################################################")
    print("Please wait while downloading...")
    if choice == "0":
        os.system("xcopy {} {} /h /i /c /e /r /y".format(Blue_Reflection_Remote, Blue_Reflection_Path))
    elif choice == "1":
        os.system("xcopy {} {} /h /i /c /e /r /y".format(Fatal_Frame_Remote, Fatal_Frame_Path))

def backup():
    print()
    print("##################################################################")
    print("Please wait while uploading...")
    now = datetime.now()
    path = "{}\\Backup\\{}-{}-{}_{}-{}-{}({})".format(remote_drive, now.day, now.month, now.year, now.hour, now.minute, now.second, username)
    os.system("mkdir {}".format(path))
    os.system("mkdir {}\\Blue_Reflection".format(path))
    os.system("xcopy {} {}\\Blue_Reflection /h /i /c /e /r /y".format(Blue_Reflection_Path, path))
    os.system("mkdir {}\\Fatal_Frame".format(path))
    os.system("xcopy {} {}\\Fatal_Frame /h /i /c /e /r /y".format(Fatal_Frame_Path, path))
