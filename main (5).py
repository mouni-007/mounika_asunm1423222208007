class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount > self.__account_balance:
            print("Insufficient balance.")
        else:
            self.__account_balance -= amount

    def display_balance(self):
        print("Account balance:", self.__account_balance)

# Creating an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 10000)

# Testing deposit functionality
account.deposit(5000)
account.display_balance()

# Testing withdrawal functionality
account.withdraw(3000)
account.display_balance()

account.withdraw(15000) # Insufficient balance test