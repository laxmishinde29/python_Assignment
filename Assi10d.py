def Frequency(Data,search):
    count = 0
    for no in Data:
        if no == search:
            count = count + 1
    return count
    
def main():
    Data = []

    n = int(input("Number of elements:"))

    for i in range(n):
        Data.append(int(input("Enter elements:")))

    search = int(input("Enter element to search:"))
    print("Frequency:",Frequency(Data,search))


if __name__ == "__main__":
    main()
