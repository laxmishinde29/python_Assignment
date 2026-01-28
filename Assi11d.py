from functools import reduce

CheckPrime = lambda No : (No % 2 == 0)

Double = lambda No : No*No

Max = lambda A,B :A if A > B else B

def main():
    Data = [11,10,15,20,27,22,30]
    print("Actual Data is :",Data)

    FData = list(filter(CheckPrime, Data))
    print("Data after filter is : ",FData)

    MData = list(map(Double, FData))
    print("Data after mapping is :",MData)

    RData = reduce(Max, MData)
    print("Data after reduce is :",RData)

if __name__ == "__main__":
    main()