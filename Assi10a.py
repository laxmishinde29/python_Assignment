def Addition(data):
    total = 0
    for no in data:
        total = total + no
    return total
    
def main():
    data = []

    n = int(input("Number of elements:"))

    for i in range(n):
        data.append(int(input("Enter elements:")))

    print("addition of all elements :",Addition(data))

if __name__ == "__main__":
    main()