def ChkMin(Data):
    min_no = Data[0]
    for no in Data:
        if no < min_no:
            min_no = no
    return min_no
    
def main():
    Data = []

    n = int(input("Number of elements:"))

    for i in range(n):
        Data.append(int(input("Enter elements:")))

    print("Maximum number :",ChkMin(Data))


if __name__ == "__main__":
    main()
