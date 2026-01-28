import threading
import time

def Maximum(numbers):
    print("Maximum element:",max(numbers))

def Minimum(numbers):
    print("Minimum element:",min(numbers))

def main():
    start_time = time.time()

    data = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    t1 = threading.Thread(target=Maximum, args=(data,))
    t2 = threading.Thread(target=Minimum, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()
    print("Time required :", end_time - start_time)


if __name__ == "__main__":
    main()
