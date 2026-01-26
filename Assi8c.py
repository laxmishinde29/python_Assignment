def Add(Value1 , Value2):
    Ans = 0     #local variable
    Ans = Value1 + Value2
    return Ans

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter first number :"))
    No2 = int(input("Enter second number :"))

    Result = Add(No1, No2)
    print("Addition is: ",Result)

#starter
if __name__ == "__main__":
    main()