# Virtual-bank-system
Bank system using Python OOP : credit, debit &amp; balance check with class, methods &amp; condition handling.
<br>
class Bank :

    def __init__(self , bal , acc_no):
        self.balance = bal
        self.acc_no = acc_no

    #debit
    def debit(self , amount):
        self.balance -= amount
        print( amount, "amount was debited")
        print("total balance :" , self.balance)
        
    #credit
    def credit(self , amount):
        self.balance += amount
        print( amount, "amount was credited")
        print("total balance :" , self.balance)

    #balance
    def check_balance (self ):
        return self.balance
    

account1 = Bank(10000 , 1234)
account1.credit(1000)
account1.debit(300)
account1.balance
