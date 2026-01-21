def CheckPerfect(No):
    total = 0
    for i in range(1, No):
        if(No % i == 0):
            total = total + i

    if(total == No):
        print("Perfect number")
    else:
        print("Not perfect")

def main():
    num = int(input("Enter the number :"))
    CheckPerfect(num)

if __name__ == "__main__":
    main()