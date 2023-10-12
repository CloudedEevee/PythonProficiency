class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance



######################## Create BankAcount Model



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


######################## Delete BankAcount Model






######################## Testing
print("######################## Testing User_1")
user_1 = BankAccount(0.03, 300)
user_1.deposit(530).deposit(545).deposit(535).withdraw(1225).yield_interest().display_account()

print("######################## Testing User_2")
user_2 = BankAccount(0.02, 1200)
user_2.deposit(1100).deposit(1230).withdraw(60).withdraw(75).withdraw(134).withdraw(1500).yield_interest().display_account()


######################## Notes
# 1) If the functions are indented to match the indentation of the __init__, they can access inside the user's instance data. (e.g. self.balance within display_account

# 2) variable_name:.2f rounds an interger to the nearest double-decimal digit. 
    # This is used in the file instead of round(variable_name, 2) because if there aren't enough digits, round() does not add zeros to ensure both the tens and hundreds places are showing. 
    # I wanted the format of the numebers to include 2 decimal places bc I am dealing with money, and that is common notation. 




