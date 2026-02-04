

def main():
    ExistingFile = input("Enter Existing file:")
    fobj = open(ExistingFile,"r")
    Data = fobj.read()

    NewFile = input("Enter name of new file:")
    nobj = open(NewFile,"w")
    nobj.write(Data)

    print("Content get copied successfully")


if __name__ == "__main__":
    main()