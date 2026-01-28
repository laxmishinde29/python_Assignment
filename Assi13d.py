import threading
import time

sum_result = 0
product_result = 1

def Sum(numbers):
    global sum_result
    sum_result = sum(numbers)

def Product(numbers):
    global product_result
    product_result *= no

def main():
    start_time = time.time()

    data = [1,2,3,4,5]

    t1 = threading.Thread(target=Sum, args=(data,))
    t2 = threading.Thread(target=Product, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()

    print("sum :",sum_result)
    print("Product :",product_result)
    print("Time required:",end_time - start_time)

if __name__ == "__main__":
    main()