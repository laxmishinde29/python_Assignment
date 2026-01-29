class BankName:
    
    ROI= 10.5

    def __init__(self,HolderName,AcBalance):
        self.Name = HolderName
        self.Amount = AcBalance

    def Display(self):
        print("Account holder name:",self.Name)
        print("Current balance is:",self.Amount)

    def Deposite(self):
        Deposite = int(input("Enter amount you want to deposite:"))

        self.Amount = self.Amount + Deposite
        print("Your total balance is :",self.Amount)

    def Withdraw(self):
        Withdraw = int(input("Enter amount you want to Withdraw:"))

        if(self.Amount>Withdraw):
            self.Amount = self.Amount - Withdraw
            print("Your total balance is :",self.Amount)

        else:
            print("you dont have sufficient balance")

    def CalculateIntrest(self):
        Interest = (self.Amount * BankName.ROI) / 100
        print("Your Intrest is:",Interest)

obj1 = BankName("Anjali",1000)
obj2 = BankName("Raj",2000)
obj3 = BankName("Yash",3000)
obj4 = BankName("Vipul",4000)

obj1.Display()
obj1.Deposite()
obj1.Withdraw()
obj1.CalculateIntrest()

obj2.Display()
obj2.Deposite()
obj2.Withdraw()
obj2.CalculateIntrest()

obj3.Display()
obj3.Deposite()
obj3.Withdraw()
obj3.CalculateIntrest()

obj4.Display()
obj4.Deposite()
obj4.Withdraw()
obj4.CalculateIntrest()