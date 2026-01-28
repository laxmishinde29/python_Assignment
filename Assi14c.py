class Arithmatic :
    def Addition(self,A,B):
        return A+B

    def Substraction(self,A,B):         #instance method parameter is self
        return A-B

    def Multiplication(self,A,B):
        return A*B

    def Division(self,A,B):
        return A/B


No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number:"))
No2 = int(input("Enter second number:"))

obj = Arithmatic()

Ans = obj.Addition(No1,No2)
print("Addition is:",Ans)

Ans = obj.Substraction(No1,No2)
print("Substraction is:",Ans)

Ans = obj.Multiplication(No1,No2)
print("Multiplication is:",Ans)

Ans = obj.Division(No1,No2)
print("Division is:",Ans)