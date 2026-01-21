def PrintNumber(No):
    for i in range(1,No + 1):
        print(i, end = " ")

def main():
    num = int(input("Enter the number :"))
    PrintNumber(num)

if __name__ == "__main__":
    main()