def Display(No):
    for i in range(No, 0 ,-1):
        for j in range(i):
            print("*",end = " ")
        print()

def main():
    n = int(input("Enter number :"))
    Display(n)

if __name__ == "__main__":
    main()