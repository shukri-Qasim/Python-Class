# BankAccount Class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# SavingsAccount Class (Child class of BankAccount)
class SavingsAccount(BankAccount):
    def calculate_interest(self, rate):
        interest = self.balance * (rate / 100)
        print(f"Interest at {rate}% rate: {interest}")
        return interest

# Testing the Classes
if __name__ == "__main__":
    # Creating an instance of SavingsAccount
    savings_account = SavingsAccount("John Doe", 1000)

    # Depositing 500 into the account
    savings_account.deposit(500)  

    # Withdrawing 200 from the account
    savings_account.withdraw(200) 

    # Calculating interest at a 5% rate
    savings_account.calculate_interest(5)  
