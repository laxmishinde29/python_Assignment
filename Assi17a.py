def main():
    lineCount = 0
    fname = input("Enter file name :")

    fobj = open(fname,"r")

    for line in fobj:
        lineCount = lineCount + 1

    print("file contain ", lineCount ,"lines")

if __name__ == "__main__":
    main()