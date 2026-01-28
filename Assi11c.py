from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Incerment = lambda No : No+1

Add = lambda A,B :A+B

def main():
    Data = [11,10,15,20,27,22,30]
    print("Actual Data is :",Data)

    FData = list(filter(CheckEven, Data))
    print("Data after filter is : ",FData)

    MData = list(map(Incerment, FData))
    print("Data after mapping is :",MData)

    RData = reduce(Add, MData)
    print("Data after reduce is :",RData)

if __name__ == "__main__":
    main()