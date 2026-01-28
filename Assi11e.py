from functools import reduce

CheckRange = lambda x:x >= 70 and x <= 90
Incease = lambda x:x + 10
product = lambda a,b: a * b 

def main():
    data = list(map(int,input("Enter numbers:").split()))

    fdata = list(filter(CheckRange,data))
    mdata = list(map(Incease,fdata))
    result = reduce(product,mdata)

    print("After Filter:",fdata)
    print("After Map:",mdata)
    print("After reduce:",result)

if __name__ == "__main__":
    main()