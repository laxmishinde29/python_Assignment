import threading
import time

def Prime(numbers):
    print("Prime numbers:")
    for No in numbers:
        if No > 1:
            for i in range(2, No):
                if No % i == 0:
                    break
            else:
                print(No, end=" ")
    print()


def NonPrime(numbers):
    print("Non-Prime numbers:")
    for No in numbers:
        if No <= 1:
            print(No, end=" ")
        else:
            for i in range(2, No):
                if No % i == 0:
                    print(No, end=" ")
                    break
    print()


def main():
    start_time = time.time()

    data = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()
    print("Time required :", end_time - start_time)


if __name__ == "__main__":
    main()
