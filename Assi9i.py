def CountDigit(No):
    Count = 0
    while(No != 0):
        Count += 1
        No //= 10
    return Count

def main():
    n = int(input("Enter the number :"))
    print("Count of Digit :",CountDigit(n))

if __name__ == "__main__":
    main()