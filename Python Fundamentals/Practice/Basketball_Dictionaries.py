class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    # Method to display all player's information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}")

# Dictionaries representing players
kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "Small Forward", 
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "Small Forward", 
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Creating Player instances manually
player_1 = Player(kevin['name'], kevin['age'], kevin['position'], kevin['team'])
player_2 = Player(jason['name'], jason['age'], jason['position'], jason['team'])
player_3 = Player(kyrie['name'], kyrie['age'], kyrie['position'], kyrie['team'])

# Challenge 3: Populate a new list with Player instances
player_instances = []

# List of player dictionaries for challenge 3
players = [kevin, jason, kyrie]

# Iterate over the list of dictionaries and create Player instances
for player_dict in players:
    # Create a Player instance using values from the dictionary
    player = Player(player_dict['name'], player_dict['age'], player_dict['position'], player_dict['team'])
    # Add the Player instance to the list
    player_instances.append(player)

# Display information for each player in the new list
for player in player_instances:
    player.display_info()
