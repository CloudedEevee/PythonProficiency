class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
    ######################## Create Player

    @classmethod
    def get_team(cls, team_list):
        player_list = []
        for this_player in team_list:
            player = {
                'name' : this_player.name,
                'age' : this_player.age,
                'position' : this_player.position,
                'team' : this_player.team,
            }
            player_list.append(player)
        return player_list
        


@staticmethod
def create_new_team(cls, player_list, new_team_list):
    for new_player in player_list:
        new_team_list.append(Player(new_player))        
    print("List completed. Printing list now.........")
    print(new_team_list)


    ######################## Read Player



    ######################## Update Player



    ######################## Delete Player



################################################ Outside-of-Class Code
# dictionaries of player info
kevin = {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}

jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}

kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

# adding players to class Player
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# iterate thru following list to create a list of new_player class instances
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

new_team = []

create_new_team(Player, players, new_team)

print(f"Your team is: \n{Player.get_team(new_team)}")
