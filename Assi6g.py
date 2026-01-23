Chkdivisible = lambda No: (No % 5 == 0)

def main():
    Ret = False

    num = int(input("Enter the number :"))

    Ret = Chkdivisible(num)

    if(Ret == True):
        print("It is divisible by 5")
    else:
        print("It is not divisible by 5")

if __name__ == "__main__":
    main()