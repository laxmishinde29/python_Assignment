def ChkNum(num):
    if(num % 2 == 0):
        print("even")
    else:
        print("Odd")

def main():
    num = int(input("Enter number:"))
    ChkNum(num)

if __name__ == "__main__":
    main()