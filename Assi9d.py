def SumFactor(No):
    total = 0
    for i in range(1, No):
        if No % i == 0:
            total += i
    return total

def main():
    n = int(input("Enter number :"))
    print("Addition of factors :",SumFactor(n))

if __name__ == "__main__":
    main()