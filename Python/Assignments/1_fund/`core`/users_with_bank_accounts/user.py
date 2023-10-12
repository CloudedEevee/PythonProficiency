class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate = 0.02, balance = 0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"Your balance is: ${self.account.balance:.2f}")
        return self


class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
    ######################## Read BankAcount Model
    def display_account(self):
        print(f"Your balance is: ${self.balance:.2f}")
        print(f"Your interest rate is: {round(self.interest_rate * 100)}%")
        return self
    ######################## Update BankAcount Model
    def deposit(self, amount):
        self.balance += amount
        print(f"Thank you for depositing ${amount}. Your balance is now ${self.balance}")
        return self
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            print(f"Thank you for using Our Bank! You have withdrawn ${amount} and now have a balance of ${self.balance}")
            return self
        else:
            print(f"Insufficient funds. Balance is ${self.balance}")
            return self

    def yield_interest(self):
        interest = (self.balance * self.interest_rate)
        self.balance += interest
        print(f"Your interest of ${interest:.2f} has been deposited into your account. Your balance is now ${self.balance:.2f}")
        return self

######################## Testing
print("######################## Testing User_1")
user_1 = User("Sophie", "catsrule@gmail.com")
user_1.account.deposit(530).deposit(545).deposit(535).withdraw(1225).yield_interest().display_account()

print("######################## Testing User_2")
user_2 = User("April", "dogsdrool@gmail.com")
user_2.account.deposit(1100).deposit(1230).withdraw(60).withdraw(75).withdraw(134).withdraw(1500).yield_interest().display_account()

