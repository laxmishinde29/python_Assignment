def SumDigit(No):
    total = 0
    while(No != 0):
        total += No % 10
        No //= 10
    return total

def main():
    n = int(input("Enter the number :"))
    print("Count of Digit :",SumDigit(n))

if __name__ == "__main__":
    main()