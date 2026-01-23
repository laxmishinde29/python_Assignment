Max = lambda x,y,z : x>y>z

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))
    No3 = int(input("Enter third number:"))
    Result = True

    Result = Max(No1,No2,No3)
    
    if(Result==True):
        print("Maximum number is:",No1)
    elif(Result == True):
        print("Maximum number is:",No2)
    else:
        print("Maximum number is:",No3)
        
if __name__ == "__main__":
    main()