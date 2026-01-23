from functools import reduce

Product = lambda a,b: a * b 

def main():
    Data = []
    No = int(input("How many numbers do you want to enter?"))
    
    for i in range(No):
        num = int(input("Enter numbers:"))
        Data.append(num)

    Result = reduce(Product,Data)
    print("Input numbers :",Data)
    print("Data after reducing:",Result)

if __name__ == "__main__":
    main()