from abc import ABC, abstractmethod
import random
import datetime
import sys


class Util:
    history = []

    @staticmethod
    def generate_account_num() -> str:
        return ''.join(str(random.randint(0, 9)) for _ in range(12))

    @classmethod
    def add_entry(cls, msg):
        cls.history.append(msg)

    @staticmethod
    def create_account(account_type):
        if account_type.lower() == "saving":
            name = input("Enter your name: ")
        else:
            name = input("Enter company name: ")

        balance = float(input("Enter initial balance: "))
        while balance < 0:
            balance = float(input("Initial balance cannot be negative. Please enter a valid amount: "))
        
        if account_type.lower() == "saving":
            account = SavingAccount(name, balance)
        else:
            account = CurrentAccount(name, balance)

        Util.add_entry(f"{datetime.datetime.now()} - {account_type} account, Account Number: {account.account_no}, balance: {balance}")
        print(f"Congratulations, your {account_type} account creation was successful!")
        print(f"Your Account Number (A/C): {account.account_no}")
        print(Util.history)

        return account

    @classmethod
    def detailed_statement(cls):
        print(cls.history[0])
        print(f"Your last {len(cls.history)-1} transactions are:")
        for transaction in cls.history[1:]:
            print(transaction)

    @classmethod
    def mini_statement(cls):
        print(cls.history[0])
        if (len(cls.history)-1) <= 5:
            print(f"Your last {len(cls.history)-1} transactions are:")
            for transaction in cls.history[1:]:
                print(transaction)
        else:
            print("Your last 5 transactions are:")
            for transaction in cls.history[-5:]:
                print(transaction)


class Account(ABC):
    BANKNAME = "Durga Bank!"

    def __init__(self, name: str, balance: float, min_balance: float) -> None:
        self.account_no = Util.generate_account_num()
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self):
        while True:
            amount = float(input('Enter Amount to deposit: '))
            if amount < 0:
                print('Invalid Amount, Enter Valid Amount to deposit:')
            else:
                self.balance += amount
                Util.add_entry(f"Account Credited (Deposit) with Amount: {amount}")
                print('After Deposit, Your account Balance:', self.balance)
                break

    def withdraw(self):
        while True:
            amount = float(input('Enter Amount to withdraw: '))
            if amount <= 0 or amount % 100 != 0:
                print('Amount should be Positive and Multiples of 100, Enter Valid Amount to withdraw:')
            else:
                if self.balance - amount >= self.min_balance:
                    self.balance -= amount
                    Util.add_entry(f"Account Debited (Withdraw) with Amount: {amount}")
                    print('After Withdraw, Your account Balance:', self.balance)
                    break
                else:
                    print('Sorry, Insufficient Funds')

    @abstractmethod
    def account_info(self) -> str:
        pass


class SavingAccount(Account):
    def __init__(self, name: str, balance: float) -> None:
        super().__init__(name, balance, 0)

    def __str__(self) -> str:
        return f"Hi {self.name}, It's your saving account with balance {self.balance}"

    def account_info(self) -> str:
        return f"Saving Account - Name: {self.name}, Balance: {self.balance}, Minimum Balance: {self.min_balance}"

    def balance_inquiry(self):
        return f"Hello, {self.name} Your saving account balance is: {self.balance}₹ account ends with xxxxxxxx{self.account_no[:-4]}"


class CurrentAccount(Account):
    def __init__(self, name: str, balance: float) -> None:
        super().__init__(name, balance, -1000)

    def __str__(self) -> str:
        return f"Hi {self.name}, It's your current account with balance {self.balance}"

    def account_info(self) -> str:
        return f"Current Account - Name: {self.name}, Balance: {self.balance}, Overdraft Limit: {self.min_balance}"

    def balance_inquiry(self):
        return f"Hello, {self.name} Your current account balance is: {self.balance}₹ account ends with xxxxxxxx{self.account_no[:-4]}"


# Main interaction code
print(f"Welcome to {Account.BANKNAME}")
print("Do you want to open a saving or current account?")
print("s - Saving\nc - Current")

option = input("Choose an option: ").lower()
count = 1

while option not in ['s', 'c']:
    if count >= 3:
        print("Sorry, maximum number of attempts reached. Try after some time!")
        sys.exit()
    option = input("Please select a correct option [s - Saving | c - Current]: ").lower()
    count += 1

account = Util.create_account("Saving" if option == 's' else "Current")

while True:
    print("""
b Balance Enquiry
d Deposit
w Withdraw
m Mini Statement
s Detailed Statement
g Get Account Information
e Exit
""")
    option = input("Choose Your Option:").lower()
    count = 1
    while option not in ['b', 'd', 'e', 'g', 'm', 's', 'w']:
        if count >= 3:
            print("Sorry, maximum number of attempts reached. Try after some time!")
            sys.exit()
        option = input("Your Option is invalid, Choose Correct Option[b|d|e|g|m|s|w]:").lower()
        count += 1

    if option == 'b':
        print(account.balance_inquiry())

    elif option == 'g':
        print(account.account_info())

    elif option == 'd':
        account.deposit()

    elif option == 'w':
        account.withdraw()

    elif option == 'm':
        Util.mini_statement()

    elif option == 's':
        Util.detailed_statement()

    else:
        print("Exiting the application...")
        sys.exit()
