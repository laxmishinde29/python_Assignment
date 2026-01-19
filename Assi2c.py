def Factorial(No):
    fact = 1
    for i in range(1, No + 1):
        fact = fact * i
    return fact
    
def main():
    num = int(input("Enter the number:"))
    result = Factorial(num)
    print(result)
    
if __name__ == "__main__":
    main()