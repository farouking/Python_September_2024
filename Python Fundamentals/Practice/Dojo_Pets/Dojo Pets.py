class Ninja:
    # __init__ method to initialize Ninja attributes
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # Method to walk the ninja's pet by invoking the pet's play() method
    def walk(self):
        self.pet.play()

    # Method to feed the ninja's pet by invoking the pet's eat() method
    def feed(self):
        print("Feeding the pet...")
        self.pet.eat()

    # Method to bathe the ninja's pet by invoking the pet's noise() method
    def bathe(self):
        self.pet.noise()


class Pet:
    # __init__ method to initialize Pet attributes
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    # Method to increase the pet's energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # Method to increase the pet's energy by 5 and health by 10
    def eat(self):
        print(f"Before eating: Energy = {self.energy}, Health = {self.health}")
        self.energy += 5
        self.health += 10
        print(f"After eating: Energy = {self.energy}, Health = {self.health}")
        return self

    # Method to increase the pet's health by 5
    def play(self):
        print(f"{self.name} is playing")
        self.health += 5

    # Method to print the pet's sound
    def noise(self):
        print(f"The noise of '{self.name}' is hawhaw")


# Example usage:
fox = Pet("Fox", "dog", "hunting")
marko = Ninja("Marko", "Rossi", "scooby snack", "milk bone", fox)

marko.walk()   # Should invoke fox.play() and increase  health by 5
marko.feed()   # Should invoke fox.eat() and increase energy and health
marko.bathe()   # Should invoke fox.noise() 

# Print the pet's current energy and health to verify the feed method worked
print(f"Final state: {fox.name}'s energy is {fox.energy} and health is {fox.health}")



