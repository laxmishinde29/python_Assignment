import os

def DirectoryScanner(DirectoryName):
    Ret = os.path.exists(DirectoryName)

    if(Ret == True):
        print({DirectoryName},"exist")

    else:
        print({DirectoryName},"not exist") 


def main():
    DirectoryName = input("Enter the name of directory :")

    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()