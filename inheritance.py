class Account:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.transaction_history = [] 
        self.overdraft_limit = 0  
        self.minimum_balance = 0  

    def deposit(self, amount):
      
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
      
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def view_account_details(self):
       
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Current Balance: ${self.balance}")

    def account_statement(self):
    
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def set_overdraft_limit(self, limit):
       
        self.overdraft_limit = limit
        print(f"Overdraft limit set to ${limit}.")

    def calculate_interest(self, rate):
       
        interest = (rate / 100) * self.balance
        self.balance += interest
        print(f"Interest applied. New balance: ${self.balance}")

    def freeze_account(self):
        print("Account frozen.")

    def unfreeze_account(self):
        print("Account unfrozen.")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def set_minimum_balance(self, min_balance):
      
        self.minimum_balance = min_balance
        print(f"Minimum balance requirement set to ${min_balance}.")

    def transfer_funds(self, target_account, amount):
        
        if self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred ${amount} to {target_account.owner_name}.")
        else:
            print("Insufficient balance for transfer.")

    def close_account(self):
       
        print(f"Account {self.account_number} closed. Thank you!")

my_account = Account(account_number=12345, balance=1000, owner_name="Fanny Ingabire")
my_account.deposit(7000)
my_account.withdraw(500)
my_account.view_account_details()
my_account.account_statement()
my_account.set_overdraft_limit(400)
my_account.calculate_interest(2)
my_account.freeze_account()
my_account.unfreeze_account()
my_account.set_minimum_balance(50)
other_account = Account(account_number=2224, balance=5000, owner_name="Ngoga Merci")
my_account.transfer_funds(other_account, 800)
my_account.close_account()
