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

###################### Update Model User
def enroll(self):
    if self.is_rewards_member == True:
        return print("Member is already enrolled!")
    else:
        self.is_rewards_member = True
        self.gold_card_points += 200
        print(f"Member is enrolled! Your gold card points are at: {self.gold_card_points}")

def spend_points(self, amount):
    if self.gold_card_points - amount < 0:
        return print(f"You don't have enough points for this! You have {self.gold_card_points} points left.")
    else:
        self.gold_card_points -= amount
        print(f"Congrats on using your points! You now have: {self.gold_card_points}")
###################### Delete Model User






###################### Testing
##########Creating a user, displaying, and enrolling member
my_user_kitt = User("Kitt", "Candie", "notarealemail@aol.com", 21)
print("#########")
display_info(my_user_kitt)
enroll(my_user_kitt)
print("#########")

##########Creating two more users
my_user_allie = User("Allie", "Mysterious", "mysteriousemail@gmail.com", 16)
my_user_seraph = User("Seraph", "Ina", "seraphina@email.com", 30)
print("#########")

##########Test the spend_points function
spend_points(my_user_kitt, 50)
print("#########")

##########Enroll second user and spend_points
enroll(my_user_allie)
spend_points(my_user_allie, 80)
print("#########")

##########Display All Users Data (individually)
print("Kitt's data:")
display_info(my_user_kitt)
print("#########")

print("Allie's data:")
display_info(my_user_allie)
print("#########")

print("Seraph's data:")
display_info(my_user_seraph)
print("#########")

##########Attempt to double-enroll a member
enroll(my_user_kitt)
print("#########")

##########Enroll third member, spend_points, then attempt to spend more points than the member has
enroll(my_user_seraph)
spend_points(my_user_seraph, 40)
spend_points(my_user_seraph, 300)
