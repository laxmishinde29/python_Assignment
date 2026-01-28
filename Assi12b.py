import threading

def EvenFactor(No):
    total = 0
    print("Even Factor:")
    for i in range(1, No + 1):
        if(No % i == 0 and i % 2 == 0):
            print(i)
            total = total + 1

    print("Sum of even factor:",total)

def OddFactor(No):
    total = 0
    print("Odd Factor:")
    for i in range(1, No + 1):
        if(No % i == 0 and i % 2 != 0):
            print(i)
            total = total + 1

    print("Sum of even factor:",total)
        
def main():
    n = int(input("Enter number:"))

    t1 = threading.Thread(target = EvenFactor, args=(n,))
    t2 = threading.Thread(target = OddFactor, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()