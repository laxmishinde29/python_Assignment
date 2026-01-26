def Factorial(No):
    fact = 1
    for i in range(1, No + 1):
        fact *= i
    return fact

def main():
    No = int(input("Enter Number:"))
    print("Factorial:",Factorial(No))

if __name__ == "__main__":
    main()