#bank account deposit but the numbers must be prime only

class BankAccount():
    def __init__ (self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def is_valid_account(self):
        #acc number must be 10 digits and prime
        if len(self.account_number) == 10 and self.account_number.isdigit():
            return self.is_prime(int(self.account_number))
        else:
            return False
        
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def __str__(self):
        return f"{self.name}'s account #{self.account_number} with balance: ${self.balance:.2f}"
    
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
        else:
            print("deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("no funds availible to withdraw from account")


#driver code goes here
name = input("enter your name: ")
acc_num = input("enter a 10 digit account number: ")
balance = float(input("enter initial balance: "))

account = BankAccount(name, acc_num, balance)

if account.is_valid_account():
    print("Account made successfully")
    print(account)
else:
    print("Invalid account number. It must be a 10 digit prime number.")
