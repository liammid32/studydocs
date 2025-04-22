class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:  # Fixed typo "amoount" to "amount"
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("No funds available to withdraw")

    def get_balance(self):
        return self.balance

    def __str__(self):  # Fixed indentation and syntax
        return f"{self.name}'s account: ${self.balance:.2f}"
    
    
account1 = Bank("Alice", 200)
print(account1)

account1.deposit(150)
print(account1)

account1.withdraw(50)
print(account1)

account1.withdraw(400) #should error out
print(account1)