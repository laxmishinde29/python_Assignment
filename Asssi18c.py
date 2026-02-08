import sys
import os
import shutil

def DirectoryCopy(Dir, Destination):
    Ret = False

    Ret = os.path.exists(Dir)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(Dir)
    if(Ret == False):
        print("It is not a directory")
        return

    if not os.path.exists(Destination):
        os.mkdir(Destination)

    for FolderName, SubFolderName, FileName in os.walk(Dir):
        for fname in FileName:
            Dir_path = os.path.join(FolderName,fname)
            Destination_path = os.path.join(Destination,fname)

            shutil.copy2(Dir_path, Destination_path)
            print(fname, "Copied successfully")

def main():
    Border = "-"*50

    print(Border)
    print("--------- Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return

    DirectoryCopy(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()