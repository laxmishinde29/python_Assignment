def ChkGreater(No1,No2):
    if(No1 > No2):
        print(No1, "is greater")
    else:
        print(No2, "is greater")

    
def main():
    No1 = int(input("Enter First number :"))
    No2 = int(input("Enter Second number :"))

    ChkGreater(No1,No2)

if __name__ == "__main__":
    main()
