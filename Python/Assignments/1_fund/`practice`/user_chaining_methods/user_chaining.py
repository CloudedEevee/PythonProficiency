class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    

###################### Create Model User



###################### Read Model User
    def display_info(self):
        data = {
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'email' : self.email,
            'age' : self.age,
        }
        for attribute in data:
            print(data[attribute])
        return self



###################### Update Model User
    def enroll(self):
        if self.is_rewards_member == True:
            print("Member is already enrolled!")
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"Member is enrolled! Your gold card points are at: {self.gold_card_points}")
        return self


    def spend_points(self, amount):
        if self.gold_card_points - amount < 0:
            print(f"You don't have enough points for this! You have {self.gold_card_points} points left.")
        else:
            self.gold_card_points -= amount
            print(f"Congrats on using your points! You now have: {self.gold_card_points}")
        return self


###################### Delete Model User



###################### Testing
print("###########################")
user_1 = User("Kitt", "Candie", "notarealemail@aol.com", 21)
user_1.display_info().enroll().spend_points(50).enroll()

user_2 = User("Allie", "Mysterious", "mysteriousemail@gmail.com", 16)
user_2.enroll().spend_points(80).display_info()

user_3 = User("Seraph", "Ina", "seraphina@email.com", 30)
user_3.display_info().enroll().spend_points(40).spend_points(300)







###################### Notes
# To be able to call upon the methods with the . notation, I must have all methods indented to the same level as the __init__ function. 