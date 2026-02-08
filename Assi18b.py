import sys
import os

def DirectoryScanner(Folder, oldExit, NewExit):
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
            if(fname.endswith(oldExit)):
                old_path = os.path.join(FolderName,fname)
                new_name = fname.replace(oldExit,NewExit)
                new_path = os.path.join(FolderName,new_name)

                os.rename(old_path, new_path)
                print(fname, "renamed to", new_name)

def main():
    Border = "-"*50

    print(Border)
    print("--------- Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1],sys.argv[2],sys.argv[3])
                    #  Folder       .txt          .doc
if __name__ == "__main__":
    main()