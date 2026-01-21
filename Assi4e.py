def PrintReverse(No):
    for i in range(No, 0, -1):
        print(i, end = " ")

def main():
    num = int(input("Enter the number :"))
    PrintReverse(num)

if __name__ == "__main__":
    main()