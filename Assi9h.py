def Pattern(No):
    for i in range(No):
        for j in range(1, No+1):
            print(j, end = " ")
        print()

def main():
    n = int(input("Enter number:"))
    Pattern(n)

if __name__ == "__main__":
    main()