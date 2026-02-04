import sys

def main():
    if(len(sys.argv) == 3):

        FirstFile = sys.argv[1]
        fobj = open(FirstFile,"r")
        FData = fobj.read()

        SecondFile = sys.argv[1]
        sobj = open(SecondFile,"r")
        SData = sobj.read()

        if(FData == SData):
            print("Success")

        else:
            print("Failure")

    else:
        print("Data is not matching")


if __name__ == "__main__":
    main()