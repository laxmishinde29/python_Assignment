def ChkGreater(Data):
    max_no = Data[0]
    for no in Data:
        if no > max_no:
            max_no = no
    return max_no
    
def main():
    Data = []

    n = int(input("Number of elements:"))

    for i in range(n):
        Data.append(int(input("Enter elements:")))

    print("Maximum number :",ChkGreater(Data))


if __name__ == "__main__":
    main()
