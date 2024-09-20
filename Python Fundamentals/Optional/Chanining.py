#Create a class
class User:
    #! Constructor
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    #method display_info:

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("S Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)
        return self
    #method enroll:

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        print("Enrolled successfully!")
        return self

    #method spend_points:
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"Spend {amount} points successfully!")
        else:
            print("Insufficient points!")
        return self    

# Create two more instances of the User class
user1 = User("Alice", "Smith", "alice@example.com", 25)
user2 = User("Bob", "Johnson", "bob@example.com", 35)

#-------------#
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
