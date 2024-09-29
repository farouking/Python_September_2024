# main.py
from ninja import Ninja
from pet import Pet

# Example usage:
fox = Pet("Fox", "dog", "hunting")
marko = Ninja("Marko", "Rossi", "scooby snack", "milk bone", fox)

marko.walk()   # Should invoke fox.play() and increase health by 5
marko.feed()   # Should invoke fox.eat() and increase energy and health
marko.bathe()  # Should invoke fox.noise()

# Print the pet's current energy and health to verify the feed method worked
print(f"Final state: {fox.name}'s energy is {fox.energy} and health is {fox.health}")
