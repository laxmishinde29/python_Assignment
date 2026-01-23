square = lambda No : No * No

def main():
    Data = []
    No = int(input("How many numbers do you want to enter?"))
    
    for i in range(No):
        num = int(input("Enter numbers:"))
        Data.append(num)

    Result = list(map(square,Data))
    print("Input numbers :",Data)
    print("Data after mapping:",Result)

if __name__ == "__main__":
    main()