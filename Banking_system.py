#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("personal details")
        print("")
        print("Name ",self.name)
        print("Age ",self.age)
        print("Gender ",self.gender)
#Child Class

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Account balance has been updated: ",self.balance)
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Funds | Balance available: ",self.balance)
        else:
            self.balance = self.balance - amount
            print("Account balance has been updated: ",self.balance)
            
    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: ",self.balance)
        
            
        
        
        
    
    

