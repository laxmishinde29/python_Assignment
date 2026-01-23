def main():
    Data = []
    n = int(input("How many numbers do you want to enter?"))
    
    for i in range(n):
        Value = input("Enter string:")
        Data.append(Value)

    Result = list(filter(lambda s : len(s) > 5, Data))
    print("String with length greater than 5 :",Result)

if __name__ == "__main__":
    main()