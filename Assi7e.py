from functools import reduce

Min = lambda a,b: a if a < b else b

def main():
    Data = []
    No = int(input("How many numbers do you want to enter?"))
    
    for i in range(No):
        num = int(input("Enter numbers:"))
        Data.append(num)

    Result = reduce(Min,Data)
    print("Input numbers :",Data)
    print("Data after mapping:",Result)

if __name__ == "__main__":
    main()