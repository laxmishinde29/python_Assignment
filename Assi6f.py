Chkodd = lambda No: (No % 2 != 0)

def main():
    #num = 0
    Ret = False

    num = int(input("Enter the number :"))

    Ret = Chkodd(num)

    if(Ret == True):
        print("It is odd")
    else:
        print("It is even")

if __name__ == "__main__":
    main()