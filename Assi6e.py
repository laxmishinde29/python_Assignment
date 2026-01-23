Chkeven = lambda No: (No % 2 == 0)

def main():
    #num = 0
    Ret = False

    num = int(input("Enter the number :"))

    Ret = Chkeven(num)

    if(Ret == True):
        print("It is even")
    else:
        print("It is odd")

if __name__ == "__main__":
    main()