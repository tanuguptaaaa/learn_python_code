class BankAccount:
    def __init__(self, initial_balance):
        # Private attribute
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

# Create a BankAccount object
account = BankAccount(1000)

# Interact with the account
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")


