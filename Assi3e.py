def Palindrome(No):
    temp = No
    rev = 0

    while(No != 0):
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10

    if(temp == rev):
        print("It is Palindrome")

    else:
        print("It is not Palindrome")

def main():
    num = int(input("Enter the number:"))
    Palindrome(num)

if __name__ == "__main__":
    main()