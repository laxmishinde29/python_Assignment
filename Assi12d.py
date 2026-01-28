import threading

def Thread1():
    for i in range(1,51):
        print("Thread1:",i)

def Thread2():
    for i in range(50,0,-1):
        print("Thread2:",i)

def main():
    t1 = threading.Thread(target = Thread1)
    t2 = threading.Thread(target = Thread2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()