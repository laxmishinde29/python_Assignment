import threading

def Small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count = count + 1

    print("Small letter:",count)

def Captial(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count = count + 1

    print("Captial letter:",count)

def Digit(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count = count + 1

    print("Digit letter:",count)
        
def main():
    s = input("Enter String:")

    t1 = threading.Thread(target = Small, args=(s,))
    t2 = threading.Thread(target = Captial, args=(s,))
    t3 = threading.Thread(target = Digit, args=(s,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()