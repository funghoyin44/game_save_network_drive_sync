from Logic import *

print("TreeDiagram Game Save Cloud Backup System")
print("Remote Server Location: " + remote_drive)
print()
print("What you want to do?")
print("0.Upload\n1.Download\n2.Backup")
choice = input("Please tell me your preference: ")
print()
if choice == "0":
    upload()
elif choice == "1":
    download()
elif choice == "2":
    backup()
else:
    print("Error Input")
    exit(0)
input("Done! Press any key to exit...")
