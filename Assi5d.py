def Binary(No):
    binary = ""
    while(No > 0):
        binary = str(No % 2) + binary
        No = No // 2
    return binary

def main():
    num = int(input("Enter number :"))
    print("Binary:",Binary(num))

if __name__ == "__main__":
    main()