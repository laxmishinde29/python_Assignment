def OddNumber(No):
    for i in range(1, No + 1):
        if(i % 2 != 0):
            print(i)

def main():
    num = int(input("Enter the number:"))

    OddNumber(num)

if __name__ == "__main__":
    main()