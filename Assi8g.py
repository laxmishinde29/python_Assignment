def Divisible(No):
    if(No % 5 == 0):
        print("True")
    else:
        print("False")
    
def main():
    No = int(input("Enter Number:"))
    Divisible(No)

if __name__ == "__main__":
    main()