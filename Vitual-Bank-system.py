class Account:
    def __init__(self, bal , acc):
        self.balance = bal
        self.account_no = acc
    
    #debit
    def debit(self, amount):
        self.balance -= amount
        print("Rs",amount, "was debited")
        print("Total balance = ", self.get_balance())

    #credit
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was Credited")
        print("Total balance = ", self.get_balance())


    def get_balance(self):
        return self.balance

acc1 = Account(10000, 4321)

while True:
    print("\n1. Debit")
    print("2. Credit")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = int(input("Enter amount to debit: "))
        acc1.debit(amt)

    elif choice == 2:
        amt = int(input("Enter amount to credit: "))
        acc1.credit(amt)

    elif choice == 3:
        print("Current Balance =", acc1.get_balance())

    elif choice == 4:
        print("Thank you for using bank system 😊")
        break

    else:
        print("Invalid choice")



