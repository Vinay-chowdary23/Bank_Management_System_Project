# Bank Management System using OOP in Python

class Customer:
    def __init__(self):
        self.name = input("Enter customer name: ")
        self.balance = int(input("Enter initial balance: "))
    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Initial Balance: ₹{self.balance}")

class Deposit:
    def __init__(self, customer):
        self.customer = customer

    def make_deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.customer.balance += amount
        print(f"₹{amount} deposited successfully.")
    def display_balance(self):
        print(f"Updated Balance: ₹{self.customer.balance}")

class Withdraw:
    def __init__(self, customer):
        self.customer = customer
    def make_withdrawal(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.customer.balance:
            print("Insufficient balance.")
        else:
            self.customer.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_final_balance(self):
        print(f"Final Balance: ₹{self.customer.balance}")

# --- Main Program ---
customer = Customer()
deposit = Deposit(customer)
withdraw = Withdraw(customer)
customer.display_info()
deposit.make_deposit()
deposit.display_balance()
withdraw.make_withdrawal()
withdraw.display_final_balance()
