def main():
    fname = input("Enter File name:")

    fobj = open(fname,"r")
    Data = fobj.read()
    print(Data)

if __name__ == "__main__":
    main()