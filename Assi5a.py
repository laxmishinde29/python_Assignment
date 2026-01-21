def AreaRectangle(length,width):
    return length * width

def main():
    length = int(input("Enter length:"))
    width = int(input("Enter width:"))

    print("Area of rectangle:",AreaRectangle(length,width))

if __name__ == "__main__":
    main()