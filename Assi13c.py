import threading
import time

counter = 0
lock = threading.Lock()

def Increment():
    global counter
    for i in range(1000):
        lock.acquire()
        counter += 1
        lock.release()


def main():
    start_time = time.time()

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)
    t3 = threading.Thread(target=Increment)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time = time.time()

    print("Final counter value:", counter)
    print("Time required :", end_time - start_time)


if __name__ == "__main__":
    main()
