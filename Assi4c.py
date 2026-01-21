def Arithmatic(No1,No2):
    print("Addition is :",No1 + No2)
    print("Substraction is :",No1 - No2)
    print("Multiplication is :",No1 * No2)
    print("Division is :",No1 / No2)

def main():
    a = int(input("Enter First number :"))
    b = int(input("Enter second number :"))

    Arithmatic(a,b)

if __name__ == "__main__":
    main()