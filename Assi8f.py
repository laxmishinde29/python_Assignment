def ChkNum(num):
    if(num > 0):
        print("Positive")
    elif(num < 0):
        print("Negative")
    else:
        print("Zero")
        

def main():
    num = int(input("Enter number:"))
    ChkNum(num)

if __name__ == "__main__":
    main()