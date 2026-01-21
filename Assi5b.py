def AreaCircle(r):
    return 3.14 * r * r

def main():
    r =int(input("Enter radius :"))
    print("Area of circle is:",AreaCircle(r))

if __name__ == "__main__":
    main()