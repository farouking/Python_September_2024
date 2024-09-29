# pet.py
class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy = min(self.energy + 25, 100)
        return self

    def eat(self):
        print(f"{self.name} is eating.")
        print(f"Before eating: Energy = {self.energy}, Health = {self.health}")
        self.energy = min(self.energy + 5, 100)
        self.health = min(self.health + 10, 100)
        print(f"After eating: Energy = {self.energy}, Health = {self.health}")
        return self

    def play(self):
        print(f"{self.name} is playing.")
        if self.energy >= 10:
            self.health = min(self.health + 5, 100)
            self.energy -= 10
        else:
            print(f"{self.name} is too tired to play!")
        return self

    def noise(self):
        print(f"The noise of '{self.name}' is a happy sound!")
