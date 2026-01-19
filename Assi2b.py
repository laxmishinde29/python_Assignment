def Sum(No):
    total = 0
    for i in range(1, No + 1):
        total = total + i
    return total
    
def main():
    num = int(input("Enter the number:"))
    result = Sum(num)
    print(result)
    
if __name__ == "__main__":
    main()