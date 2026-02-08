import sys
import os

def DirectoryScanner(Folder):
    Ret = False

    Ret = os.path.exists(Folder)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(Folder)
    if(Ret == False):
        print("It is not a directory")
        return

    for FolderName, SubFolderName, FileName in os.walk(Folder):
        for fname in FileName:
            print(fname)

def main():
    Border = "-"*50

    print(Border)
    print("--------- Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()