from functools import reduce

Max = lambda a,b: a if a > b else b

def main():
    Data = []
    No = int(input("How many numbers do you want to enter?"))
    
    for i in range(No):
        num = int(input("Enter numbers:"))
        Data.append(num)

    Result = reduce(Max,Data)
    print("Input numbers :",Data)
    print("Data after mapping:",Result)

if __name__ == "__main__":
    main()