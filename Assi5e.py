def DisplayGread(marks):
    if(marks >= 75):
        print("Distinction")
    elif(marks >= 60):
        print("First class")
    elif(marks >= 50):
        print("Second class")
    else:
        print("fail")

def main():
    marks = int(input("Enter Marks :"))
    DisplayGread(marks)

if __name__ == "__main__":
    main()