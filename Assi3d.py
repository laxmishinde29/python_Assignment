def SumDigits(No):
    total = 0
    while(No != 0):
        digit = No % 10
        total = total + digit
        No = No // 10
    return total

def main():
    num = int(input("Enter the number :"))

    print(SumDigits(num))

if __name__ == "__main__":
    main()