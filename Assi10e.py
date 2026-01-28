def Chkprime(No):
    if(No <= 1):
        return False

    for i in range(2,No):
        if(No % i == 0):
            return False
    return True

def ListPrime(data):
    total = 0

    for x in data:
        if Chkprime(x):
            total = total + x

    return total

def main():
    data = []

    n = int(input("Enter number of elements:"))

    for i in range(n):
        data.append(int(input("Enter element:")))

    print("Addition of prime numbers: ",ListPrime(data))

if __name__ == "__main__":
    main()