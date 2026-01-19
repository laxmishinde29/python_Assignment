def ChkDivisible(No):
    if(No % 3 == 0 & No % 5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("It is not Divisible by 3 and 5")


def main():
    num = int(input("Enter number:"))

    ChkDivisible(num)

if __name__ == "__main__":
    main()